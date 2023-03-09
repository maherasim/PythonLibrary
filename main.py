from LibraryOOP import Library

library=Library()
library.add_book()
library.remove_book()
library.search_book()
library.display_books()
library.check_out()
library.check_in()


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
