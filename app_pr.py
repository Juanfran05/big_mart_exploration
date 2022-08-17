import streamlit as st
import pandas as pd
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report

st.title("Pandas Profiling")

df = pd.read_csv("Test_BigMart.csv")
pr = df.profile_report(title="Big Mart Data Analysis")
st_profile_report(pr)
