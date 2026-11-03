# Job Market Analyzer for India

## About
Many freshers apply to analyst jobs without knowing which skills companies really want. I built this project to answer that with data instead of guesses. I took job postings from 2024 to 2026, cleaned them, stored them in a database, and used SQL to answer four clear questions about the entry-level analyst market. I then built an interactive dashboard so anyone can explore the results.

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
Python (pandas), MySQL, Streamlit, GitHub, VS Code

## Data
`india_job_market_2024_2026.csv` has 5,000 job postings. The data looks very clean, so it may be partly synthetic. About 230 postings are entry level analyst jobs, so results are for this dataset only.

## Project Structure
- /data: job postings datasets
- /notebooks: data cleaning in Python
- /sql: schema and queries answering 4 questions
- /dashboard: Streamlit dashboard files

## Checking the results on real data
I compared my skills result with about 2,000 entry level analyst postings from Naukri.
SQL ranked high in both datasets, so it is the most reliable skill finding.
Power BI and Excel ranked higher in the main dataset than on Naukri, so those results are less certain.

## Dashboard Preview
<img width="968" height="600" alt="2026-11-03T12-18_chart" src="https://github.com/user-attachments/assets/eda0667a-cb3a-414b-af41-75ed4ae74e67" />
<img width="968" height="600" alt="2026-11-03T12-18_chart (1)" src="https://github.com/user-attachments/assets/e8dd2007-bb90-44e7-95db-8dfcb8747f30" />
<img width="968" height="600" alt="2026-11-03T12-18_chart (2)" src="https://github.com/user-attachments/assets/e0c3a3ad-d1bd-4b0b-965b-10c66e4ded56" />



