
csv_file_name = "reed_uk.csv"

with open(csv_file_name, mode='r') as csv_file:
    data = {}
    headers = csv_file.readline()

    # for line in csv_file.readlines():


