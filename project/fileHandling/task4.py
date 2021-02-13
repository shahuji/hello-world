# 4. Write a function in python to count the number of lines from a text file "story.txt" which is not starting with an alphabet "T".

file_check = open('files/story.txt', 'r')
count = 0
for line in file_check:
    if not line.startswith('T'):
        count += 1

print("Number of line not containing \"T\" is ", count)
