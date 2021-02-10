class Library:

    def __init__(self, book_list, name):
        self.booklist = book_list
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f"List of library Books: {self.name}")
        for book in self.booklist:
            print(book)

    def lendBook(self, username, book):
        """

        :param username: name of user
        :type book: bookname name for rent
        """
        if book not in self.lendDict.keys():
            self.lendDict.update({book: username})
            print(f"Books Updated!!!\nYou can take now {book}...")
        else:
            print(f"Book is already in use by {self.lendDict[book]}")

    def addBook(self, bookname):
        self.booklist.append(bookname)
        print("Book added succesfully...")

    def returnBook(self, bookname):
        self.lendDict.pop(bookname)
        print("Book removed!!!")


if __name__ == '__main__':
    vishal = Library(['Python', 'Java', 'A.I.', 'Harry Potter', 'Rich Dad Poor Dad'], "Shahuji")

    while True:
        print(f"Welcome to the {vishal.name} library.\nEnter your choice: ")
        print("1. Display Books")
        print("2. Lend a Book")
        print("3. Add a Book")
        print("4. Return Book")
        print("0. Exit")
        user_choice = int(input())

        if user_choice == 1:
            vishal.displayBooks()

        elif user_choice == 2:
            book = input("Enter the bookname name you want to land: ")
            user = input("Enter your name: ")
            vishal.lendBook(user, book)

        elif user_choice == 3:
            book = input("Enter the bookname name you want to add: ")
            vishal.addBook(book)

        elif user_choice == 4:
            book = input("Enter the bookname name you want to add: ")
            vishal.returnBook(book)

        elif user_choice == 0:
            exit()

        else:
            print("Enter right option!!!")
