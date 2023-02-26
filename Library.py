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
       
        library[isbn] = {"title": title, "author": author, "publisher": publisher, 
                         "publication date": pub_date}
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

def main():
    """Main program loop"""
    while True:
        print("\nLibrary Management System")
        print("1. Add book")
        print("2. Remove book")
        print("3. Search book")
        print("4. Display all books")
        print("5. Quit")
        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            add_book()
        elif choice == "2":
            remove_book()
        elif choice == "3":
            search_book()
        elif choice == "4":
            display_books()
        elif choice == "5":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
