# 8. Write a function in Python to count the words "this" and "these" present in a text file "article.txt".
#     [Note that the words "this" and "these" are complete words]

totalWords = dict()
word1 = 0
word2 = 0

with open("files/article.txt", "r") as f:
    for line in f:
        for word in line.split():
            if word == "This" or word == "this":
                word1 += 1
            if word == "These" or word == "these":
                word2 += 1
print("This : ", word1)
print("These : ", word2)
