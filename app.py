import streamlit as st
import pandas as pd
import plotly_express as px

# ---- Jupyter Notebooks ----

# Dataframe uploaded
df = pd.read_csv('.notebooks/dss.csv')

# Dropped salary and salary_currency column because it was redundant material.
df.drop(df[['salary','salary_currency']], axis = 1, inplace = True)

# Converted the experience levels instead of being abreviations to the full title of what they are.
df['experience_level'] = df['experience_level'].replace('EN','Entry-level')
df['experience_level'] = df['experience_level'].replace('MI','Mid-level')
df['experience_level'] = df['experience_level'].replace('SE','Senior-level')
df['experience_level'] = df['experience_level'].replace('Ex','Executive-level')
df['experience_level'] = df['experience_level'].replace('EX','Executive-level')

df = df.drop_duplicates()

df.duplicated().sum()

del df['index']

df.reset_index(inplace=True)
df

# ---- Streamlit Material ----

# title at top of tab
st.set_page_config(page_title="Data Science Salaries", layout='wide')

# ---- Header ----

with st.container():
    st.header("Hi, I am Cory!")
    st.subheader("I am an aspiring Data Scientist")
    st.write("I built this Website to showcase the salaries that people of all levels of Data Science can enjoy making with the different tables.")

st.dataframe(df)


# will create histogram based on: experience level and salary

list_for_hist = ['experience_level', 'salary_in_usd']

# create select box- interactive
choice_for_hist = st.selectbox('Choose experience level', list_for_hist)

# plotly histogram, where price is determined by choice in box
hist1 = px.histogram(df, x= 'salary_in_usd', color='experience_level', color_discrete_map={'Entry-level':'purple',
                                                                                          'Mid-level':'blue',
                                                                                          'Senior-level':'red', 'Executive-level':'green'})

#add title
hist1.update_layout(title="<b> Salary of level by {}</b>".format(choice_for_hist))

#embed for streamlit
st.plotly_chart(hist1)

# scatter plot 

st.write( """
#### Now let's find out how many people are within each job title, 
based on experience level
""")

#- Job title based on experience level = ['salary_in_usd']
#choice_for_scatter = st.selectbox('Remote work dependency', list_for_scatter)
scat1 = px.scatter(df, x='job_title', hover_data=['experience_level', 'remote_ratio'])

scat1.update_layout(
title="<br> Job Title VS </b>")
st.plotly_chart(scat1)

st.write("The scatter plot above showcases that as a position becomes more of a leadership role it gets more scarce. But you have alot of good opportunity as a basic role position!")

# making data tables on same line
left_column, right_column = st.columns(2)
left_column.plotly_chart(hist1, use_container_width=True)
right_column.plotly_chart(scat1, use_container_width=True)
