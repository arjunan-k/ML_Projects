# Covid Death Analysis
```sql
SELECT * FROM covid_deaths            -- Complete dataset of covid_deaths
SELECT * FROM covid_vaccinations      -- Complete dataset of covid_vaccinations
```
# Dataset of covid_deaths
```sql
SELECT location, date, total_cases, new_cases, total_deaths, population 
FROM covid_deaths
```
# Comparison of Total Cases v/s Total Deaths
Shows the percentage chance of dying if you get infected
```sql
SELECT location, date, total_cases, total_deaths, population, 
(total_deaths/total_cases) * 100 AS death_percentage
FROM covid_deaths
WHERE location ILIKE '%india%'
ORDER BY death_percentage DESC
```
# Comparison of Total Cases v/s Population
```sql
SELECT location, date, population, total_cases, 
(total_cases/population) * 100 AS infected_population
FROM covid_deaths
ORDER BY infected_population DESC

# ----- Top 10 infected Country ----- #

SELECT location, population, MAX(total_cases), 
MAX((total_cases/population)) * 100 AS infected_population
FROM covid_deaths
WHERE ((total_cases/population) * 100) IS NOT NULL
GROUP BY location, population
ORDER BY infected_population DESC
LIMIT 10
```
# Showing Top 10 Countries with Highest Death Count Per Population
```sql
SELECT location, continent, population, MAX(total_deaths) AS total_death_count
FROM covid_deaths
WHERE total_deaths IS NOT NULL AND continent IS NOT NULL
GROUP BY location, population, continent
ORDER BY total_death_count DESC
LIMIT 10

# ----- Death count in continents ----- #

SELECT location, MAX(total_deaths) AS total_death_count
FROM covid_deaths
WHERE continent IS NULL
GROUP BY location
ORDER BY total_death_count DESC
```
# Showing the Total Death Percentage Per Date
```sql
SELECT SUM(new_cases) as total_cases, SUM(new_deaths) as total_death,
(SUM(new_deaths)/SUM(new_cases)) * 100 AS deathpercentage
FROM covid_deaths
WHERE CONTINENT IS NOT NULL
# GROUP BY date
HAVING (SUM(new_deaths)/SUM(new_cases)) IS NOT NULL
ORDER BY total_cases DESC
```
# Total Population v/s Vaccinations
```sql
SELECT cd.continent, cd.location, cd.date, 
cd.population, cv.new_vaccinations, 
    SUM(cv.new_vaccinations) 
    OVER (PARTITION BY cd.location ORDER BY cd.location , cd.date) AS RollingPeopleVaccinations
    
FROM covid_deaths AS cd
INNER JOIN covid_vaccinations AS cv
ON cd.location = cv.location AND cd.date = cv.date
WHERE cd.continent IS NOT NULL AND cv.new_vaccinations IS NOT NULL
ORDER BY 2, 3
# LIMIT 25
```
# Percentage of Total Population v/s Total Vaccinations Using CTE (Common Table Expression)
```sql
WITH PopvsVac
AS 
(
SELECT cd.continent, cd.location, cd.date, 
cd.population, cv.new_vaccinations, 
    SUM(cv.new_vaccinations) 
    OVER (PARTITION BY cd.location ORDER BY cd.location , cd.date) AS rolling_people_vaccinations
    
FROM covid_deaths AS cd
INNER JOIN covid_vaccinations AS cv
ON cd.location = cv.location AND cd.date = cv.date
WHERE cd.continent IS NOT NULL AND cv.new_vaccinations IS NOT NULL
ORDER BY 2, 3
)

SELECT *, (rolling_people_vaccinations/population)*100 FROM PopvsVac
# LIMIT 25
```
# Percentage of Total Population v/s Total Vaccinations Using Temp Table
```sql
DROP TABLE IF EXISTS PopvsVac;

CREATE TEMP TABLE PopvsVac(
    continent VARCHAR(255),
    location VARCHAR(255),
    date VARCHAR(255),
    population BIGINT,
    new_vaccinations BIGINT,
    rolling_people_vaccinations NUMERIC
);

INSERT INTO PopvsVac(continent, location, date, population, new_vaccinations, rolling_people_vaccinations)
(
SELECT cd.continent, cd.location, cd.date, 
cd.population, cv.new_vaccinations, 
    SUM(cv.new_vaccinations) 
    OVER (PARTITION BY cd.location ORDER BY cd.location , cd.date) AS rolling_people_vaccinations
    
FROM covid_deaths AS cd
INNER JOIN covid_vaccinations AS cv
ON cd.location = cv.location AND cd.date = cv.date
WHERE cd.continent IS NOT NULL AND cv.new_vaccinations IS NOT NULL
ORDER BY 2, 3
)

SELECT *, (rolling_people_vaccinations/population)*100 FROM PopvsVac
# LIMIT 25
```
# Creating Views for later Visualizations
```sql
CREATE VIEW percent_population_vaccinated AS 
(
SELECT cd.continent, cd.location, cd.date, 
cd.population, cv.new_vaccinations, 
    SUM(cv.new_vaccinations) 
    OVER (PARTITION BY cd.location ORDER BY cd.location , cd.date) AS rolling_people_vaccinations
    
FROM covid_deaths AS cd
INNER JOIN covid_vaccinations AS cv
ON cd.location = cv.location AND cd.date = cv.date
WHERE cd.continent IS NOT NULL
)

# SELECT * FROM percent_population_vaccinated
```

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
