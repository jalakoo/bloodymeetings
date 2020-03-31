# COST OF MEETINGS CALCULATOR
This is a simple cost of meetings calculator based on annual salaries for selected attendees. The app itself does not account for regional salary differences, taxes, or other operational costs. These however, could be included in your own custom dataset.

# OPTIONS
FIELD NAME | DESCRIPTION | DEFAULT VALUE
----- | ----- | --------
Currency Symbol | For indicating which currency for displaying cost information | $
Meeting Length | Length of a meeting in minutes | 60
Occurrences Per Month | How often in a month a meeting repeats. 20 equates to every business day over a 4 week period. Set to 0 if the meeting is not recurring | 4
Working Months | How many months that this meeting will occur over | 11
Salary Data Source URL | Defaults to a dataset of average annual job salaries for a very limited set of roles in the US, at the date of this commit. An alternate address to a static .csv file may be used, so long as the .csv file contains these column names: `NAME,ANNUAL_SALARY`. The `ANNUAL_SALARY` column contains only integer representations of a positions annual salary (no currency indicators, commas or decimal values). A re-indexed version of this .csv will display in the `Salary Data` table. | Sample data from an AWS S3 bucket is provided
Meeting Attendees | Multiselect list of attendee by job roles (if using the provided default data source) | 4 developer jobs roles
Edit Data Source | Checkbox for displaying Salary Data Source URL field | Unchecked
Show Salary Data | Checkbox for displaying Indexed Salary data from the data source | Unchecked
Show Cost Graph | Checkbox for displaying a graph of monthly aggregating cost over time | Unchecked

## REQUIREMENTS
### STREAMLIT
This applicaiton makes use of [Streamlit](https://www.streamlit.io), see:
- [Install Instructions here](https://docs.streamlit.io/getting_started.html#install-streamlit)
- To run this app from the terminal: `streamlit run app.py`


## ISSUES
PROBLEM: `URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1076)>`
SOLUTION: On OSX, goto the Applications/Python 3.7 folder then double-click on `Install Certficates.command`