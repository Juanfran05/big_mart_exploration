import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Streamlit App")

st.header("Data Visualization")
st.subheader("Import Data")
st.text("Import Big Mart Data")

df = pd.read_csv("Test_BigMart.csv")

show_df = st.checkbox("Show DataFrame")
if show_df:
    st.dataframe(df)

st.subheader("Data Visualization")
# bar char from outlet type
st.text("Bar Chart from Outlet Type")
fig = px.bar(df["Outlet_Type"].value_counts())
fig.update_layout(title="Outlet Type",
        xaxis_title="Outlet Type",
        yaxis_title="Count")
st.plotly_chart(fig)

st.text("Scatter plot item visibility vs item mrp")
fig = px.scatter(df, x="Item_Visibility", y="Item_MRP",
        color="Outlet_Type")
fig.update_layout(title="Item Visibility vs Item MRP",
        xaxis_title="Item Visibility",
        yaxis_title="Item MRP")
st.plotly_chart(fig)
