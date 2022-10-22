import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

@st.cache
def read_data():
    return pd.read_csv("output.csv")

st.title("http request status codes")

df = read_data()
statusCodeCounts = dict(df["status"].value_counts())
statusCodes = list(map(str, list(statusCodeCounts.keys())))
statusCounts = list(statusCodeCounts.values())

patches, texts = plt.pie(statusCounts)
plt.legend(patches, statusCodes, loc="best")
plt.axis('equal')
plt.tight_layout()

st.pyplot(plt)
