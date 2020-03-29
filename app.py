import streamlit as st
import numpy as np
import pandas as pd

# Page Title
st.title("Bleeding Cost of Meetings")

# Data source
SALARY_COLUMN = 'ANNUAL_SALARY'
data_url = st.text_input("Salary Data URL:", "https://bloodymeetings.s3-us-west-1.amazonaws.com/us_annual_salaries.csv")

@st.cache(suppress_st_warning=True, persist=True)
def load_data(url):
    data = pd.read_csv(url)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    return data.set_index(['name'])
data = load_data(data_url)

# Display the raw data
st.subheader('Salaries')
st.write("", data)

# Meeting attendees by role
jobs = st.multiselect("Choose attende job roles:", list(data.index), ["Software Engineer - Junior", "Software Engineer", "Software Engineer - Senior", "Software Engineering Manager"])

# Interactive sidebar options
## Length of meeting
length = st.sidebar.slider("Meeting Length (minutes)", 5, 480, 60, 5)
## Occurances of meeting(s)
occurances = st.sidebar.slider("Repeating Occurances Per Month", 0, 20, 4, 1)
## Working months
working_months = st.sidebar.slider("Working Months", 0, 12, 11, 1)

# Cost sum for selections prior
st.subheader('Cost of a meeting with individuals with the selected names')
combined_annual_cost = 0
for role in jobs:
    salary = int(data.loc[role, "annual_salary"])
    combined_annual_cost = combined_annual_cost + salary
cost = (combined_annual_cost/1920) * (length/60)
cost_rounded = round(cost, 2)
st.write('Single meeting cost:', cost_rounded)
repeating_cost = cost * (occurances * working_months)
repeating_cost_rounded = round(repeating_cost, 2)
st.write('Annual Cost:', repeating_cost_rounded)

