import pandas as pd
csv_file_name = "reed_uk.csv"

df = pd.read_csv(csv_file_name)

job_board = df['job_board']

# reed is the only value in the job_board column
print(job_board.unique())

job_titles = df['job_title'].unique()
print(job_titles)
