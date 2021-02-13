import csv

"""
['Programming language', 'Designed by', 'Appeared', 'Extension'],
           ['Python', 'Guido van Rossum', '1991', '.py'],
           ['Java', 'James Gosling', '1995', '.java'],
           ['C++', 'Bjarne Stroustrup', '1983', '.cpp'],
           ['.net', 'Vishal Shahu', '1998', '.net']
"""
content = []

with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    globals()['content'] = list(reader)
    # for read in content:
    #     print(read)
    # globals()['content'] = reader

# Executive,Bjarne Stroustrup,1985,.jar
with open('data2.csv', 'w', newline='') as file1:
    writer = csv.writer(file1)
    writer.writerows(content)

with open('data2.csv', 'r') as file2:
    reader = csv.reader(file2)
    for read in reader:
        print(read)
