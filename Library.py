class Book:
    count = 0 

    def __init__(self):
        self.author = ""
        self.book_price = 0
        self.book_name = ""
        Book.count += 1 

    def set_author(self, author_name):
        self.author = author_name

    def set_book_name(self, book_name):
        self.book_name = book_name

    def set_book_price(self, price):
        self.book_price = price

    def display_details(self):
        print(f"Author Name: {self.author}")
        print(f"Book Name: {self.book_name}")
        print(f"Book Price: {self.book_price}")


class Library:
    def __init__(self):
        self.books = []  

    def add_book(self, book):
        self.books.append(book)

    def show_all_books(self):
        if not self.books:
            print("No books in library yet.")
        else:
            print("\nAll Books in Library:")
            for i, book in enumerate(self.books, 1):
                print(f"Book {i}:")
                book.display_details()


def menu():
    print("\n----- Library Menu -----")
    print("1. Add Book")
    print("2. Show All Books")
    print("3. Exit")


library = Library()

while True:
    menu()
    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        book = Book()
        author = input("Enter Author Name: ")
        book.set_author(author)

        name = input("Enter Book Name: ")
        book.set_book_name(name)

        price = float(input("Enter Book Price: "))
        book.set_book_price(price)

        library.add_book(book)
        print("Book added successfully!")

    elif choice == '2':
        library.show_all_books()

    elif choice == '3':
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice, please enter 1, 2, or 3.")
