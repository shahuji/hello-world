import csv

# with default seperater
with open('data.csv', 'r') as file:
    writerer = csv.reader(file)
    for read in writerer:
        print(read)

# with user define seperater
with open('data.csv', 'r') as file:
    writerer = csv.reader(file, delimiter='\t')
    for read in writerer:
        print(read)
