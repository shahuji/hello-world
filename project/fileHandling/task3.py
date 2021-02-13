# 3. Write a function in python to read the content from a text file "poem.txt" line by line
# and display the same on screen.

file_read = open('files/poem.txt', 'r')
for line in file_read:
    print(line)


