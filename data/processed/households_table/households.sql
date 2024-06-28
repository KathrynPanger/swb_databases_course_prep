CREATE TABLE public.households
(
    household_id INTEGER PRIMARY KEY,
    lga_id INTEGER,
	FOREIGN KEY (lga_id) REFERENCES lgas (lga_id),
    someone_left VARCHAR(10),
    someone_joined VARCHAR(10),
    health_services_last_month VARCHAR(10),
    household_still_in_state VARCHAR(10),
    someone_moved_away VARCHAR(10),
    bought_petrol_ever VARCHAR(10),
    when_bought_petrol VARCHAR(30),
    liters_petrol_last_bought  INTEGER,
    cost_of_petrol_last_bought INTEGER,
    changed_price_of_petrol_last_month VARCHAR(30),
    food_consumption_last_month VARCHAR(30),
    housing_last_month VARCHAR(30),
    clothing_last_month VARCHAR(30),
    healthcare_standard_last_month VARCHAR(30),
    how_getting_by_financially VARCHAR(30)



);

\COPY households FROM 'households.csv' WITH (FORMAT CSV, HEADER);