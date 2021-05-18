# This file was replaced by the Jupyter Notebook. Please Ignore


import pandas as pd
csv_file_name = "reed_uk.csv"

df = pd.read_csv(csv_file_name)

job_board = df['job_board']
# reed is the only value in the job_board column, it can be ignored in the graph
print(job_board.unique())

# DATASET INFO
print("-----NUMBER OF DATASET ROWS------")
print(df.shape[0])

print("----------------------------")
# Check how many unique job titles are there in the dataset and its count
num_unique_titles = len(df['job_title'].unique())
print("There are %d unique job titles" % num_unique_titles)
print(df['job_title'].value_counts()[:15].sort_values(ascending=False))

print("----------------------------")
# Checking how many unique companies are there in the dataset
companies = df['company_name']
print("There are %d unique companies" % len(companies.unique()))
print(companies.value_counts()[:15].sort_values(ascending=False))

print("----------------------------")
# Checking skills values
requirements = df['job_requirements']
print(len(requirements.unique()))
print(requirements.value_counts()[:15].sort_values(ascending=False))

print("----------------------------")
# Checking country values
countries = df['geo']
