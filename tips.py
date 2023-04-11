import yfinance as yf
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib as mpl
import matplotlib.pyplot as plt

st.write("""
# Tips DataFrame
""")
tips = pd.read_csv('../ds-phase-0/learning/datasets/tips.csv')
st.dataframe(tips)
st.dataframe(tips.groupby('day', as_index=False).agg({'total_bill': 'mean'}))
fig, ax = plt.subplots()
ax.hist(tips['total_bill'])
plt.xlabel('Number of orders')
plt.ylabel('$')
st.pyplot(fig)