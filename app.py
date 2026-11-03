import streamlit as st
import pandas as pd
import altair as alt
import joblib

st.set_page_config(page_title="Job Market Analyzer", page_icon="📊", layout="wide")

# ---------- Style ----------
st.markdown("""
<style>
.block-container {padding-top: 2rem; max-width: 1100px;}
[data-testid="stMetric"] {
    background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 12px;
    padding: 16px 18px; box-shadow: 0 1px 3px rgba(15, 23, 42, 0.06);
}
[data-testid="stMetricLabel"] {color: #64748B;}
[data-testid="stMetricValue"] {color: #0F766E; font-size: 1.8rem;}
h1 {color: #0F172A;}
h3 {color: #0F766E; margin-top: 1.5rem;}
</style>
""", unsafe_allow_html=True)

TEAL = "#0F766E"
@st.cache_resource
def load_model():
    model = joblib.load("model/salary_model.pkl")
    columns = joblib.load("model/model_columns.pkl")
    return model, columns

model, model_columns = load_model()

def sorted_bar(series, horizontal=False, color=TEAL):
    data = series.reset_index()
    data.columns = ["name", "value"]
    if horizontal:
        base = alt.Chart(data).encode(
            y=alt.Y("name:N", sort="-x", title=None, axis=alt.Axis(labelLimit=250)),
            x=alt.X("value:Q", title=None, axis=None),
        )
        bars = base.mark_bar(color=color, cornerRadiusEnd=4)
        labels = base.mark_text(align="left", dx=4, color="#334155").encode(text="value:Q")
    else:
        base = alt.Chart(data).encode(
            x=alt.X("name:N", sort="-y", title=None, axis=alt.Axis(labelAngle=0)),
            y=alt.Y("value:Q", title=None, axis=None),
        )
        bars = base.mark_bar(color=color, cornerRadiusTopLeft=4, cornerRadiusTopRight=4)
        labels = base.mark_text(dy=-8, color="#334155").encode(text="value:Q")
    return (bars + labels).properties(height=300)

# ---------- Data ----------
jobs = pd.read_csv("data/clean/jobs_clean.csv")
skills = pd.read_csv("data/clean/job_skills.csv")
df = jobs[jobs["Is_Entry_Level"] & jobs["Is_Analyst"]]

top_skills = skills[skills["Job_ID"].isin(df["Job_ID"])]["Skill"].value_counts().head(10)
cities = df[df["City"] != "Remote"]["City"].value_counts().head(5)
type_jobs = df["Company_Type"].value_counts()
type_salary = df.groupby("Company_Type")["Salary_LPA"].mean().round(1).sort_values(ascending=False)

# ---------- Header ----------
st.title("📊 Job Market Analyzer")
st.caption("What does a fresher need to get hired as an analyst in India?")

# ---------- KPIs ----------
a, b, c, d = st.columns(4)
a.metric("Entry level analyst jobs", len(df))
b.metric("Average salary (LPA)", round(df["Salary_LPA"].mean(), 1))
c.metric("Median salary (LPA)", round(df["Salary_LPA"].median(), 1))
d.metric("Highest salary (LPA)", df["Salary_LPA"].max())

e, f, g, h = st.columns(4)
e.metric("Top skill", top_skills.index[0])
f.metric("Top hiring city", cities.index[0])
g.metric("Most jobs from", type_jobs.index[0])
h.metric("Best paying", type_salary.index[0])

st.divider()

# ---------- Q1 ----------
st.subheader("Q1: Which skills are most wanted?")
st.altair_chart(sorted_bar(top_skills, horizontal=True), use_container_width=True)
st.info(f"**{top_skills.index[0]}**, **{top_skills.index[1]}** and **{top_skills.index[2]}** "
        f"come first. Learn these before anything else.")

# ---------- Q2 ----------
st.subheader("Q2: Which cities hire the most?")
st.altair_chart(sorted_bar(cities), use_container_width=True)
st.info(f"**{cities.index[0]}** leads, followed by **{cities.index[1]}** and **{cities.index[2]}**. "
        f"Remote jobs are not counted here.")

# ---------- Q3 ----------
st.subheader("Q3: Startups or big companies?")
left, right = st.columns(2)
left.markdown("**Number of jobs**")
left.altair_chart(sorted_bar(type_jobs), use_container_width=True)
right.markdown("**Average salary (LPA)**")
right.altair_chart(sorted_bar(type_salary, color="#F59E0B"), use_container_width=True)
st.info(f"**{type_jobs.index[0]}** companies post the most jobs. "
        f"**{type_salary.index[0]}** companies pay the most.")

# ---------- Salary predictor ----------
st.subheader("Try it yourself: salary predictor")
st.write("Pick a job below and the model will guess the salary.")

levels = ["Fresher (0-1 yr)", "Junior (1-3 yrs)", "Mid (3-6 yrs)", "Senior (6-10 yrs)", "Lead (10+ yrs)"]
titles = sorted(jobs["Job_Title"].unique())

c1, c2, c3 = st.columns(3)
exp = c1.selectbox("Experience level", levels)
company = c2.selectbox("Company type", sorted(jobs["Company_Type"].unique()))
city = c3.selectbox("City", sorted(jobs["City"].unique()))

c4, c5, c6 = st.columns(3)
title = c4.selectbox("Job title", titles, index=titles.index("Data Analyst") if "Data Analyst" in titles else 0)
mode = c5.selectbox("Work mode", sorted(jobs["Work_Mode"].unique()))
industry = c6.selectbox("Industry", sorted(jobs["Industry"].unique()))

picked = st.multiselect("Skills the job asks for", ["SQL", "Python", "Power BI", "Excel", "Tableau"], default=["SQL"])

if st.button("Predict salary"):
    row = pd.DataFrame(0, index=[0], columns=model_columns)
    for name in [f"Experience_Level_{exp}", f"Company_Type_{company}", f"City_{city}",
                 f"Job_Title_{title}", f"Work_Mode_{mode}", f"Industry_{industry}"]:
        if name in row.columns:
            row[name] = 1
    for s in picked:
        row[f"Has_{s}"] = 1
    guess = model.predict(row)[0]
    st.success(f"Estimated salary: **{guess:.1f} LPA**")
    margin = 2.0 if exp.startswith(("Fresher", "Junior")) else 5.2
    st.caption(f"The model is usually off by about {margin} LPA for jobs like this. "
               f"It learned from a dataset that may be partly synthetic, so treat this as a rough guide.")

# ---------- Footer ----------
st.divider()
st.caption("Data: 5,000 job postings from 2024 to 2026, of which 230 are entry level analyst roles. "
           "The data may be partly synthetic, so results show the method more than real market numbers.")
