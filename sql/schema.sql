-- Create the database
CREATE DATABASE job_market;
USE job_market;

-- Note: jobs_clean was created by importing data/clean/jobs_clean.csv
-- using the Table Data Import Wizard in MySQL Workbench.

-- Helper table with counting numbers (used to split skills).
-- The most skills any job has is 6, so 6 numbers are enough.
CREATE TABLE numbers (n INT);
INSERT INTO numbers VALUES (1),(2),(3),(4),(5),(6);

-- Skills table: one skill per row
CREATE TABLE job_skills AS
SELECT j.Job_ID,
       TRIM(SUBSTRING_INDEX(SUBSTRING_INDEX(j.Skills_Required, ',', numbers.n), ',', -1)) AS Skill
FROM jobs_clean j
JOIN numbers
  ON numbers.n <= 1 + LENGTH(j.Skills_Required) - LENGTH(REPLACE(j.Skills_Required, ',', ''));
