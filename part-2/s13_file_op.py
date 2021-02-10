# simple read file
# def file_read(txt1):
#     txt = open(txt1)
#     print(txt.read())
#
# file_read("done-2.txt")

# read specific line
# def read_head(txt2, nline):
#     from itertools import islice
#     with open(txt2) as f:
#         for line in islice(f, nline):
#             print(line)
#
#
# read_head('done-2.txt', 3)

# write and read file
# def file_append_read(filename):
#     from itertools import islice
#     with open(filename, "w") as filer:
#         filer.write("Python file appended.\j")
#         filer.write("Done appending.")
#
#
# def readfile(filename):
#     txt = open(filename)
#     print(txt.read())
#
#
# file_append_read('txt1.txt')
# readfile('txt1.txt')

# find longest word in file.
# def findmaxwordlength(fiilename):
#     with open(fiilename) as file:
#         words = file.read().split(' ')
#         max_len = len(max(words, key=len))
#         return [word for word in words if len(word) == max_len]
#
#
# print(findmaxwordlength("txt1.txt"))
