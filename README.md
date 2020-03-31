# COST OF MEETINGS CALCULATOR
This is a simple cost of meetings calculator based on annual salaries for selected attendees. The app itself does not account for regional salary differences, taxes, or other operational costs. These however, could be included in your own custom dataset.

# OPTIONS
## Salary Data URL
Defaults to a dataset of average annual job salaries for a very limited set of roles in the US, at the date of this commit. An alternate address to a static .csv file may be used, so long as the .csv file contains these column names: `NAME,ANNUAL_SALARY` and the `ANNUAL_SALARY` column contains only integer representations of a positions annual salary (no currency indicators, commas or decimal values). For example: `
```
NAME,ANNUAL_SALARY
Full Stack Developer - Junior,93000
```
A re-indexed version of this .csv will display in the `Salaries` table.

*NOTE: Currency sign was intentionally omitted so a dataset with any currency value could be used.*

## Choose attendee job roles
Select the name of the attendees' positions to add them to the cost calculator.

*NOTE: Currently only one of each job role can be selected from the example data set. Use a different dataset with name variations having the same salary value or something like an employee-id to differentiate roles.* 

## Lefthand Panel
Contains additional cost calculation parameters.

### Meeting Length
How long the meeting is in minutes. Currently 480min or 8hrs is the arbitrarily set max calculable time.

### Repeating Occurances Per Month
How many times a month this particular meeting occurs. Set 0 if it's a one-off meeting. Max is 20, which would be every work day for a typical 4 week month.

### Working Months
How many months out of the year to consider in the calculation. Default is sit to 11 months to account for 2 weeks of set holidays, and another 2 to cover time off, sicknesses, and other events. Maybe useful for calculating seasonal or limited length projects. Setting this to 0 will also equate calculation to a one-off meeting.

## REQUIREMENTS
### STREAMLIT
This applicaiton makes use of [Streamlit](https://www.streamlit.io), see:
- [Install Instructions here](https://docs.streamlit.io/getting_started.html#install-streamlit)
- To run this app from the terminal: `streamlit run app.py`


## ISSUES
PROBLEM: `URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1076)>`
SOLUTION: On OSX, goto the Applications/Python 3.7 folder then double-click on `Install Certficates.command`