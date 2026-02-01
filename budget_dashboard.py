import streamlit as st
import pandas as pd
import plotly.express as px
from io import StringIO  # ← NEW LINE

st.set_page_config(layout="wide")
st.title("💰 Budget Tracker Dashboard")

@st.cache_data
def load_data():
    data = """Date,Amount,Description
2025-11-15,45.50,Amazon ESP32 kit
2025-11-16,12.30,McDonalds lunch"""
    return pd.read_csv(StringIO(data), parse_dates=['Date'])  # ← FIXED

df = load_data()
df['Category'] = df['Description'].str.lower().apply(
    lambda x: 'Food' if 'food' in x.lower() else 'Electronics' if 'amazon' in x.lower() else 'Other')

col1, col2 = st.columns([2,1])
with col1:
    st.subheader("📊 Transactions")
    st.dataframe(df)
with col2:
    st.metric("Total Spent", f"₹{df['Amount'].sum():.0f}")

fig = px.pie(df, names='Category', values='Amount')
st.plotly_chart(fig)
