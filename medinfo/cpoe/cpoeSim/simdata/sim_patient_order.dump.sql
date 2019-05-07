--
-- PostgreSQL database dump
--

-- Dumped from database version 9.6.5
-- Dumped by pg_dump version 10.3

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: sim_patient_order; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.sim_patient_order (sim_patient_order_id, sim_user_id, sim_patient_id, clinical_item_id, relative_time_start, relative_time_end, sim_state_id) FROM stdin;
125	9	13	44256	0	\N	3
78	0	9	41839	0	\N	3
126	9	13	62083	1800	\N	3
127	0	14	45801	-1200	\N	6
128	0	14	45763	-1200	\N	6
129	0	14	45788	-1200	\N	6
130	0	14	45955	-1200	\N	6
131	0	14	45873	-1200	\N	6
132	0	14	45821	-1200	\N	6
114	0	13	45763	-1200	\N	3
115	0	13	45801	-1200	\N	3
116	0	13	45866	-1200	\N	3
117	0	13	45838	-1200	\N	3
118	0	13	45788	-1200	\N	3
119	0	13	45821	-1200	\N	3
120	0	13	41839	0	\N	3
121	9	13	63392	0	\N	3
122	9	13	50706	0	\N	3
123	9	13	45797	0	\N	3
124	9	13	45935	0	\N	3
133	0	14	45918	-1200	\N	6
134	9	14	44198	0	\N	6
135	9	14	45866	0	\N	6
136	9	14	45972	0	\N	6
137	9	14	45910	0	\N	6
138	9	14	57721	0	\N	6
139	9	14	45752	0	\N	6
140	9	14	45945	0	\N	6
141	9	14	43997	0	\N	6
142	9	14	45759	0	\N	6
143	9	14	45792	0	\N	6
144	9	14	49228	0	\N	6
145	0	15	45793	-1200	\N	7
146	0	15	45771	-1200	\N	7
147	0	15	45759	-1200	\N	7
148	0	15	45821	-1200	\N	7
149	0	15	41788	0	\N	7
150	9	15	45969	0	\N	7
151	9	15	49481	0	\N	7
152	9	15	45945	0	\N	7
153	9	15	45927	0	\N	7
154	9	15	48954	0	\N	7
155	9	15	63165	0	\N	7
156	9	15	44219	0	\N	7
157	9	15	45811	0	\N	7
158	9	15	45948	0	\N	7
159	9	15	62866	0	\N	7
160	0	16	45955	-1200	\N	9
161	0	16	45771	-1200	\N	9
162	0	16	45788	-1200	\N	9
163	0	16	45821	-1200	\N	9
164	0	16	45873	-1200	\N	9
165	0	16	42232	0	\N	9
166	9	16	45763	0	\N	9
167	9	16	45806	0	\N	9
168	9	16	44198	0	\N	9
169	9	16	35850	0	\N	9
170	9	16	51920	0	\N	9
171	9	16	45811	0	\N	9
172	9	16	45771	0	\N	9
173	9	16	63927	0	\N	9
174	9	16	45751	0	\N	9
175	9	16	50850	1200	\N	9
178	0	6	41964	0	\N	6
180	0	7	41788	0	\N	7
184	0	18	41788	0	\N	7
185	0	19	41839	0	\N	3
186	0	20	41964	0	\N	6
188	2	17	45793	0	\N	9
189	2	17	45771	0	\N	9
190	2	17	50343	0	\N	9
191	2	17	44198	0	\N	9
192	2	17	45763	1200	\N	9
193	2	17	45797	1200	\N	9
194	2	17	44198	1200	\N	9
195	2	17	35850	1200	\N	9
196	2	17	49549	1200	\N	9
197	2	17	45870	1200	\N	9
198	2	17	61840	1200	\N	9
199	2	17	45778	1200	\N	9
200	2	17	45811	1200	\N	9
201	2	17	45751	1200	\N	9
202	2	17	45752	1200	\N	9
203	2	17	45918	1200	\N	9
204	2	17	45866	1200	\N	9
205	2	17	49134	1200	\N	9
206	2	17	46096	1200	\N	9
207	2	19	45801	0	\N	3
208	2	19	45866	0	\N	3
209	2	19	45771	0	\N	3
210	2	19	48532	0	\N	3
211	2	19	45914	0	\N	3
212	2	19	45788	0	\N	3
213	2	19	44206	1200	\N	3
214	2	19	44256	1200	\N	3
215	2	18	45793	0	\N	7
216	2	18	49481	0	\N	7
217	2	18	45802	0	\N	7
218	2	18	45771	0	\N	7
219	2	18	45945	0	\N	7
220	2	18	44219	0	\N	7
221	2	18	45759	0	\N	7
222	2	18	46348	0	\N	7
223	2	18	45927	0	\N	7
224	2	18	49005	0	\N	7
225	2	18	45748	1200	\N	7
226	2	18	44592	1200	\N	7
227	2	18	45827	1200	\N	7
228	2	20	44198	0	\N	6
229	2	20	63725	0	\N	6
230	2	20	36210	0	\N	6
231	2	20	45752	0	\N	6
232	2	20	45901	0	\N	6
233	2	20	45782	0	\N	6
234	2	20	45751	0	\N	6
235	2	20	45801	0	\N	6
236	2	20	45945	0	\N	6
237	2	20	43997	1200	\N	6
253	0	5	41788	0	\N	14
282	0	23	41788	0	\N	14
283	0	23	41788	0	\N	14
284	0	24	41839	0	\N	3
285	0	25	41964	0	\N	6
291	10	8	45793	0	\N	21
292	10	8	45763	60	\N	21
293	10	8	45797	60	\N	21
294	10	8	50343	60	\N	21
295	10	8	45751	240	\N	21
296	10	8	45818	1200	\N	21
297	10	8	45838	1200	\N	21
298	10	8	45919	1200	\N	21
299	10	8	44439	1380	\N	21
300	10	8	35850	1440	\N	21
301	10	8	45806	1440	\N	21
302	10	8	61840	1440	\N	21
303	10	8	45778	1440	\N	21
304	10	8	45811	1440	\N	21
305	10	8	48916	1440	\N	21
306	10	8	45763	1800	\N	18
308	10	24	45866	0	\N	3
309	10	24	45771	0	\N	3
310	10	24	44206	0	\N	3
311	10	24	45914	0	\N	3
312	10	24	45788	0	\N	3
313	10	24	45818	0	\N	3
314	10	24	45759	0	\N	3
315	10	24	45870	1320	\N	3
316	10	24	45892	2280	\N	3
317	10	24	44212	2280	\N	3
318	10	24	45870	2280	\N	3
319	10	24	45806	2280	\N	3
320	10	24	44240	2520	\N	3
321	10	24	63714	2520	\N	3
322	10	24	44256	2640	\N	3
323	10	24	49251	2640	\N	3
324	10	23	50267	0	\N	14
325	10	23	44198	0	\N	14
326	10	23	49481	0	\N	14
327	10	23	45770	0	\N	14
328	10	23	45771	0	\N	14
329	10	23	45811	0	\N	14
330	10	23	45945	0	\N	14
331	10	23	44219	0	\N	14
332	10	23	45788	0	\N	14
333	10	23	45866	0	\N	14
334	10	23	45759	0	\N	14
335	10	23	46245	1560	\N	15
336	10	23	45927	1620	\N	15
337	10	23	44439	1620	\N	15
338	10	23	45872	1620	\N	15
339	10	23	45877	1620	\N	15
340	10	23	61975	1620	\N	15
341	10	23	43996	1620	\N	15
342	10	23	45793	2880	\N	14
343	10	23	44439	2940	\N	14
344	10	23	44001	4800	\N	14
345	10	23	45969	4860	\N	16
351	0	29	41839	0	\N	3
352	0	30	41964	0	\N	6
353	0	31	41788	0	\N	14
354	11	28	45788	0	\N	21
355	11	28	45827	960	\N	21
356	11	28	45965	960	\N	21
357	11	28	45841	960	\N	21
358	11	28	48515	960	\N	21
359	11	28	45849	960	\N	21
360	11	28	44198	960	\N	21
361	11	28	45870	960	\N	21
362	11	28	45750	960	\N	21
363	11	28	45751	960	\N	21
364	11	28	45755	960	\N	21
365	11	28	45766	960	\N	21
366	11	28	45771	960	\N	21
367	11	28	45901	960	\N	21
368	11	28	45776	960	\N	21
369	11	28	45778	960	\N	21
370	11	28	45781	960	\N	21
371	11	28	45782	960	\N	21
372	11	28	45783	960	\N	21
373	11	28	45787	960	\N	21
374	11	28	46050	960	\N	21
375	11	28	45799	960	\N	21
376	11	28	65641	960	\N	21
377	11	28	45802	960	\N	21
378	11	28	45806	960	\N	21
379	11	28	45811	960	\N	21
380	11	28	45801	960	\N	21
381	11	28	61823	960	\N	21
382	11	28	35850	2580	\N	21
383	11	28	45760	2640	\N	18
384	11	29	45892	0	\N	3
385	11	29	45866	0	\N	3
386	11	29	45771	0	\N	3
387	11	29	44206	0	\N	3
388	11	29	48532	0	\N	3
389	11	29	45870	0	\N	3
390	11	29	45818	0	\N	3
391	11	29	45788	0	\N	3
392	11	29	48676	1380	\N	3
393	11	29	45770	1380	\N	3
394	11	29	45806	1380	\N	3
395	11	29	45811	1380	\N	3
396	11	29	45853	1380	\N	3
397	11	29	45759	1380	\N	3
398	11	29	52590	3540	\N	3
399	11	29	45870	3600	\N	3
400	11	29	45824	3660	\N	3
401	11	29	50100	3660	\N	3
402	11	29	61837	3660	\N	3
403	11	29	45797	3660	\N	3
404	11	31	44198	0	\N	14
405	11	31	49481	0	\N	14
406	11	31	45770	0	\N	14
407	11	31	45771	0	\N	14
408	11	31	45811	0	\N	14
409	11	31	45945	0	\N	14
410	11	31	44219	0	\N	14
411	11	31	45788	0	\N	14
412	11	31	45866	0	\N	14
413	11	31	45759	0	\N	14
414	11	31	45778	600	\N	15
415	11	31	45806	600	\N	15
416	11	31	45927	600	\N	15
417	11	31	65640	1680	\N	15
418	11	31	61823	1680	\N	15
419	11	31	65649	1800	\N	14
420	11	31	61993	1860	\N	14
421	11	31	45793	1920	\N	16
422	11	31	45759	1920	\N	16
423	11	31	49481	2940	\N	16
424	11	30	48960	0	\N	6
425	11	30	44198	0	\N	6
426	11	30	45801	0	\N	6
427	11	30	45771	0	\N	6
428	11	30	49228	0	\N	6
429	11	30	45901	0	\N	6
430	11	30	46157	0	\N	6
431	11	30	36210	0	\N	6
432	11	30	45788	0	\N	6
433	0	32	41839	0	\N	3
434	0	34	41964	0	\N	6
435	0	35	41788	0	\N	14
436	12	33	45788	0	\N	21
437	12	33	45763	960	\N	21
438	12	33	50343	960	\N	21
439	12	33	45763	1980	\N	21
440	12	33	44198	1980	\N	21
441	12	33	62151	1980	\N	21
442	12	33	35850	1980	\N	21
443	12	33	44267	1980	\N	21
444	12	33	45901	1980	\N	21
445	12	33	61840	1980	\N	21
446	12	33	45873	1980	\N	21
447	12	33	45778	1980	\N	21
448	12	33	45811	1980	\N	21
449	12	33	44021	1980	\N	21
450	12	33	45752	1980	\N	21
451	12	33	45818	1980	\N	21
452	12	33	44283	1980	\N	21
453	12	33	44220	1980	\N	21
454	12	32	44294	0	\N	3
455	12	32	45866	0	\N	3
456	12	32	45771	0	\N	3
457	12	32	45900	0	\N	3
458	12	32	45870	0	\N	3
459	12	32	44206	0	\N	3
460	12	32	45914	0	\N	3
461	12	32	45788	0	\N	3
462	12	32	45818	0	\N	3
463	12	32	45759	0	\N	3
464	12	32	44256	1500	\N	3
465	12	32	46081	1500	\N	3
466	12	32	49251	1500	\N	3
467	12	32	44359	1500	\N	3
468	12	32	45866	1500	\N	3
469	12	32	45870	1500	\N	3
470	12	32	48628	1500	\N	3
471	12	32	45977	1500	\N	3
472	12	35	45945	0	\N	14
473	12	35	45771	0	\N	14
474	12	35	45788	0	\N	14
475	12	35	45869	0	\N	14
476	12	35	45759	0	\N	14
477	12	35	44219	300	\N	14
478	12	35	43996	300	\N	14
479	12	35	35733	300	\N	14
480	12	35	49481	480	\N	14
481	12	35	45969	480	\N	14
482	12	35	45793	1500	\N	15
483	12	35	65640	1560	\N	15
484	12	35	61993	1560	\N	15
485	12	35	65646	1560	\N	15
486	12	35	61975	1560	\N	15
487	12	35	46286	1800	\N	16
488	12	35	44404	1860	\N	16
489	12	35	49481	3720	\N	16
490	12	34	48960	0	\N	6
491	12	34	45955	0	\N	6
492	12	34	44198	0	\N	6
493	12	34	45801	0	\N	6
494	12	34	45771	0	\N	6
495	12	34	49228	0	\N	6
496	12	34	45873	0	\N	6
497	12	34	36210	0	\N	6
498	12	34	45788	0	\N	6
499	12	34	44198	1440	\N	6
500	0	37	41839	0	\N	3
501	0	38	41964	0	\N	6
502	0	39	41788	0	\N	14
503	13	36	45793	0	\N	21
504	13	36	45778	960	\N	21
505	13	36	45763	960	\N	21
506	13	36	45788	960	\N	21
507	13	36	45910	960	\N	21
508	13	36	45806	960	\N	21
509	13	36	46093	1260	\N	21
510	13	36	45763	2220	\N	21
511	13	36	45796	2220	\N	21
512	13	36	45797	2220	\N	21
513	13	36	44198	2220	\N	21
514	13	36	35850	2220	\N	21
515	13	36	49549	2220	\N	21
516	13	36	61840	2220	\N	21
517	13	36	45778	2220	\N	21
518	13	36	45811	2220	\N	21
519	13	36	48916	2220	\N	21
520	13	36	44021	2220	\N	21
521	13	36	45751	2220	\N	21
522	13	36	45752	2220	\N	21
523	13	36	45918	2220	\N	21
524	13	36	45919	2220	\N	21
525	13	37	44256	0	\N	3
526	13	37	45892	0	\N	3
527	13	37	45866	0	\N	3
528	13	37	45771	0	\N	3
529	13	37	45838	0	\N	3
530	13	37	44206	0	\N	3
531	13	37	45870	0	\N	3
532	13	37	45818	0	\N	3
533	13	37	45788	0	\N	3
534	13	37	45759	0	\N	3
535	13	37	46160	1500	\N	3
536	13	37	48871	1560	\N	3
537	13	37	45811	1620	\N	3
538	13	37	71052	2580	\N	3
539	13	37	61982	2580	\N	3
540	13	39	45793	0	\N	14
541	13	39	44198	0	\N	14
542	13	39	49481	0	\N	14
543	13	39	45770	0	\N	14
544	13	39	45771	0	\N	14
545	13	39	43996	0	\N	14
546	13	39	45811	0	\N	14
547	13	39	49207	0	\N	14
548	13	39	45945	0	\N	14
549	13	39	44219	0	\N	14
550	13	39	45788	0	\N	14
551	13	39	45866	0	\N	14
552	13	39	45759	0	\N	14
553	13	39	45969	1680	\N	15
554	13	39	61982	1680	\N	15
555	13	39	61993	1680	\N	15
556	13	39	45872	1860	\N	15
557	13	39	65640	1860	\N	15
558	13	39	61975	1860	\N	15
559	13	39	63759	1860	\N	15
560	13	39	45927	1860	\N	15
561	13	39	61323	2160	\N	14
562	13	39	61982	2160	\N	14
563	13	39	45872	2280	\N	14
564	13	39	61993	2280	\N	14
565	13	39	45793	2400	\N	16
566	13	39	45759	2400	\N	16
567	13	39	49481	2520	\N	16
568	13	39	63720	2580	\N	2
569	13	39	46343	2580	\N	2
570	13	38	48960	0	\N	6
571	13	38	44198	0	\N	6
572	13	38	45801	0	\N	6
573	13	38	45771	0	\N	6
574	13	38	49228	0	\N	6
575	13	38	46157	0	\N	6
576	13	38	45806	0	\N	6
577	13	38	36210	0	\N	6
578	13	38	44439	0	\N	6
579	13	38	45752	0	\N	6
580	13	38	45788	0	\N	6
581	13	38	43997	0	\N	6
582	13	38	45811	1620	\N	6
583	13	38	45919	1620	\N	6
691	0	49	41870	0	\N	40
824	0	48	42197	0	\N	30
825	0	50	41759	0	\N	5000
\.


--
-- Name: sim_patient_order_sim_patient_order_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.sim_patient_order_sim_patient_order_id_seq', 889, true);


--
-- PostgreSQL database dump complete
--

