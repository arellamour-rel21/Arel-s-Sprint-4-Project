import streamlit as st
import pandas as pd
import plotly.express as px

vehicles_df = pd.read_csv('vehicles_us.csv')
st.header('Car Sales Advertisements')
fig_hist = px.histogram(vehicles_df, x='model_year', title='Distribution of Model Year')
st.plotly_chart(fig_hist)
price_vs_year_fig = px.scatter(vehicles_df, x='model_year', y='price', title='Average Price by Model Year')
st.plotly_chart(price_vs_year_fig)
show_histogram = st.checkbox('Show Histogram of Model Year')
if show_histogram:
    st.plotly_chart(fig_hist)
    
    