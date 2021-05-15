import pandas as pd
csv_file_name = "reed_uk.csv"

df = pd.read_csv(csv_file_name)

job_board = df['job_board']
# reed is the only value in the job_board column, it can be ignored in the graph
print(job_board.unique())

# DATASET INFO
print("-----NUMBER OF DATASET ROWS------")
print(df.shape[0])

# Check how many unique job titles are there in the dataset and its count
num_unique_titles = len(df['job_title'].unique())
print(df['job_title'].value_counts()[:15].sort_values(ascending=False))

print("----------------------------")
# Checking skills values
requirements = df['job_requirements']
requirements_unique = requirements.unique()
print(len(requirements_unique))
print(requirements.value_counts()[:15].sort_values(ascending=False))

