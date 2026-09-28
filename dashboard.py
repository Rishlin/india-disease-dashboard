import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="India Disease Dashboard", layout="wide")
st.title("🏥 India Disease Trends Dashboard")
st.markdown("Public health data across Indian states")

# Dataset
data = {
    "State": ["Maharashtra","Tamil Nadu","Kerala","UP","Karnataka",
              "Maharashtra","Tamil Nadu","Kerala","UP","Karnataka",
              "Maharashtra","Tamil Nadu","Kerala","UP","Karnataka"],
    "Disease": ["Dengue","Dengue","Dengue","Dengue","Dengue",
                "Malaria","Malaria","Malaria","Malaria","Malaria",
                "Tuberculosis","Tuberculosis","Tuberculosis","Tuberculosis","Tuberculosis"],
    "Year": [2022,2022,2022,2022,2022,
             2022,2022,2022,2022,2022,
             2022,2022,2022,2022,2022],
    "Cases": [12000,9500,7800,15000,8200,
              5000,3200,1800,22000,4100,
              45000,38000,12000,95000,31000]
}

df = pd.DataFrame(data)

# Filters
disease = st.selectbox("Select Disease", df["Disease"].unique())
filtered = df[df["Disease"] == disease]

# Charts
col1, col2 = st.columns(2)

with col1:
    st.subheader("Cases by State")
    fig1 = px.bar(filtered, x="State", y="Cases", color="State")
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.subheader("Share of Cases")
    fig2 = px.pie(filtered, names="State", values="Cases")
    st.plotly_chart(fig2, use_container_width=True)

st.subheader("Data Table")
st.dataframe(filtered)
