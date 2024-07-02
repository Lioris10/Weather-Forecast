import streamlit as st
import pandas as pd
import seaborn as sns

from datetime import date
from datetime import datetime

st.write("""
# Lior first Streamlit app
Hello *world!*
""")
st.text('This is some text.')


df = sns.load_dataset ('dowjones')

# Ensure 'Date' is a datetime column
df['Date'] = pd.to_datetime(df['Date']).dt.date

# print ("df")
# print (df)

# Option 1 -  Line Chart from df2
# df2 = df.copy()
# Getting rid of th 0,1,2,3 index column and replacing it with date as index
# df2 = df2.set_index ('Date')
# print ("df2")
# print (df2)
# st.line_chart(df2)


# Option 2 - Line Chart from df
st.line_chart(data=df, x='Date', y='Price', x_label = 'Time', y_label='Dow Price')

# Find min and max dates in the dataset to set default date inputs
min_date = df['Date'].min()
print(f"min date: {min_date}")

max_date = df['Date'].max()
print(f"max date: {max_date}")

today = date.today()

# Create two date input widgets for the from date and to date
# The inputs will appear as columns -side by side
st.subheader("Select Date Range")

col1, col2 = st.columns(2)
with col1:
    from_date = st.date_input("From Date", min_value=min_date, max_value=max_date, format="YYYY-MM-DD")

with col2:
    to_date = st.date_input("To Date", min_value=min_date, max_value=max_date, format="YYYY-MM-DD")

# Display the selected date range and the sliced DataFrame
# st.write("From Date:", from_date)
# st.write("To Date:", to_date)

# Convert date inputs to string
# from_date_str = from_date.strftime('%Y-%m-%d')
# to_date_str = to_date.strftime('%Y-%m-%d')

# Filtering df3 from df according to Date Range on the input
# df3 = df.loc [from_date : to_date] # this is good if the date was the row index! faster execution.
df3 = df.loc[(df['Date'] >= from_date) & (df['Date'] <= to_date)]  # this is a filter

with st.container():
    st.write("## Sliced DataFrame")
    st.dataframe(df3)

    st.write("## Updated Line Chart")
    st.line_chart(data=df3, x='Date', y='Price', x_label='Time', y_label='Dow Price')