import streamlit as st
import numpy as np
import pandas as pd

# TITLE
st.title("Meetings Cost Calculator")
st.markdown('<font color=\"grey\">*This mini application displays the total cost for a given instance of a meeting and optionally, the total annual cost for regularly repeating meetings. For more information and how to run your own local copy of this app, see [this Github repo](https://github.com/jalakoo/bloodymeetings).*</font>', unsafe_allow_html=True)
st.markdown('<br>', unsafe_allow_html=True)


# SIDEBAR
# ============================================
st.sidebar.markdown("**Currency Symbol**:", unsafe_allow_html=True)
currency_symbol = st.sidebar.text_input('', '$')

## Length of meeting
st.sidebar.markdown("**Meeting length (minutes)**:", unsafe_allow_html=True)
length = st.sidebar.slider("", 15, 480, 60, 15)

## Occurences of meeting(s)
st.sidebar.markdown("**Occurences Per Month**:<br>*Set to 0 for a one-off meeting*", unsafe_allow_html=True)
occurences = st.sidebar.slider("", 0, 20, 4, 1)

## Working months
st.sidebar.markdown("**Working Months**:<br>*Adjust for seasonal, or project based options. Default is 11 to account for holidays, time-off, and other events.*", unsafe_allow_html=True)
working_months = st.sidebar.slider("", 1, 12, 11, 1)

## Display raw data
display_salary_data = st.sidebar.checkbox('Show Salary Data')


# MAIN BODY
# ============================================
# DATA SOURCE
SALARY_COLUMN = 'ANNUAL_SALARY'
st.markdown('**Salary Data Source URL**:<br>*Can use any static location for a .csv file with the following header columns: **name, annual_salary** *', unsafe_allow_html=True)
data_url = st.text_input("", "https://bloodymeetings.s3-us-west-1.amazonaws.com/us_annual_salaries.csv")

@st.cache(suppress_st_warning=True, persist=True)
def load_data(url):
    data = pd.read_csv(url)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    return data
    # return data.set_index(['name'])
raw_data = load_data(data_url)
data = raw_data.set_index(['name'])

# SOURCE DATA (optional)
if display_salary_data:
    st.markdown('**Salary Data:**')
    st.write("", raw_data)

# ATTENDEES - Sample provided
st.markdown('<br>', unsafe_allow_html=True)
st.markdown('<br>', unsafe_allow_html=True)
st.markdown('**Meeting Attendees**:<br>*Select from the following dropdown list of job names. These are drawn from the data source\'s **name** column. NOTE: Multiple instances of a name aren\'t supported.*', unsafe_allow_html=True)
jobs = st.multiselect("", list(data.index), ["Software Engineer - Junior", "Software Engineer", "Software Engineer - Senior", "Software Engineering Manager"])

# COST SUMMARY
# ============================================
# st.subheader('Cost of a meeting with individuals with the selected names')
st.markdown('---')
combined_annual_cost = 0
for role in jobs:
    salary = int(data.loc[role, "annual_salary"])
    combined_annual_cost = combined_annual_cost + salary
cost = (combined_annual_cost/1920) * (length/60)
cost_rounded = round(cost, 2)
repeating_cost = cost * (occurences * working_months)
repeating_cost_rounded = round(repeating_cost, 2)
costs = "<pre>Single Meeting Cost: <font color=\'green\'><b>{}{:,}</b></font>   |   Annual Meetings Cost: <font color=\'red\'><b>{}{:,}</b></font></pre>".format(currency_symbol, cost_rounded, currency_symbol, repeating_cost_rounded)
st.markdown(costs, unsafe_allow_html=True)