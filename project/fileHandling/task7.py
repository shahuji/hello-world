# 7. Write a function display_words() in python to read lines from a text file "story.txt",
#     and display those words, which are less than 4 characters.

totalWords = dict()


def display_words(lines):
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

    print("-----------------------")
    for word in totalWords:
        if totalWords[word] <= 4:
            print(word, " is less then 4.")
    print("-----------------------")


file_word = open('files/story.txt', 'r')
for lines in file_word:
    display_words(lines)
