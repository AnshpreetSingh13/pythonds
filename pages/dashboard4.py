import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import plotly.graph_objects as go
st.header("Business Performance and Employee Insights")
df=pd.read_csv("techlayoffs.csv")
st.dataframe(df)
import streamlit as st


# Revenue Growth
df["Revenue Category"] = pd.cut(
df["revenue_growth_percent"],
bins=[-100,0,20,100],
labels=["Loss","Stable","Growth"]
)

df["AI Adoption Category"] = pd.cut(
    df["ai_adoption_level"],
    bins=3,
    labels=["Low","Medium","High"]
)
import streamlit as st

def app():
    st.title("ℹ About Project")

#stock growth 
df["Stock growth percent"] = pd.cut(
df["stock_growth_percent"],
bins=[-100,0,20,100],
labels=["Loss","Stable","Growth"]
)
#job security score
df["Job Security Category"] = pd.cut(
    df["job_security_score"],
    bins=3,
    labels=["Poor","Average","Good"]
)
df["Salary Budeget Category"] = pd.cut(
    df["salary_budget_change"],
    bins=3,
    labels=["Negative","Neutral","Positive"]
)
df["Remote Work Category"] = pd.cut(
    df["remote_jobs_percentage"],
    bins=3,
    labels=["Low","Hybrid","Remote"]
)

    




c1,c2,c3,c4,c5=st.columns(5)

with c1: 
    st.metric("Average renvenue growth ",df["revenue_growth_percent"].mean())
with c2:
    st.metric("Average stock growth",df["stock_growth_percent"].mean())
with c3:
    st.metric("Average Salary Budget Change",df["salary_budget_change"].mean())
with c4:
    st.metric("Average Employee Sentiment",df["employee_sentiment"].mean())
c5,c6=st.columns(2)
with c5:
    st.metric("Average job security score",df["job_security_score"].mean())
with c6:
    st.metric("Average Remote Jobs",df["remote_jobs_percentage"].mean())

c7,c8=st.columns(2)
with c7:
    ai_distributin=df.groupby("Revenue Category").value_counts().reset_index()
    # st.write(ai_distributin)
    fig1 = px.bar(
            df,
            x="Revenue Category",
            
            color="Revenue Category",
            title="Revenue growth percent"
        )
    st.plotly_chart(fig1, use_container_width=True)
with c8:
  replace_distributin=df.groupby("Stock growth percent")["record_id"].count().reset_index()

  fig2 = px.treemap(
                replace_distributin,
                path=["Stock growth percent"],
                values="record_id",
                title="Stock growth percent",
                width=300,
                height=600
                
            )
  st.plotly_chart(fig2, use_container_width=True)
industry_distributin=df.groupby("Job Security Category")["record_id"].count().reset_index()
# st.dataframe(industry_distributin)
fig3 = px.pie(
    industry_distributin,
    names="Job Security Category",
    hole=0.5,
    title="Job Security Category"
)
st.plotly_chart(fig3, use_container_width=True)

temp = df.groupby("Revenue Category")["stock_growth_percent"].sum().reset_index()
fig4 = px.line(
    temp,
    x="Revenue Category",
    y="stock_growth_percent",

    
)
st.plotly_chart(fig4, use_container_width=True)

country_distributin=df.groupby("Revenue Category")["layoffs_count"].sum().reset_index()
# st.write(country_distributin)
fig5 = px.area(
    country_distributin,
    x='Revenue Category',
    y='layoffs_count',
    # color="ai_adoption_level",

    # trendline="ols"
)
st.plotly_chart(fig5, use_container_width=True)
open_distributin=df.groupby("AI Adoption Category")["employee_sentiment"].value_counts().reset_index()
st.dataframe(open_distributin)
fig6 = px.pie(
    df,
    names="AI Adoption Category",
    values ="employee_sentiment",
    color="ai_adoption_level"
)
st.plotly_chart(fig6, use_container_width=True)

temp = df.groupby("Salary Budeget Category")["employee_sentiment"].sum().reset_index()

fig7 = px.area(
    temp,
    x="Salary Budeget Category",
    y="employee_sentiment",
    # color="Salary Budeget Category",
    title="Salary Budeget Category Vs employee_sentiment"


)
st.plotly_chart(fig7,use_container_width=True)
temp1 = df.groupby("Remote Work Category")["employee_sentiment"].sum().reset_index()

fig8 = px.histogram(
    temp1,
    x="Remote Work Category",
    y="employee_sentiment",
    color="Remote Work Category"

)
st.plotly_chart(fig8,use_container_width=True)
temp2 = df.groupby("market_condition")["revenue_growth_percent"].sum().reset_index()
fig9 = px.bar(
    temp2,
    x="market_condition",
    y="revenue_growth_percent",
    color="market_condition"

)
st.plotly_chart(fig9,use_container_width=True)
temp3 = df.groupby("hiring_trend")["employee_sentiment"].sum().reset_index()
fig10 = px.area(
    temp3,
    x="hiring_trend",
    y="employee_sentiment",
    color="hiring_trend"

)
st.plotly_chart(fig10,use_container_width=True)
temp4 = df.groupby("country")["salary_budget_change"].sum().reset_index()
fig10 = px.histogram(
    temp4,
    x="country",
    y="salary_budget_change",
    color="country"

)
st.plotly_chart(fig10,use_container_width=True)
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




