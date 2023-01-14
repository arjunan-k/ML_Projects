# Tableau Queries
## 1. Showing the Total Death Percentage Per Total Cases
```sql
SELECT SUM(new_cases) as total_cases, SUM(new_deaths) as total_death,
(SUM(new_deaths)/SUM(new_cases)) * 100 AS deathpercentage
FROM covid_deaths
WHERE CONTINENT IS NOT NULL
HAVING (SUM(new_deaths)/SUM(new_cases)) IS NOT NULL
ORDER BY total_cases DESC
```

## 2. Total Death Count Per Location
```sql
SELECT LOCATION, SUM(cast(new_deaths as int)) as total_death_count
FROM covid_deaths
WHERE continent is null 
AND location NOT IN ('World', 'European Union', 'International')
GROUP BY location
ORDER BY total_death_count DESC
```
## 3. Finding Percentage of Population Infected
```sql
SELECT location, population, COALESCE(MAX(total_cases), 0) AS highest_infection_count, 
COALESCE(MAX((total_cases/population)) * 100, 0) AS percent_population_infected
FROM covid_deaths
GROUP BY location, population
ORDER BY percent_population_infected DESC
```
## 4. Finding Percentage of Population Infected with Date 
```sql
SELECT location, 
COALESCE(population, 0), 
date,
COALESCE(MAX(total_cases), 0) AS highest_infection_count, 
COALESCE(MAX((total_cases/population)) * 100, 0) AS percent_population_infected
FROM covid_deaths
GROUP BY location, population, date
ORDER BY percent_population_infected DESC
```
