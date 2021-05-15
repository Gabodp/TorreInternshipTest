import pandas as pd
csv_file_name = "reed_uk.csv"

df = pd.read_csv(csv_file_name)

job_board = df['job_board']

# rows of dataframe
num_rows = df.shape[0]
print(num_rows)

# reed is the only value in the job_board column
print(job_board.unique())

job_titles = df['job_title'].unique()
num_unique_titles = len(job_titles)

print(job_titles)
print(num_unique_titles)
