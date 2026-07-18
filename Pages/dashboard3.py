import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import plotly.graph_objects as go
st.header("AI Transformation and Workforce Impact")
df=pd.read_csv("techlayoffs.csv")
st.dataframe(df)
# with st.sidebar:
#     st.multiselect("select country",df["country"].unique())
#     industry = st.multiselect("select industry",df["industry"].unique())
#     st.radio("select company size",df["company_size"].unique())

# if industry:
#     df = df[df["industry"].isin(industry)]
import streamlit as st


df["AI Adoption Category"] = pd.cut(
    df["ai_adoption_level"],
    bins=3,
    labels=["Low","Medium","High"]
)

c1,c2,c3,c4,c5=st.columns(5)
with c1: 
    st.metric("Average Ai adoption level",df["ai_adoption_level"].mean())
with c2:
    st.metric("Average Ai replacement risk",df["ai_replacement_risk"].mean())
with c3:
    st.metric("Average automation impact",df["ai_automation_impact"].mean())
with c4:
    st.metric("Average remote work",df["remote_jobs_percentage"].mean())
c5,c6=st.columns(2)
with c5:
    st.metric("Average job security score",df["job_security_score"].mean())

df["AI Risk Category"] = pd.cut(
    df["ai_replacement_risk"],
    bins=3,
    labels=["Low","Medium","High"]
)
df["AI automation impact"] = pd.cut(
    df["ai_automation_impact"],
    bins=3,
    labels=["Low","Medium","High"]
)




ai_distributin=df.groupby("AI Adoption Category").value_counts().reset_index()
fig1 = px.bar(
    ai_distributin,
    x="AI Adoption Category",
    y="count",
    color="AI Adoption Category",
    title="AI Adoption Level Distribution"
)


st.plotly_chart(fig1, use_container_width=True)

replace_distributin=df.groupby("AI Risk Category").value_counts().reset_index()

fig2 = px.treemap(
    replace_distributin,
    path=["AI Risk Category"],
    values="count",
    color="AI Risk Category",
    title="AI Replacement Risk"
)
st.plotly_chart(fig2, use_container_width=True)

industry_distributin=df.groupby("AI automation impact").value_counts().reset_index()
fig3 = px.histogram(
    industry_distributin,
    x="AI automation impact",
    y="count",
    color="AI automation impact",
    title="AI automation Impact"
)
st.plotly_chart(fig3, use_container_width=True)

temp = df.groupby("AI Adoption Category")["layoffs_count"].sum().reset_index()

fig4 = px.density_heatmap(
    temp,
    x="AI Adoption Category",
    y="layoffs_count"
)
st.plotly_chart(fig4, use_container_width=True)

country_distributin=df.groupby("AI Adoption Category")["open_roles"].sum().reset_index()
# st.write(country_distributin)
fig5 = px.bar(
    country_distributin,
    x='AI Adoption Category',
    y='open_roles',
    color="AI Adoption Category",

)
st.plotly_chart(fig5, use_container_width=True)
open_distributin=df.groupby("AI Adoption Category")["employee_sentiment"].sum().reset_index()
fig6 = px.area(
    open_distributin,
    x="AI Adoption Category",
    y="employee_sentiment",
    color="AI Adoption Category"
)
st.plotly_chart(fig6, use_container_width=True)

temp = df.groupby(["industry","ai_adoption_level"]).size().reset_index(name="count")

fig7 = px.treemap(
    temp,
    path=["industry","ai_adoption_level"],
    values="count"
)
st.plotly_chart(fig7,use_container_width=True)
temp = df.groupby(["company_size","ai_adoption_level"]).size().reset_index(name="count")

fig8 = px.bar(
    temp,
    x="company_size",
    y="count",
    color="company_size",
    barmode="stack"
)
st.plotly_chart(fig8,use_container_width=True)
numeric_df = df.select_dtypes(include="number")
corr = numeric_df.corr()
fig = px.imshow(
    corr,
    text_auto=".1f",
    color_continuous_scale="RdBu_r",
    width=1200,      
    height=900  
)

st.plotly_chart(fig, use_container_width=True)
# with st.sidebar:
#     st.multiselect("select country",df["country"].unique())
#     st.selectbox("select industry",df["industry"].unique())
#     st.radio("select company size",df["company_size"].unique())




