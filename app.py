import streamlit as st
import pandas as pd
import plotly.express as px

vehicles_df = pd.read_csv('vehicles_us.csv')
st.header('Car Sales Advertisements')
fig_one = px.histogram(vehicles_df, x='model_year', title='Distribution of Model Year')
st.plotly_chart(fig_one)
price_vs_year_fig = px.scatter(vehicles_df, x='model_year', y='price', title='Average Price by Model Year')
st.plotly_chart(price_vs_year_fig)
price_grp = vehicles_df.groupby('model_year')['price'].mean().reset_index()
price_fig = px.scatter(price_grp, x='model_year', y='price', title='Average Price by Model Year')
show_histogram = st.checkbox('Show Histogram of Model Year')
if show_histogram:
    st.plotly_chart(price_fig)