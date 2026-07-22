import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu

st.title("Project on Techlayoffs")
st.header("Executive Workforce Overview")
df=pd.read_csv("techlayoffs.csv")
# st.dataframe(df)

c1, c2, c3, c4 = st.columns(4)
with c1: 
    st.metric("Total Companies", f"{df['company_name'].nunique():,}")
with c2:
    st.metric("Total Layoffs", f"{int(df['layoffs_count'].sum()):,}")
with c3:
    st.metric("Total Open Roles", f"{int(df['open_roles'].sum()):,}")
with c4:
    st.metric("Average AI Adoption Level", f"{df['ai_adoption_level'].mean():.2f}")

c5, c6, c7, c8 = st.columns(4)
with c5:
    st.metric("Average Revenue Growth", f"{df['revenue_growth_percent'].mean():.2f}%")
with c6:
    st.metric("Average Stock Growth", f"{df['stock_growth_percent'].mean():.2f}%")
with c7:
    st.metric("Average Employee Sentiment", f"{df['employee_sentiment'].mean():.2f}")
with c8:
    st.metric("Average Job Security Score", f"{df['job_security_score'].mean():.2f}")
df["AI Adoption Category"] = pd.cut(
    df["ai_adoption_level"],
    bins=[0,30,70,100],
    labels=["Low","Medium","High"]
)

df["AI Risk Category"] = pd.cut(
    df["ai_replacement_risk"],
    bins=[0,30,70,100],
    labels=["Low","Medium","High"]
)

df["Job Security Category"] = pd.cut(
    df["job_security_score"],
    bins=[0,30,70,100],
    labels=["Poor","Average","Good"]
)

df["Employee Sentiment Category"] = pd.cut(
    df["employee_sentiment"],
    bins=[0,30,70,100],
    labels=["Negative","Neutral","Positive"]
)

df["Revenue Category"] = pd.cut(
    df["revenue_growth_percent"],
    bins=[-100,0,20,100],
    labels=["Loss","Stable","Growth"]
)

df["Layoff Category"] = pd.cut(
    df["layoff_percentage"],
    bins=[0,10,30,100],
    labels=["Low","Medium","High"]
)

df["Remote Work Category"] = pd.cut(
    df["remote_jobs_percentage"],
    bins=[0,30,70,100],
    labels=["Low","Hybrid","Remote"]
)

industry = (
    df.groupby("industry")["layoffs_count"]
      .sum()
      .reset_index()
)

fig1 = px.bar(
    industry,
    x="industry",
    y="layoffs_count",
    color="industry",
    title="Layoff count by industry",
)
st.plotly_chart(fig1, use_container_width=True)
# country_distributin=df.groupby("country").value_counts()
country = (
    df.groupby("country")["layoffs_count"]
      .mean()
      .reset_index()
      .nlargest(10 , "layoffs_count")
)
# map
fig2 = px.treemap(
    country,
    path=["country"],
    values="layoffs_count",
    title="Layoff count by country"

)
st.plotly_chart(fig2, use_container_width=True)
company_distribution = (
    df.groupby("company_size")
      .size()
      .reset_index(name="Count")
)
fig3=px.pie(data_frame=df,names="company_size",hole=0.5,title="Company size distribution")
st.plotly_chart(fig3, use_container_width=True)
Hiring_distributin=df.groupby("hiring_trend")["open_roles"].sum().reset_index()
fig4=px.bar(data_frame=Hiring_distributin,x="hiring_trend",y = "open_roles")
st.plotly_chart(fig4, use_container_width=True)
market = (
    df["market_condition"]
      .value_counts()
      .reset_index()
)

market.columns = ["market_condition", "Count"]

fig5 = px.pie(
    market,
    names="market_condition",
    values="Count",
    hole=0.5
)
fig5=px.pie(data_frame=df,names="market_condition",values="job_security_score")
st.plotly_chart(fig5, use_container_width=True)
industry_distributin = (
    df.groupby("industry")["layoffs_count"]
      .sum()
      .sort_values(ascending=True)
      .reset_index()
)

fig6 = px.bar(
    industry_distributin,
    x="layoffs_count",
    y="industry",
    orientation="h",
    color="layoffs_count",
    text="layoffs_count",
    title="Total Layoffs by Industry"
)

fig6.update_traces(textposition="outside")

st.plotly_chart(fig6, use_container_width=True)
country_distributin = (
    df.groupby("country")["open_roles"]
      .sum()
      .reset_index()
)

fig7 = px.treemap(
    country_distributin,
    path=["country"],
    values="open_roles",
    color="open_roles",
    title="Open Roles by Country"
)

st.plotly_chart(fig7, use_container_width=True)
with st.sidebar:
    st.multiselect("select country",df["country"].unique())
    st.selectbox("select industry",df["industry"].unique())
    st.radio("select company size",df["company_size"].unique())
    st.multiselect("select year",df["year"].unique())
    st.selectbox("select month",df["month"].unique())
    st.radio("select market condition",df["market_condition"].unique())
