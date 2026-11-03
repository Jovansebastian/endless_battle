--
-- PostgreSQL database dump
--

\restrict JdKIvomjEJSZf97BhkyeAJ167kJF3S7J2SFxnSyTIaawE9djjzympzTjmLThmRD

-- Dumped from database version 18.4
-- Dumped by pg_dump version 18.4

-- Started on 2026-11-03 09:17:25

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 222 (class 1259 OID 16401)
-- Name: detection_images; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.detection_images (
    id integer NOT NULL,
    original_filename character varying(255) NOT NULL,
    stored_filename character varying(255) NOT NULL,
    image_path text NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);


ALTER TABLE public.detection_images OWNER TO postgres;

--
-- TOC entry 221 (class 1259 OID 16400)
-- Name: detection_images_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.detection_images_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.detection_images_id_seq OWNER TO postgres;

--
-- TOC entry 5037 (class 0 OID 0)
-- Dependencies: 221
-- Name: detection_images_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.detection_images_id_seq OWNED BY public.detection_images.id;


--
-- TOC entry 224 (class 1259 OID 16416)
-- Name: detection_results; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.detection_results (
    id integer NOT NULL,
    image_id integer NOT NULL,
    class_id integer NOT NULL,
    confidence_score numeric(5,4) NOT NULL,
    x_min integer NOT NULL,
    y_min integer NOT NULL,
    x_max integer NOT NULL,
    y_max integer NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);


ALTER TABLE public.detection_results OWNER TO postgres;

--
-- TOC entry 223 (class 1259 OID 16415)
-- Name: detection_results_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.detection_results_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.detection_results_id_seq OWNER TO postgres;

--
-- TOC entry 5038 (class 0 OID 0)
-- Dependencies: 223
-- Name: detection_results_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.detection_results_id_seq OWNED BY public.detection_results.id;


--
-- TOC entry 220 (class 1259 OID 16390)
-- Name: object_classes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.object_classes (
    id integer NOT NULL,
    class_name character varying(100) NOT NULL,
    description text
);


ALTER TABLE public.object_classes OWNER TO postgres;

--
-- TOC entry 219 (class 1259 OID 16389)
-- Name: object_classes_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.object_classes_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.object_classes_id_seq OWNER TO postgres;

--
-- TOC entry 5039 (class 0 OID 0)
-- Dependencies: 219
-- Name: object_classes_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.object_classes_id_seq OWNED BY public.object_classes.id;


--
-- TOC entry 4867 (class 2604 OID 16404)
-- Name: detection_images id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.detection_images ALTER COLUMN id SET DEFAULT nextval('public.detection_images_id_seq'::regclass);


--
-- TOC entry 4869 (class 2604 OID 16419)
-- Name: detection_results id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.detection_results ALTER COLUMN id SET DEFAULT nextval('public.detection_results_id_seq'::regclass);


--
-- TOC entry 4866 (class 2604 OID 16393)
-- Name: object_classes id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.object_classes ALTER COLUMN id SET DEFAULT nextval('public.object_classes_id_seq'::regclass);


--
-- TOC entry 5029 (class 0 OID 16401)
-- Dependencies: 222
-- Data for Name: detection_images; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.detection_images (id, original_filename, stored_filename, image_path, created_at) FROM stdin;
\.


--
-- TOC entry 5031 (class 0 OID 16416)
-- Dependencies: 224
-- Data for Name: detection_results; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.detection_results (id, image_id, class_id, confidence_score, x_min, y_min, x_max, y_max, created_at) FROM stdin;
\.


--
-- TOC entry 5027 (class 0 OID 16390)
-- Dependencies: 220
-- Data for Name: object_classes; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.object_classes (id, class_name, description) FROM stdin;
1	helmet	Pekerja menggunakan helm keselamatan
2	no_helmet	Pekerja tidak menggunakan helm keselamatan
\.


--
-- TOC entry 5040 (class 0 OID 0)
-- Dependencies: 221
-- Name: detection_images_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.detection_images_id_seq', 1, false);


--
-- TOC entry 5041 (class 0 OID 0)
-- Dependencies: 223
-- Name: detection_results_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.detection_results_id_seq', 1, false);


--
-- TOC entry 5042 (class 0 OID 0)
-- Dependencies: 219
-- Name: object_classes_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.object_classes_id_seq', 1, false);


--
-- TOC entry 4874 (class 2606 OID 16414)
-- Name: detection_images detection_images_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.detection_images
    ADD CONSTRAINT detection_images_pkey PRIMARY KEY (id);


--
-- TOC entry 4876 (class 2606 OID 16431)
-- Name: detection_results detection_results_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.detection_results
    ADD CONSTRAINT detection_results_pkey PRIMARY KEY (id);


--
-- TOC entry 4872 (class 2606 OID 16399)
-- Name: object_classes object_classes_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.object_classes
    ADD CONSTRAINT object_classes_pkey PRIMARY KEY (id);


--
-- TOC entry 4877 (class 2606 OID 16437)
-- Name: detection_results detection_results_class_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.detection_results
    ADD CONSTRAINT detection_results_class_id_fkey FOREIGN KEY (class_id) REFERENCES public.object_classes(id) ON DELETE CASCADE;


--
-- TOC entry 4878 (class 2606 OID 16432)
-- Name: detection_results detection_results_image_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.detection_results
    ADD CONSTRAINT detection_results_image_id_fkey FOREIGN KEY (image_id) REFERENCES public.detection_images(id) ON DELETE CASCADE;


-- Completed on 2026-11-03 09:17:25

--
-- PostgreSQL database dump complete
--

\unrestrict JdKIvomjEJSZf97BhkyeAJ167kJF3S7J2SFxnSyTIaawE9djjzympzTjmLThmRD

