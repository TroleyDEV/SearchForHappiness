import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_csv("happy.csv")

# Get Columns names
options = df.columns

# Replace _ for white space and use .title()
options = [col.replace("_", " ").title() for col in options]

# Frontend

st.title("In Search for Happiness")

option1 = st.selectbox(label="Select the data for the X-axis", options=options)
option2 = st.selectbox(label="Select the data for the Y-axis", options=options)

st.title(f"{option1} and {option2}")

# Frontend end

# Go back to default value for dynamic plotting
option1 = str(option1.replace(" ", "_").lower())
option2 = str(option2.replace(" ", "_").lower())

if option1 != option2:
    # Plotly figure
    figure = px.scatter(x=df[option1], y=df[option2])

    # Draw a chart
    st.plotly_chart(figure)
else:
    st.error("You cant plot data with the same values")
