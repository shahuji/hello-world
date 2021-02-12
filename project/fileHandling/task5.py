# 5. Write a function in Python to count and display the total number of words in a text file.

totalWords = 0
file_word = open('files/story.txt', 'r')
for lines in file_word:
    line = lines.strip()  # this will remove whitespace and new line character
    # print(line)
    words = line.split(" ")  # this divide thw line into words list
    # print(words)
    for count in words:
        totalWords += 1

print("Total numbers of words in \"story.txt\" is |", totalWords, "|")
