library = {}

def add_book(isbn, title, author, publisher, publication_date):
    """Adds a book to the library"""
    library[isbn] = {"title": title, "author": author, "publisher": publisher, "publication_date": publication_date}
    print("Book added successfully.")

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
    print("3. Quit")
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
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
