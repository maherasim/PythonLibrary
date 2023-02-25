library = {}

def add_book(isbn, title, author, publisher,  pub_date):
    """Adds a book to the library"""
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
        

def show_books():
    """Shows the list of books in the library"""
    if len(library) == 0:
        print("The library is empty.")
    else:
        print("Books in the library:")
        for isbn, details in library.items():
            print(f"{details['title']} by {details['author']} (ISBN: {isbn})")

# Main program loop
while True:
    print("\nWhat would you like to do?")
    print("1. Show books in the library")
    print("2. Add a new book to the library")
    print("3. Remove Books from library")
    print("4. Search Books from library")
    print("5. Quit")
    choice = input("> ")
    
    if choice == "1":
        show_books()
    elif choice == "2":
        print("\nPlease enter the details of the book:")
        isbn = input("ISBN: ")
        title = input("Title: ")
        author = input("Author: ")
        publisher = input("Publisher: ")
        publication_date = input("Publication Date: ")
       
        add_book(isbn, title, author, publisher, publication_date)
    elif choice == "3":
        remove_book()
    elif choice == "4":
        search_book()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")
