import streamlit as st
import numpy as np
import pandas as pd

st.title("Cost of Meetings")

SALARY_COLUMN = 'ANNUAL_SALARY'
DATA_URL = ('annual_salaries.csv')

def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    # data.set_index("name")
    return data.set_index(['name'])

data = load_data(20)

st.subheader('Salaries')
st.write("", data)

jobs = st.multiselect("Choose job roles of individuals attending meeting", list(data.index), [])


st.subheader('Cost of a meeting with individuals with these job roles')
length = st.sidebar.slider("Meeting Length in minutes", 1, 480, 60, 1)
combined_annual_cost = 0
for role in jobs:
    salary = int(data.loc[role, "annual_salary"])
    combined_annual_cost = combined_annual_cost + salary

cost = (combined_annual_cost/1920) * (length/60)
cost_rounded = round(cost, 2)
st.write('This meeting cost:', cost_rounded)

