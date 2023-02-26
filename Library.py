library = {}

def add_book():
    """Add a book to the library"""
    isbn = input("Enter the book's ISBN: ")
    if isbn in library:
        print("The book already exists in the library!")
    else:
        title = input("Enter the book's title: ")
        author = input("Enter the book's author: ")
        publisher = input("Enter the book's publisher: ")
        pub_date = input("Enter the book's publication date (YYYY-MM-DD): ")
        pages = int(input("Enter the book's number of pages: "))
        library[isbn] = {"title": title, "author": author, "publisher": publisher, 
                         "publication date": pub_date, "pages": pages, "checked out": False}
        print("The book has been added to the library.")

def remove_book():
    """Remove a book from the library"""
    isbn = input("Enter the book's ISBN to remove: ")
    if isbn in library:
        del library[isbn]
        print("The book has been removed from the library.")
    else:
        print("The book was not found in the library.")

def search_book():
    """Search for a book in the library"""
    isbn = input("Enter the book's ISBN to search: ")
    if isbn in library:
        print("Book details:")
        for key, value in library[isbn].items():
            print(f"{key.capitalize()}: {value}")
    else:
        print("The book was not found in the library.")

def display_books():
    """Display all books in the library"""
    if library:
        print("Library books:")
        for isbn, details in library.items():
            print(f"ISBN: {isbn}")
            for key, value in details.items():
                print(f"{key.capitalize()}: {value}")
            print("")
    else:
        print("The library is empty.")

def check_out():
    """Check out a book from the library"""
    isbn = input("Enter the book's ISBN to check out: ")
    if isbn in library:
        if library[isbn]['checked out']:
            print("The book is already checked out.")
        else:
            library[isbn]['checked out'] = True
            print("The book has been checked out.")
    else:
        print("The book was not found in the library.")

def check_in():
    """Check in a book to the library"""
    isbn = input("Enter the book's ISBN to check in: ")
    if isbn in library:
        if library[isbn]['checked out']:
            library[isbn]['checked out'] = False
            print("The book has been checked in.")
        else:
            print("The book is not checked out.")
    else:
        print("The book was not found in the library.")

def main():
    """Main program loop"""
    while True:
        print("\nLibrary Management System")
        print("1. Add book")
        print("2. Remove book")
        print("3. Search book")
        print("4. Display all books")
        print("5. Check out a book")
        print("6. Check in a book")
        print("7. Quit")
        choice = input("Enter your choice (1-7): ")
        if choice == "1":
            add_book()
        elif choice == "2":
            remove_book()
        elif choice == "3":
            search_book()
        elif choice == "4":
            display_books()
        elif choice == "5":
            check_out()
        elif choice == "6":
            check_in()
        elif choice == "7":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()

