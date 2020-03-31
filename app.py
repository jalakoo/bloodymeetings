import streamlit as st
import numpy as np
import pandas as pd

# TITLE
st.title("Meetings Cost Calculator")
st.markdown('<font color=\"grey\">*This app displays the cost of a single meeting and the annual cost of recurring meetings based on attendee salaries. For more information & to run your own local copy, see [this Github repo](https://github.com/jalakoo/bloodymeetings).*</font>', unsafe_allow_html=True)
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
occurrences = st.sidebar.slider("", 0, 20, 4, 1)

## Working months
st.sidebar.markdown("**Working Months**:<br>*Adjust for seasonal, or project based options. Default is 11 to account for holidays, time-off, and other events.*", unsafe_allow_html=True)
working_months = st.sidebar.slider("", 1, 12, 11, 1)

## Display Options
display_data_source = st.sidebar.checkbox('Edit Data Source')
display_salary_data = st.sidebar.checkbox('Show Salary Data')
display_cost_graph = st.sidebar.checkbox('Show Cost Graph')

# MAIN BODY
# ============================================
# DATA SOURCE (optional)
SALARY_COLUMN = 'ANNUAL_SALARY'
data_url = "https://bloodymeetings.s3-us-west-1.amazonaws.com/us_annual_salaries.csv"
if display_data_source:
    st.markdown('**Salary Data Source URL**:<br>*Can use any static location for a .csv file with the following header columns: **name, annual_salary** *', unsafe_allow_html=True)
    data_url = st.text_input("", data_url)

@st.cache(suppress_st_warning=True, persist=True)
def load_data(url):
    data = pd.read_csv(url)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    return data
raw_data = load_data(data_url)
data = raw_data.set_index(['name'])

# SOURCE DATA (optional)
if display_salary_data:
    st.markdown('**Salary Data:**')
    st.write("", raw_data)

# ATTENDEES - Sample provided
st.markdown('**Meeting Attendees**:<br>*Select job names from the following dropdown. Only one of each name is currently supported.*', unsafe_allow_html=True)
jobs = st.multiselect("", list(data.index), ["Software Engineer - Junior", "Software Engineer", "Software Engineer - Senior", "Software Engineering Manager"])

# COST SUMMARY
# ============================================
# Calculate
combined_annual_cost = 0
for role in jobs:
    salary = int(data.loc[role, "annual_salary"])
    combined_annual_cost = combined_annual_cost + salary
cost = (combined_annual_cost/1920) * (length/60)
cost_rounded = round(cost, 2)
repeating_cost = cost * (occurrences * working_months)
repeating_cost_rounded = round(repeating_cost, 2)
costs = "<pre>Single Meeting Cost: <font color=\'green\'><b>{}{:,}</b></font>   |   Annual Meetings Cost: <font color=\'red\'><b>{}{:,}</b></font></pre>".format(currency_symbol, cost_rounded, currency_symbol, repeating_cost_rounded)

# Create data for graph
if display_cost_graph:
    graph_df = pd.DataFrame(columns=['Month','Cost'])
    for i in range(working_months):
        month = i + 1
        month_cost = round((month * occurrences * cost), 2)
        if month < 10:
            month_string = 'Month 0{}'.format(month)
        else:
            month_string = 'Month {}'.format(month)
        graph_df = graph_df.append({'Month': month_string,'Cost':month_cost }, ignore_index=True)
    graph_df = graph_df.set_index(['Month'])

# Display
st.markdown('---')
if display_cost_graph:
    st.area_chart(graph_df, width=12)
st.markdown(costs, unsafe_allow_html=True)