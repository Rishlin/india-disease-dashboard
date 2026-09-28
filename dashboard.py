import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="India Disease Surveillance Dashboard", layout="wide")

# Header
st.title("🏥 India Disease Surveillance Dashboard")
st.markdown("**Tracking public health trends across Indian states | Inspired by hospital IT workflows**")
st.divider()

# Dataset - expanded with more diseases, states and years
data = {
    "State": [
        # Dengue
        "Maharashtra","Tamil Nadu","Kerala","Uttar Pradesh","Karnataka",
        "Maharashtra","Tamil Nadu","Kerala","Uttar Pradesh","Karnataka",
        "Maharashtra","Tamil Nadu","Kerala","Uttar Pradesh","Karnataka",
        # Malaria
        "Maharashtra","Tamil Nadu","Kerala","Uttar Pradesh","Karnataka",
        "Maharashtra","Tamil Nadu","Kerala","Uttar Pradesh","Karnataka",
        "Maharashtra","Tamil Nadu","Kerala","Uttar Pradesh","Karnataka",
        # Tuberculosis
        "Maharashtra","Tamil Nadu","Kerala","Uttar Pradesh","Karnataka",
        "Maharashtra","Tamil Nadu","Kerala","Uttar Pradesh","Karnataka",
        "Maharashtra","Tamil Nadu","Kerala","Uttar Pradesh","Karnataka",
        # Cholera
        "Maharashtra","Tamil Nadu","Kerala","Uttar Pradesh","Karnataka",
        "Maharashtra","Tamil Nadu","Kerala","Uttar Pradesh","Karnataka",
        "Maharashtra","Tamil Nadu","Kerala","Uttar Pradesh","Karnataka",
    ],
    "Disease": [
        *["Dengue"]*15,
        *["Malaria"]*15,
        *["Tuberculosis"]*15,
        *["Cholera"]*15,
    ],
    "Year": [
        *[2020,2020,2020,2020,2020, 2021,2021,2021,2021,2021, 2022,2022,2022,2022,2022]*4
    ],
    "Cases": [
        # Dengue
        8000,7000,5000,12000,6000,
        10000,8500,6500,13500,7000,
        12000,9500,7800,15000,8200,
        # Malaria
        4000,2500,1500,18000,3200,
        4500,2800,1600,20000,3600,
        5000,3200,1800,22000,4100,
        # Tuberculosis
        38000,30000,10000,80000,25000,
        41000,34000,11000,87000,28000,
        45000,38000,12000,95000,31000,
        # Cholera
        1200,800,300,3500,900,
        1500,950,400,4000,1100,
        1800,1100,500,4800,1300,
    ]
}

df = pd.DataFrame(data)

# Sidebar filters
st.sidebar.header("🔍 Filters")
selected_disease = st.sidebar.selectbox("Select Disease", sorted(df["Disease"].unique()))
selected_year = st.sidebar.selectbox("Select Year", sorted(df["Year"].unique(), reverse=True))

filtered = df[(df["Disease"] == selected_disease) & (df["Year"] == selected_year)]
trend_data = df[df["Disease"] == selected_disease]

# Key metrics row
st.subheader(f"📊 {selected_disease} Overview — {selected_year}")
col1, col2, col3 = st.columns(3)
col1.metric("Total Cases", f"{filtered['Cases'].sum():,}")
col2.metric("Most Affected State", filtered.loc[filtered['Cases'].idxmax(), 'State'])
col3.metric("Least Affected State", filtered.loc[filtered['Cases'].idxmin(), 'State'])

st.divider()

# Charts row 1
col1, col2 = st.columns(2)

with col1:
    st.subheader("Cases by State")
    fig1 = px.bar(filtered, x="State", y="Cases", color="State",
                  color_discrete_sequence=px.colors.qualitative.Set2)
    fig1.update_layout(showlegend=False)
    st.plotly_chart(fig1, width='stretch')

with col2:
    st.subheader("State-wise Share")
    fig2 = px.pie(filtered, names="State", values="Cases",
                  color_discrete_sequence=px.colors.qualitative.Set2)
    st.plotly_chart(fig2, width='stretch')

# Charts row 2 - Year wise trend
st.subheader(f"📈 Year-wise Trend — {selected_disease} across States")
fig3 = px.line(trend_data, x="Year", y="Cases", color="State",
               markers=True,
               color_discrete_sequence=px.colors.qualitative.Set1)
fig3.update_layout(xaxis=dict(tickmode='linear'))
st.plotly_chart(fig3, width='stretch')

# Data table
st.subheader("📋 Raw Data")
st.dataframe(filtered.reset_index(drop=True), use_container_width=True)

# Footer
st.divider()
st.markdown("*Data sourced from public health records | Dashboard built as part of hospital IT internship project*")