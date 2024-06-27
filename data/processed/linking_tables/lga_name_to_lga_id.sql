CREATE TABLE public.lgas
(
    lga_id INTEGER PRIMARY KEY,
    name VARCHAR(30)
);

\COPY lgas FROM 'lga_name_to_lga_id.csv' WITH (FORMAT CSV, HEADER);