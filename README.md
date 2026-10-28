# Job Market Analyzer for India

A project that looks at data and business analyst job postings in India, to find out what a fresher needs to get hired.

## Questions I wanted to answer
1. Which skills are most wanted for entry level analysts?
2. Which cities hire the most analysts?
3. Do startups or big companies hire more entry level analysts?
4. What is the entry level salary?

## What I found
1. **Skills:** Power BI, SQL, and Excel come first, then Python.
2. **Cities:** Pune, Delhi, Mumbai, Hyderabad, and Chennai (remote jobs not counted).
3. **Company type:** MNCs post the most entry level analyst jobs. Startups have slightly less competition per opening. Indian unicorns pay the most.
4. **Salary:** about 7 to 8 LPA on average, with a wide range (1.1 to 16.5 LPA).

## Tools used
Python (pandas), MySQL, GitHub

## Data
`india_job_market_2024_2026.csv` has 5,000 job postings. The data looks very clean, so it may be partly synthetic. About 230 postings are entry level analyst jobs, so results are for this dataset only.

## Project steps
1. Cleaned the data in Python (`notebooks`)
2. Loaded it into MySQL and split skills into one skill per row (`sql/schema.sql`)
3. Answered the 4 questions with SQL queries (`sql/analysis.sql`)

## Coming next
Machine learning model, AWS setup, and a dashboard
