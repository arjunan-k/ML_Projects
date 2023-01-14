CREATE TABLE public.covid_deaths
(
    iso_code character varying(10),
    continent character varying(25),
    location character varying(50),
    date character varying(10),
    population bigint,
    total_cases bigint,
    new_cases bigint,
    new_cases_smoothed numeric(10, 3),
    total_deaths bigint,
    new_deaths bigint,
    new_deaths_smoothed numeric(10, 3),
    total_cases_per_million numeric(10, 3),
    new_cases_per_million numeric(10, 3),
    new_cases_smoothed_per_million numeric(10, 3),
    total_deaths_per_million numeric(10, 3),
    new_deaths_per_million numeric(10, 3),
    new_deaths_smoothed_per_million numeric(10, 3),
    reproduction_rate numeric(10, 3),
    icu_patients integer,
    icu_patients_per_million numeric(10, 3),
    hosp_patients integer,
    hosp_patients_per_million numeric(10, 3),
    weekly_icu_admissions numeric(10, 3),
    weekly_icu_admissions_per_million numeric(10, 3),
    weekly_hosp_admissions numeric(10, 3),
    weekly_hosp_admissions_per_million numeric(10, 3)
);

ALTER TABLE IF EXISTS public.covid_deaths
    OWNER to postgres;



CREATE TABLE public.covid_vaccinations
(
    iso_code character varying(25),
    continent character varying(25),
    location character varying(50),
    date character varying(10),
    new_tests numeric(15, 3),
    total_tests numeric(15, 3),
    total_tests_per_thousand numeric(15, 3),
    new_tests_per_thousand numeric(15, 3),
    new_tests_smoothed numeric(15, 3),
    new_tests_smoothed_per_thousand numeric(15, 3),
    positive_rate numeric(15, 3),
    tests_per_case numeric(10, 3),
    tests_units character varying(25),
    total_vaccinations bigint,
    people_vaccinated bigint,
    people_fully_vaccinated bigint,
    new_vaccinations numeric(10, 3),
    new_vaccinations_smoothed bigint,
    total_vaccinations_per_hundred numeric(10, 3),
    people_vaccinated_per_hundred numeric(10, 3),
    people_fully_vaccinated_per_hundred numeric(10, 3),
    new_vaccinations_smoothed_per_million bigint,
    stringency_index numeric(10, 3),
    population_density numeric(10, 3),
    median_age numeric(10, 3),
    aged_65_older numeric(10, 3),
    aged_70_older numeric(10, 3),
    gdp_per_capita numeric(10, 3),
    extreme_poverty numeric(10, 3),
    cardiovasc_death_rate numeric(10, 3),
    diabetes_prevalence numeric(10, 3),
    female_smokers numeric(10, 3),
    male_smokers numeric(10, 3),
    handwashing_facilities numeric(10, 3),
    hospital_beds_per_thousand numeric(10, 3),
    life_expectancy numeric(10, 3),
    human_development_index numeric(10, 3)
);

ALTER TABLE IF EXISTS public.covid_vaccinations
    OWNER to postgres;
