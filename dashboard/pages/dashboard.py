import streamlit as st

import seaborn as sns
import pandas as pd
import plotly.express as px

st.title("Titanic Dataset analysis")
st.write("this is the analysis of titanic dataset.")

# df = sns.load_dataset("titanic")

df = pd.read_csv("country_wise_latest.csv")

st.dataframe(df)

top_10 = df.nlargest(10, 'Confirmed')
fig = px.bar(top_10, x='Country/Region', y='Confirmed', color='Confirmed',title='top 10 countries with highest confirmed cases', template='plotly_dark')


fig.update_traces(textposition='outside')

st.plotly_chart(fig)

fig = px.pie(df, names="WHO Region", values="Confirmed",
title="Confirmed cases per WHO Region", template='plotly_dark',
color_discrete_sequence=px.colors.sequential.RdBu,height=500, width=800)


st.plotly_chart(fig)

fig = px.scatter(df, x="Confirmed", y='Deaths', color='WHO Region', size='Confirmed',
    title='Confirmed cases vs Deaths', template='plotly_dark', height=600, width=800,
    hover_name='Country/Region')

fig



