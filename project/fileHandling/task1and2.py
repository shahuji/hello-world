# 1.Write a Python program to read first n lines of a file

w = open("files/task1.txt", mode='r', encoding='utf-8')
print(w.read())
w.close()

# 2. Write a Python program to append text to a file and display the text.

print("--TASK 2--")
w = open('files/task2.txt', mode='w', encoding='utf-8')
print("Enter the text want to append: \n")
inputByUser = input()
while True:
    if inputByUser != "":
        w.write(inputByUser + "\n")
        break
    else:
        inputByUser = input("Enter the text want to append: \n")
w.close()

w = open('files/task2.txt', 'r', encoding='utf-8')
print(w.read())
w.close()


