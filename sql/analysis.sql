USE job_market;

-- Quick checks
SELECT COUNT(*) FROM jobs_clean;
SELECT COUNT(*) FROM job_skills;

-- Q1: What skills are most wanted for entry level analysts?
SELECT s.Skill,
       COUNT(*) AS jobs,
       ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM jobs_clean
                                 WHERE Is_Entry_Level = 'True' AND Is_Analyst = 'True'), 1) AS percent_of_jobs
FROM job_skills s
JOIN jobs_clean j ON j.Job_ID = s.Job_ID
WHERE j.Is_Entry_Level = 'True' AND j.Is_Analyst = 'True'
GROUP BY s.Skill
ORDER BY jobs DESC
LIMIT 10;

-- Q2: Which cities hire the most analysts?
SELECT City, COUNT(*) AS total_jobs
FROM jobs_clean
WHERE Is_Analyst = 'True' AND City != 'Remote'
GROUP BY City
ORDER BY total_jobs DESC
LIMIT 5;

-- Q3: Startups or big companies, who hires more entry level analysts?
SELECT Company_Type,
       COUNT(*) AS jobs,
       SUM(Openings) AS total_openings,
       ROUND(AVG(Salary_LPA), 1) AS avg_salary_lpa
FROM jobs_clean
WHERE Is_Entry_Level = 'True' AND Is_Analyst = 'True'
GROUP BY Company_Type
ORDER BY jobs DESC;

-- Q3b: How many people compete for each opening?
SELECT Company_Type,
       SUM(Openings) AS total_openings,
       SUM(Applicants) AS total_applicants,
       ROUND(SUM(Applicants) / SUM(Openings), 1) AS applicants_per_opening
FROM jobs_clean
WHERE Is_Entry_Level = 'True' AND Is_Analyst = 'True'
GROUP BY Company_Type
ORDER BY applicants_per_opening;

-- Q4: What is the entry level salary?
SELECT COUNT(*) AS jobs,
       ROUND(MIN(Salary_LPA), 1) AS lowest,
       ROUND(AVG(Salary_LPA), 1) AS average,
       ROUND(MAX(Salary_LPA), 1) AS highest
FROM jobs_clean
WHERE Is_Entry_Level = 'True' AND Is_Analyst = 'True';
