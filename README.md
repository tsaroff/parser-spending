# parser-spending
Python3 parser of outgoing transactions, according to the code of the public money manager from API http://api.spending.gov.ua/api/swagger-ui.html

Create database PostgreSQL

Create table 'transaction'

    CREATE TABLE public.transaction (
    id bigint NOT NULL,
    doc_vob integer NOT NULL,
    doc_vob_name character varying(128),
    doc_number character varying(24) NOT NULL,
    doc_date date,
    doc_v_date date,
    trans_date date,
    amount numeric(16,2),
    amount_cop bigint NOT NULL,
    currency character varying(16),
    payer_edrpou character varying(12) NOT NULL,
    payer_name character varying(512),
    payer_account character varying(24) NOT NULL,
    payer_mfo character varying(12) NOT NULL,
    payer_bank character varying(512),
    recipt_edrpou character varying(12) NOT NULL,
    recipt_name character varying(512),
    recipt_account character varying(24) NOT NULL,
    recipt_bank character varying(512),
    recipt_mfo character varying(12) NOT NULL,
    payment_details text,
    doc_add_attr character varying(256),
    region_id integer NOT NULL,
    payment_type character varying(32),
    payment_data character varying(32),
    source_id integer NOT NULL,
    source_name character varying(32)
    );

    ALTER TABLE ONLY public.transaction
    ADD CONSTRAINT transaction_pkey PRIMARY KEY (id);
    

    
connect script to your database in rows 18-24

Using:

    python3 update_transactions.py [code edrpou]

Profit!

