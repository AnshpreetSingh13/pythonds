import streamlit as st
import pandas as pd
import plotly.express as px
st.header("Layoff and Hiring Analytics")
df=pd.read_csv("techlayoffs.csv")
st.dataframe(df)
c1,c2,c3,c4,c5=st.columns(5)

# Layoff Percentage
df["Layoff Category"] = pd.cut(
    df["layoff_percentage"],
    bins=[0,10,30,100],
    labels=["Low","Medium","High"],
    include_lowest=True,
)

# Open Roles
df["Hiring Category"] = pd.cut(
    df["open_roles"],
    bins=[0,100,300,1000],
    labels=["Low Hiring","Moderate Hiring","High Hiring"]
)

# Revenue Growth
df["Revenue Category"] = pd.cut(
    df["revenue_growth_percent"],
    bins=[-100,0,20,100],
    labels=["Negative","Stable","High Growth"]
)

with c1: 
    st.metric("Total Layoffs",df["layoffs_count"].sum())
with c2:
    st.metric("Average Layoffs Percentage",df["layoff_percentage"].mean())
with c3:
    st.metric("Highest Layoffs",df["layoffs_count"].max())
with c4:
    st.metric("Average Open Roles",df["open_roles"].mean())
c5,c6=st.columns(2)
with c5:
    st.metric("Hiring Growth Index",df["hiring_trend"].nunique())


fig1 = px.bar(
    df,
    x="Layoff Category",
    color="Layoff Category",
    title="Companies by Layoff Category"
)

st.plotly_chart(fig1, use_container_width=True)

# layoffs_distributin=df.groupby("layoff_percentage").value_counts()
fig2= px.imshow(df.corr(numeric_only= True))
st.plotly_chart(fig2)
industry_distributin=df.groupby("industry")["layoff_percentage"].value_counts()
fig3 = px.box(data_frame= df , x = "industry" , y = "layoff_percentage" , color= "industry")
st.plotly_chart(fig3)
# company_distributin=df.groupby("company_size")["layoff_percentage"].value_counts()
# fig4=px.violin(data_frame=df,x="company_size", y="layoff_percentage",color="company_size")
# st.plotly_chart(fig4)
# country_distributin=df.groupby("country")["layoff_percentage"].sum().reset_index()
fig5 = px.sunburst(
    df,
    path=["company_size","Layoff Category"],
    title="Company Size and Layoff Category"
)

st.plotly_chart(fig5, use_container_width=True)


fig6 = px.bar(
    df,
    x="Hiring Category",
    color="Hiring Category",
    title="Companies by Hiring Category"
)

st.plotly_chart(fig6, use_container_width=True)


reason = (
    df.groupby("reason_for_layoffs")["layoffs_count"]
      .sum()
      .reset_index()
      .sort_values("layoffs_count", ascending=False)
)

fig7 = px.bar(
    reason,
    x="reason_for_layoffs",
    y="layoffs_count",
    color="layoffs_count",
    title="Total Layoffs by Reason"
)

st.plotly_chart(fig7, use_container_width=True)

# open_distributin=df.groupby("layoffs_count")["open_roles"].value_counts()
# fig6=px.histogram(data_frame=df,x="layoffs_count",y="open_roles",nbins=10)
# st.plotly_chart(fig6)
# country_distributin=df.groupby("reason_for_layoffs").sum().reset_index().nlargest(5,["layoffs_count"])
# fig7=px.histogram(data_frame=df,x="reason_for_layoffs",color="reason_for_layoffs")
# st.plotly_chart(fig7)

hiring_trend = (
    df.groupby("hiring_trend")["open_roles"]
      .sum()
      .reset_index()
)

fig8 = px.bar(
    hiring_trend,
    x="hiring_trend",
    y="open_roles",
    color="hiring_trend",
    text="open_roles",
    title="Open Roles by Hiring Trend"
)

fig8.update_traces(textposition="outside")

# hiring_distributin=df.groupby("hiring_trend")["open_roles"].value_counts()
# fig8=px.bar(data_frame=df,x="hiring_trend",y="open_roles",color="hiring_trend")
# st.plotly_chart(fig8)
# with st.sidebar:
#     st.multiselect("select country",df["country"].unique())
#     st.selectbox("select industry",df["industry"].unique())
#     st.radio("select company size",df["company_size"].unique())


