import streamlit as st
import pandas as pd
import seaborn as sns

st.write("""
# Lior first app
Hello *world!*
""")
st.text('This is some text.')

df = sns.load_dataset ('dowjones')
df2 = df.copy()
df2 = df2.set_index ('Date')
print (df2)
st.line_chart(data=df, x='Date', y='Price', x_label = 'Day', y_label='kuku')
