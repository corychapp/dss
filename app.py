import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly_express as px


# ---- Jupyter Notebooks ----

# Dataframe uploaded
df = pd.read_csv('notebooks/dss.csv')

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


df.reset_index(drop=True, inplace=True)

df.rename( columns={'Unnamed: 0':'index'}, inplace=True )


# ---- Streamlit Material ----

# title at top of tab


# ---- Header ----

with st.container():
    st.header("Hi, I am Cory!")
    st.subheader("I am an aspiring Data Scientist")
    st.write("I built this Website to showcase the salaries that people of all levels of Data Science can enjoy making with the different tables.")

st.dataframe(df)

# Define list of variables to display in dropdown
#list_for_hist = ['experience_level', 'salary_in_usd']

# Create select box for experience level
experience_level = st.selectbox('Select experience level', sorted(df['experience_level'].unique()))

# Filter data by selected experience level
filtered_hist_data = df[df['experience_level'] == experience_level]

# Create histogram with Plotly Express
hist1 = px.histogram(filtered_hist_data, x='salary_in_usd', color='experience_level', color_discrete_map=   {'Entry-level':'purple',
                                                                                                      'Mid-level':'blue',
                                                                                                      'Senior-level':'red',
                                                                                                      'Executive-level':'green'})

# Add title
hist1.update_layout(title="<b>Salary distribution for {} level</b>".format(experience_level))

# Embed in Streamlit
st.plotly_chart(hist1)



# Define a list of all job titles
all_job_titles = df['job_title'].unique().tolist()

# Define a default selection that includes all four job titles
default_selection = ['Data Engineer', 'Data Analyst', 'Data Scientist', 'Machine Learning Engineer']

# Create a multiselect widget to select job titles
selected_job_titles = st.multiselect('Select job titles', options=all_job_titles, default=default_selection)
df_filtered = df[df['job_title'].isin(selected_job_titles)]
# Create a radio button widget to select experience level

strip =  px.strip(data_frame=df_filtered, x='job_title', y='salary_in_usd', color='experience_level', color_discrete_map=   {'Entry-level':'purple', 'Mid-level':'blue', 'Senior-level':'red', 'Executive-level':'green'}) 

# Display the plot within a Streamlit app using st.pyplot():
st.plotly_chart(strip)