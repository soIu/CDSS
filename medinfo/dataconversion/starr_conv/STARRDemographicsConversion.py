#!/usr/bin/env python

import sys, os
import time
from itertools import islice
from datetime import datetime
from medinfo.common.Util import ProgressDots
from medinfo.db import DBUtil
from medinfo.db.Model import SQLQuery
from medinfo.db.Model import RowItemModel

from scripts.GoogleCloud.BQ.BigQueryConnect_py2 import BigQueryConnect

from medinfo.dataconversion.Util import log

from google.cloud import bigquery

SOURCE_TABLE = 'starr_datalake2018.demographic'

UNSPECIFIED_RACE_ETHNICITY = ("Unknown","Other")
HISPANIC_LATINO_ETHNICITY = "HISPANIC/LATINO"
RACE_MAPPINGS = \
    {
        None: "Unknown",
        "": "Unknown",
        "American Indian or Alaska Native": "Native American",
        "AMERICAN INDIAN OR ALASKA NATIVE": "Native American",
        "ASIAN - HISTORICAL CONV": "Asian",
        "Asian": "Asian",
        "ASIAN": "Asian",
        "ASIAN, HISPANIC": "Asian",
        "Asian, non-Hispanic": "Asian",
        "ASIAN, NON-HISPANIC": "Asian",
        "Black": "Black",
        "Black or African American": "Black",
        "BLACK OR AFRICAN AMERICAN": "Black",
        "Black, Hispanic": "Black",
        "BLACK, HISPANIC": "Black",
        "Black, non-Hispanic": "Black",
        "BLACK, NON-HISPANIC": "Black",
        "Native American": "Native American",
        "NATIVE AMERICAN, HISPANIC": "Native American",
        "Native American, non-Hispanic": "Native American",
        "NATIVE AMERICAN, NON-HISPANIC": "Native American",
        "Native Hawaiian or Other Pacific Islander": "Pacific Islander",
        "NATIVE HAWAIIAN OR OTHER PACIFIC ISLANDER": "Pacific Islander",
        "NATIVE HAWAIIAN OR OTHER PACIFIC ISLANDER ": "Pacific Islander",
        "Other": "Other",
        "OTHER": "Other",
        "Other, Hispanic": "Hispanic/Latino",
        "OTHER, HISPANIC": "Hispanic/Latino",
        "Other, non-Hispanic": "Other",
        "OTHER, NON-HISPANIC": "Other",
        "Pacific Islander": "Pacific Islander",
        "Pacific Islander, non-Hispanic": "Pacific Islander",
        "PACIFIC ISLANDER, NON-HISPANIC": "Pacific Islander",
        "Patient Refused": "Unknown",
        "PATIENT REFUSED": "Unknown",
        "Race and Ethnicity Unknown": "Unknown",
        "RACE AND ETHNICITY UNKNOWN": "Unknown",
        "Unknown": "Unknown",
        "UNKNOWN": "Unknown",
        "White": "White (%s)",
        "WHITE": "White (%s)",  # Subset by ethnicity Hispanic/Latino
        "White, Hispanic": "White (Hispanic/Latino)",
        "WHITE, HISPANIC": "White (Hispanic/Latino)",
        "White, non-Hispanic": "White (Non-Hispanic/Latino)",
        "WHITE, NON-HISPANIC": "White (Non-Hispanic/Latino)",
        HISPANIC_LATINO_ETHNICITY: "Hispanic/Latino"
    }

