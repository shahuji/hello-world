# 6. Write a function in Python to read lines from a text file "notes.txt".

totalWords = dict()
check = "the"

file_word = open('files/notes.txt', 'r')
for lines in file_word:
    line = lines.strip()  # this will remove whitespace and new line character
    # print(line)
    line = line.lower()  # Making all words same
    # print(line)
    words = line.split(" ")  # this divide thw line into words list
    # print(words)
    for word in words:
        if word in totalWords:
            totalWords[word] = totalWords[word] + 1
        else:
            totalWords[word] = 1

print("\n\nTotal occurrence of words({}) in \"notes.txt\" is | {}".format(check, totalWords[check]), "|")
print("Total number of words in \"notes.txt\" is | ", len(totalWords), "|")
# print("+-----------+")
# print('\nwords : count')
# for k, v in totalWords.items():
#     print(k, ' : ', v)
# print("+-----------+")
