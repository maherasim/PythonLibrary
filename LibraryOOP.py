class Library:
    def __init__(self):
        self.books = {}

    def add_book(self):
        """Add a book (or multiple copies) to the library"""
        isbn = input("Enter the book's ISBN: ")
        title = input("Enter the book's title: ")
        author = input("Enter the book's author: ")
        publisher = input("Enter the book's publisher: ")
        pub_date = input("Enter the book's publication date (YYYY-MM-DD): ")
        num_copies = int(input("Enter the number of copies to add: "))

        if isbn not in self.books:
            self.books[isbn] = []

        for i in range(num_copies):
            copy_id = f"{isbn}_{i+1}"
            self.books[isbn].append({"copy_id": copy_id, "title": title, "author": author, "publisher": publisher, 
                             "publication date": pub_date, "status": "available"})

        print(f"{num_copies} copies of the book have been added to the library.")

    def remove_book(self):
        """Remove a book from the library"""
        isbn = input("Enter the book's ISBN to remove: ")
        if isbn in self.books:
            del self.books[isbn]
            print("The book has been removed from the library.")
        else:
            print("The book was not found in the library.")

    def search_book(self):
        """Search for a book in the library"""
        isbn = input("Enter the book's ISBN to search: ")
        if isbn in self.books:
            print("Book details:")
            for copy in self.books[isbn]:
                for key, value in copy.items():
                    print(f"{key.capitalize()}: {value}")
                print("")
        else:
            print("The book was not found in the library.")

    def display_books(self):
        """Display all books in the library"""
        if self.books:
            print("Library books:")
            for isbn, copies in self.books.items():
                print(f"ISBN: {isbn}")
                for copy in copies:
                    for key, value in copy.items():
                        print(f"{key.capitalize()}: {value}")
                    print("")
        else:
            print("The library is empty.")

    def check_out(self):
        """Check out a book from the library"""
        isbn = input("Enter the book's ISBN to check out: ")
        if isbn in self.books:
            available_copies = [copy for copy in self.books[isbn] if copy['status'] == 'available']
            if available_copies:
                copy = available_copies[0]
                copy['status'] = 'checked out'
                print(f"The book copy with ID {copy['copy_id']} has been checked out.")
            else:
                print("All copies of the book are currently checked out.")
        else:
            print("The book was not found in the library.")

    def check_in(self):
        """Check in a book to the library"""
        isbn = input("Enter the book's ISBN to check in: ")
        if isbn in self.books:
            checked_out_copies = [copy for copy in self.books[isbn] if copy['status'] == 'checked out']
            if checked_out_copies:
                copy = checked_out_copies[0]
                copy['status'] = 'available'
                print(f"The book copy with ID {copy['copy_id']} has been checked in.")
            else:
                print("All copies of the book are currently checked in.")
library = Library()

while True:
    print("Enter a command: ")
    print("1 - Add a book")
    print("2 - Remove a book")
    print("3 - Search for a book")
    print("4 - Display all books")
    print("5 - Check out a book")
    print("6 - Check in a book")
    print("0 - Exit")
    
    command = input()
    
    if command == '1':
        library.add_book()
    elif command == '2':
        library.remove_book()
    elif command == '3':
        library.search_book()
    elif command == '4':
        library.display_books()
    elif command == '5':
        library.check_out()
    elif command == '6':
        library.check_in()
    elif command == '0':
        break
    else:
        print("Invalid command. Please enter a valid command.")