class STARRDemographicsConversion:
    """Data conversion module to take STARR provided patient demographics data
    into the structured data tables to facilitate subsequent analysis.

    Capturing death date for now as an event.
    """
    connFactory = None # Allow specification of alternative DB connection source

    categoryBySourceDescr = None   # Local cache to track the clinical item category table contents
    clinicalItemByCategoryIdExtId = None   # Local cache to track clinical item table contents

    def __init__(self):
        """Default constructor"""
        self.bqconn = BigQueryConnect()
        self.connFactory = DBUtil.ConnectionFactory();  # Default connection source

        self.categoryBySourceDescr = dict()
        self.clinicalItemByCategoryIdExtId = dict()

    def convertItemsByBatch(self, patientIdsFile, batchSize=10000, tempDir='/tmp/', removeCsvs=True, datasetId='starr_datalake2018', skipFirstLine=True):
        # split pat ids into blocks
        # for each split
            # convert to local postgres db
            # dump local postgres db to csv
            # upload csv to BQ clinical item
            # clean up

        log.info('Batch size is %s \n\n' % batchSize)

        def getBatch(file, num_lines):
            return [line.strip() for line in islice(file, num_lines)]

        with open(patientIdsFile, 'r') as f:
            if skipFirstLine: firstLine = f.readline()
            idsBatch = getBatch(f, batchSize)
            batchCounter = 0
            while idsBatch:
                log.info('Processing batch %s' % batchCounter)
                log.info('Batch %s contains ids %s to %s' % (batchCounter, (batchSize*batchCounter+1), (batchSize*(batchCounter+1))) )

                self.convertSourceItems(idsBatch)

                self.dumpPatientItemToCsv(tempDir, batchCounter)

                self.uploadPatientItemCsvToBQ(tempDir, batchCounter, datasetId)

                if removeCsvs:
                    self.removePatientItemCsv(tempDir, batchCounter)

                self.removePatientItemAddedLines()

                log.info('Finished with batch %s \n\n' % batchCounter)
                idsBatch = getBatch(f, batchSize)
                batchCounter += 1

        self.dumpClinicalTablesToCsv(tempDir)
        self.uploadClinicalTablesCsvToBQ(tempDir, datasetId)
        self.removeClinicalTablesCsv(tempDir)
        self.removeClinicalTablesAddedLines()



    def dumpPatientItemToCsv(self, tempDir, batchCounter):
        log.info('Dumping patient_item for batch %s to CSV' % batchCounter)

        DBUtil.execute \
                (
                '''
                COPY patient_item TO '%s/%s_patient_item.csv' DELIMITER ',' CSV;
                ''' % (tempDir, batchCounter)
            )

    def dumpClinicalTablesToCsv(self, tempDir):
        log.info('Dumping clinical_item and clinical_item_category to CSV')

        DBUtil.execute \
            (
                '''
                COPY clinical_item TO '%s/clinical_item.csv' DELIMITER ',' CSV;
                ''' % tempDir
            )

        DBUtil.execute \
                (
                '''
                COPY clinical_item_category TO '%s/clinical_item_category.csv' DELIMITER ',' CSV;
                ''' % tempDir
            )


    def uploadPatientItemCsvToBQ(self, tempDir, batchCounter, datasetId):
        log.info('Uploading patient_item CSV to BQ dataset %s for batch %s' % (datasetId, batchCounter) )
        patient_item_schema = [bigquery.SchemaField('patient_item_id', 'INT64', 'REQUIRED', None, ()),
                               bigquery.SchemaField('external_id', 'INT64', 'NULLABLE', None, ()),
                               bigquery.SchemaField('patient_id', 'INT64', 'REQUIRED', None, ()),
                               bigquery.SchemaField('clinical_item_id', 'INT64', 'REQUIRED', None, ()),
                               bigquery.SchemaField('item_date', 'TIMESTAMP', 'REQUIRED', None, ()),
                               bigquery.SchemaField('analyze_date', 'TIMESTAMP', 'NULLABLE', None, ()),
                               bigquery.SchemaField('encounter_id', 'INT64', 'NULLABLE', None, ()),
                               bigquery.SchemaField('text_value', 'STRING', 'NULLABLE', None, ()),
                               bigquery.SchemaField('num_value', 'FLOAT64', 'NULLABLE', None, ()),
                               bigquery.SchemaField('source_id', 'INT64', 'NULLABLE', None, ())]

        self.bqconn.load_csv_to_table(datasetId, 'patient_item',
                                      tempDir + '/' + str(batchCounter) + '_patient_item.csv', skip_rows=0,
                                      append_to_table=True)
                                      # auto_detect_schema=False, schema=patient_item_schema)

    def uploadClinicalTablesCsvToBQ(self, tempDir, datasetId):
        log.info('Uploading clinical_item and clinical_item_category CSVs to BQ dataset %s' % datasetId )
        clinical_item_category_schema = [
            bigquery.SchemaField('clinical_item_category_id', 'INT64', 'REQUIRED', None, ()),
            bigquery.SchemaField('source_table', 'STRING', 'REQUIRED', None, ()),
            bigquery.SchemaField('description', 'STRING', 'NULLABLE', None, ()),
            bigquery.SchemaField('default_recommend', 'INT64', 'NULLABLE', None, ())]

        self.bqconn.load_csv_to_table(datasetId, 'clinical_item_category', tempDir + '/clinical_item_category.csv',
                                      skip_rows=0, append_to_table=True)
                                      # auto_detect_schema=False, schema=clinical_item_category_schema)

        clinical_item_schema = [bigquery.SchemaField('clinical_item_id', 'INT64', 'REQUIRED', None, ()),
                                bigquery.SchemaField('clinical_item_category_id', 'INT64', 'REQUIRED', None, ()),
                                bigquery.SchemaField('external_id', 'INT64', 'NULLABLE', None, ()),
                                bigquery.SchemaField('name', 'STRING', 'REQUIRED', None, ()),
                                bigquery.SchemaField('description', 'STRING', 'NULLABLE', None, ()),
                                bigquery.SchemaField('default_recommend', 'INT64', 'NULLABLE', None, ()),
                                bigquery.SchemaField('item_count', 'FLOAT64', 'NULLABLE', None, ()),
                                bigquery.SchemaField('patient_count', 'FLOAT64', 'NULLABLE', None, ()),
                                bigquery.SchemaField('encounter_count', 'FLOAT64', 'NULLABLE', None, ()),
                                bigquery.SchemaField('analysis_status', 'INT64', 'NULLABLE', None, ()),
                                bigquery.SchemaField('outcome_interest', 'INT64', 'NULLABLE', None, ())]
        self.bqconn.load_csv_to_table(datasetId, 'clinical_item', tempDir + '/clinical_item.csv',
                                      skip_rows=0, append_to_table=True)
                                      # auto_detect_schema=False, schema=clinical_item_schema)

    def removePatientItemCsv(self, tempDir, batchCounter):
        log.info('Removing patient_item CSV for batch %s' % batchCounter)
        if os.path.exists(tempDir + '/' + str(batchCounter) + '_patient_item.csv'):
            os.remove(tempDir + '/' + str(batchCounter) + '_patient_item.csv')
        else:
            print(tempDir + '/' + str(batchCounter) + '_patient_item.csv does not exist')

    def removeClinicalTablesCsv(self, tempDir):
        log.info('Removing clinical_item and clinical_item_category CSVs')
        if os.path.exists(tempDir + '/clinical_item.csv'):
            os.remove(tempDir + '/clinical_item.csv')
        else:
            print(tempDir + '/clinical_item.csv does not exist')

        if os.path.exists(tempDir + '/clinical_item_category.csv'):
            os.remove(tempDir + '/clinical_item_category.csv')
        else:
            print(tempDir + '/clinical_item_category.csv does not exist')


    def removePatientItemAddedLines(self):
        """delete added records"""
        log.info('Removing patient_item added lines in PSQL DB')

        DBUtil.execute \
            ("""delete from patient_item 
                    where clinical_item_id in 
                    (   select clinical_item_id
                        from clinical_item as ci, clinical_item_category as cic
                        where ci.clinical_item_category_id = cic.clinical_item_category_id
                        and cic.source_table = '%s'
                    );
                    """ % SOURCE_TABLE
             )

    def removeClinicalTablesAddedLines(self):
        """delete added records"""
        log.info('Removing clinical_item and clinical_item_category added lines in PSQL DB')

        DBUtil.execute \
            ("""delete from clinical_item 
                    where clinical_item_category_id in 
                    (   select clinical_item_category_id 
                        from clinical_item_category 
                        where source_table = '%s'
                    );
                    """ % SOURCE_TABLE
             )
        DBUtil.execute("delete from clinical_item_category where source_table = '%s';" % SOURCE_TABLE)


    def convertSourceItems(self, patientIds=None):
        """Primary run function to process the contents of the stride_patient
        table and convert them into equivalent patient_item, clinical_item, and clinical_item_category entries.
        Should look for redundancies to avoid repeating conversion.

        patientIds - If provided, only process items for patient IDs matching those provided
        """
        log.info("Conversion for patients starting with: %s, %s total" % (patientIds[:5], len(patientIds)) )
        progress = ProgressDots()

        with self.connFactory.connection() as conn:
            for sourceItem in self.querySourceItems(patientIds, progress=progress):
                self.convertSourceItem(sourceItem, conn=conn)

    def convertSourceItem(self, sourceItem, conn=None):
        """Given an individual sourceItem record, produce / convert it into an equivalent
        item record in the analysis database.
        """
        # Normalize sourceItem data into hierachical components (category -> clinical_item -> patient_item).
        #   Relatively small / finite number of categories and clinical_items, so these should only have to be instantiated
        #   in a first past, with subsequent calls just yielding back in memory cached copies
        categoryModel = self.categoryFromSourceItem(sourceItem, conn=conn)
        clinicalItemModel = self.clinicalItemFromSourceItem(sourceItem, categoryModel, conn=conn)
        patientItemModel = self.patientItemModelFromSourceItem(sourceItem, clinicalItemModel, conn=conn)

    def querySourceItems(self, patientIds=None, progress=None, debug=False):
        """Query the database for list of all patient demographics
        and yield the results one at a time.  If patientIds provided, only return items
        matching those IDs.
        """
        # Column headers to query for that map to respective fields in analysis table
        headers = ["rit_uid","birth_date_jittered","gender","death_date_jittered","canonical_race","canonical_ethnicity"]

        # TODO need to fix for BQ SQL
        '''
        query = SQLQuery()
        for header in headers:
            query.addSelect( header )
        query.addFrom("starr_datalake2018.demographic as dem")
        if patientIds is not None:
            query.addWhereIn("dem.rit_uid", patientIds)
        '''

        query = '''
                SELECT rit_uid,birth_date_jittered,gender,death_date_jittered,canonical_race,canonical_ethnicity
                FROM starr_datalake2018.demographic as dem
                WHERE dem.rit_uid IN UNNEST(@pat_ids)
                '''

        query_params = [
            bigquery.ArrayQueryParameter('pat_ids', 'STRING', patientIds),
        ]

        if debug:
            print(query)
            print(query_params)

        query_job = self.bqconn.queryBQ(str(query), query_params=query_params, location='US', batch_mode=False, verbose=True)

        if debug:
            for row in query_job:
                print(row)

        for row in query_job:  # API request - fetches results
            # Row values can be accessed by field name or index
            # assert row[0] == row.name == row["name"]
            rowModel = RowItemModel( row.values(), headers )

            if rowModel["birth_date_jittered"] is None:
                # Blank values, doesn't make sense.  Skip it
                log.warning(rowModel)
            else:
                # Record birth at resolution of year
                rowModel["itemDate"] = datetime(rowModel["birth_date_jittered"].year,1,1)
                rowModel["name"] = "Birth"
                rowModel["description"] = "Birth Year"
                yield rowModel

                # Record another at resolution of decade
                decade = (rowModel["birth_date_jittered"].year / 10) * 10
                rowModel["itemDate"] = datetime(rowModel["birth_date_jittered"].year,1,1)
                rowModel["name"] = "Birth%ds" % decade
                rowModel["description"] = "Birth Decade %ds" % decade
                yield rowModel

                # Summarize race and ethnicity information into single field of interest
                raceEthnicity = self.summarizeRaceEthnicity(rowModel)
                rowModel["itemDate"] = datetime(rowModel["birth_date_jittered"].year,1,1)
                rowModel["name"] = "Race"+(raceEthnicity.translate(None," ()-/"))   # Strip off punctuation
                rowModel["description"] = "Race/Ethnicity: %s" % raceEthnicity
                yield rowModel


                gender = rowModel["gender"].title()
                rowModel["name"] = gender
                rowModel["description"] = "%s Gender" % gender
                yield rowModel

                if rowModel["death_date_jittered"] is not None:
                    rowModel["name"] = "Death"
                    rowModel["description"] = "Death Date"
                    rowModel["itemDate"] = rowModel["death_date_jittered"]
                    yield rowModel

            progress.Update()


    def summarizeRaceEthnicity(self, rowModel):
        """Given row model with patient information, return a single string to summarize the patient's race and ethnicity information"""
        raceEthnicity = RACE_MAPPINGS[rowModel["canonical_race"]]
        if raceEthnicity in UNSPECIFIED_RACE_ETHNICITY and rowModel["canonical_ethnicity"] == HISPANIC_LATINO_ETHNICITY:
            raceEthnicity = RACE_MAPPINGS[HISPANIC_LATINO_ETHNICITY]   # Use Hispanic/Latino as basis if no other information
        if raceEthnicity.find("%s") >= 0:    # Found replacement string.  Look to ethnicity for more information
            if rowModel["canonical_ethnicity"] == HISPANIC_LATINO_ETHNICITY:
                raceEthnicity = raceEthnicity % RACE_MAPPINGS[HISPANIC_LATINO_ETHNICITY]
            else:
                raceEthnicity = raceEthnicity % ("Non-"+RACE_MAPPINGS[HISPANIC_LATINO_ETHNICITY])
        return raceEthnicity

    def categoryFromSourceItem(self, sourceItem, conn):
        # Load or produce a clinical_item_category record model for the given sourceItem
        categoryKey = (SOURCE_TABLE, "Demographics")
        if categoryKey not in self.categoryBySourceDescr:
            # Category does not yet exist in the local cache.  Check if in database table (if not, persist a new record)
            category = \
                RowItemModel \
                    ({"source_table": SOURCE_TABLE,
                      "description": "Demographics",
                      }
                     )
            
            (categoryId, isNew) = DBUtil.findOrInsertItem("clinical_item_category", category, conn=conn)
            category["clinical_item_category_id"] = categoryId
            self.categoryBySourceDescr[categoryKey] = category
        return self.categoryBySourceDescr[categoryKey]

    def clinicalItemFromSourceItem(self, sourceItem, category, conn):
        # Load or produce a clinical_item record model for the given sourceItem
        clinicalItemKey = (category["clinical_item_category_id"], sourceItem["name"])
        if clinicalItemKey not in self.clinicalItemByCategoryIdExtId:
            # Clinical Item does not yet exist in the local cache.  Check if in database table (if not, persist a new record)
            clinicalItem = \
                RowItemModel \
                    ({"clinical_item_category_id": category["clinical_item_category_id"],
                      "external_id": None,
                      "name": sourceItem["name"],
                      "description": sourceItem["description"],
                      }
                     )
            (clinicalItemId, isNew) = DBUtil.findOrInsertItem("clinical_item", clinicalItem, conn=conn)
            clinicalItem["clinical_item_id"] = clinicalItemId
            self.clinicalItemByCategoryIdExtId[clinicalItemKey] = clinicalItem
        return self.clinicalItemByCategoryIdExtId[clinicalItemKey]

    def patientItemModelFromSourceItem(self, sourceItem, clinicalItem, conn):
        # Produce a patient_item record model for the given sourceItem
        patientItem = \
            RowItemModel \
                ({"external_id": None,
                  "patient_id": int(sourceItem["rit_uid"][2:], 16),
                  "encounter_id": None,
                  "clinical_item_id": clinicalItem["clinical_item_id"],
                  "item_date": sourceItem["itemDate"],
                  }
                 )
        insertQuery = DBUtil.buildInsertQuery("patient_item", patientItem.keys())
        insertParams = patientItem.values()
        try:
            # Optimistic insert of a new unique item
            DBUtil.execute(insertQuery, insertParams, conn=conn)
        except conn.IntegrityError, err:
            # If turns out to be a duplicate, okay, just note it and continue to insert whatever else is possible
            log.info(err);