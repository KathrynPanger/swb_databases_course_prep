CREATE TABLE public.individuals
(
    individual_id                                 INTEGER PRIMARY KEY,
    household_id                                  INTEGER,
    FOREIGN KEY (household_id) REFERENCES households (household_id),
    is_new_household_member                       VARCHAR(10),
    is_still_household_member                     VARCHAR(10),
    why_leave_household                           VARCHAR(10),
    sex                                           VARCHAR(10),
    age                                           INTEGER,
    relationship_to_head                          VARCHAR(30),
    other_relationship                            TEXT,
    why_join_household                            VARCHAR(30),
    is_covid_vaccinated                           VARCHAR(10),
    is_available_to_respond                       VARCHAR(10),
    worked_for_pay_last_week                      VARCHAR(10),
    has_business_was_absent_last_week             VARCHAR(10),
    when_expected_to_return_to_work,
    VARCHAR(40),
    why_not_work_last_week                        VARCHAR(30),
    other_reason_not_work                         TEXT,
    tried_to_earn_pay_last_month                  VARCHAR(10),
    how_tried_to_earn_pay_last_month              VARCHAR(40),
    other_way_tried_to_earn_pay_last_month        TEXT,
    main_activity_of_employers_business_last_week VARCHAR(40),
    family_farm_food_fate                         VARCHAR(30),
    hours_worked_last_week_main_business_activity INTEGER,
    worked_december_2021                          VARCHAR(10),
    worked_january_2022                           VARCHAR(10),
    worked_february_2022                          VARCHAR(10),
    worked_march_2022                             VARCHAR(10),
    age_started_working                           INTEGER,
    is_employed                                   VARCHAR(10),
    years_worked_first_job                        INTEGER,
    why_left_first_job                            VARCHAR(40),
    how_many_shots                                varchar(30)
);

























);