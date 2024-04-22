'''
Name: Library Management System Details
Description: 
This program will load library books from a CSV file and allow users to perform various functions to identify and modify information of the books through various menu options.
When the program is shut down, all of the books are saved to the CSV file.

Authors: Amrit Reddy, Harjap Singh, Devyn Weir
Date: 04/22/2024
'''
import book as b
import os

#Program Functions
'''
Function Name: load_books()
Description: This function reads the book attributes from the books.csv file, creates Book objects from each set of attributes 
and adds them one-by-one onto the list and appends each book into a book list.
Parameters: book_list - required parameter(list) - book list where books will be loaded into. 
path_name - required parameter(string) - path name of file to be loaded.
Returns: num_books - (int) - total number of books loaded from books.csv file.
'''
def load_books(book_list, path_name):
    num_books = 0
    with open(path_name) as file:
        for line in file:
            book_data = line.rstrip().split(',')
            isbn = book_data[0]
            title = book_data[1]
            author = book_data[2]
            genre = book_data[3]
            available = book_data[4]
            new_book = b.Book(isbn, title, author, int(genre), available.lower() == 'true')
            book_list.append(new_book)
            num_books += 1
    print('Book catalog has been loaded.')
    return num_books

'''
Function Name: print_menu()
Description: This function displays the heading and menu options passed in, inputs selection from user until valid selection is entered
and returns user's valid selection.
Parameters: menu_heading - required parameter(string) - main menu or librarian headings. , 
menu_options - required parameter(dictionary) - key and value pairs of menu options user can select.
Returns: selection - (int) - the user selection based on valid number selected
'''
librarian_menu = False
main_menu = True
def print_menu(menu_heading, menu_options):
    global librarian_menu
    global main_menu
    invalid_option = True
    print(menu_heading)
    for key, value in menu_options.items():
        print(f'{key}. {value}')
    
    while invalid_option:
        selection = input('Enter your selection: ')
        if(not selection.isdigit()):
            print('Invalid option')
        else:
            selection = int(selection)
            if selection == 2130 and main_menu:
                librarian_menu = True
                main_menu = False
                invalid_option = False
            elif selection != 2130 and main_menu:
                if selection > 3 or selection < 0:
                    print('Invalid option')
                    if (selection == 2130):
                        librarian_menu = True
                        main_menu = False
                else:
                    invalid_option = False
            elif librarian_menu:
                if selection > 6 or selection < 0:
                    print('Invalid option')
                else:
                    invalid_option = False
    return selection

'''
Function Name: menu_heading
Description: This function displays formatted menu headings.
Parameters: None
Returns: heading - the various formatted heading titles
'''
def menu_heading():
    isbn = 'ISBN'
    title = 'Title'
    author = 'Author'
    genre = 'Genre'
    available = 'Availability'
    isbn_line = '-'*14
    title_line = '-'*25
    author_line = '-'*25
    genre_line = '-'*20
    available_line = '-'*12
    heading = (
        f'{isbn:<15}'
        f'{title:<26}'
        f'{author:<26}'
        f'{genre:<21}'
        f'{available}\n'
        f'{isbn_line:<15}'
        f'{title_line:<26}'
        f'{author_line:<26}'
        f'{genre_line:<21}'
        f'{available_line}'
    )
    return heading

'''
Function Name: print_books
Description: This function iterates through a book list and displays a menu heading and then book object information on seperate lines.
Parameters: book_list - required parameter (list) - a list of book objects
Returns: None
'''
def print_books(book_list):
    print(menu_heading())
    for book in book_list:
        print(
            f'{book.get_isbn():<15}'
            f'{book.get_title():<26}'
            f'{book.get_author():<26}'
            f'{book.get_genre_name():<21}'
            f'{book.get_availability()}'
        )

'''
Function Name: search_books
Description: This function iterates through the list of books and checks if the search string appears in isbn, title, author, or genre name. 
If any match is found, the book is added to the search result list.
Parameters: book_list - required parameter(list) - the list of all the books loaded in. 
search_string - required parameter(string) - search string that the user enters to search for books.
Returns: search_result - (list) - list of books that the user searched for. 
'''

def search_books(book_list, search_string):
    search_result = []
    for book in book_list:
        if (search_string in book.get_isbn() or search_string.lower() in book.get_title().lower()
            or search_string.lower() in book.get_author().lower() or search_string.lower() in book.get_genre_name().lower()):
            search_result.append(book)
    if not search_result:
        print('No matching books found.')
    return search_result

'''
Function Name: find_book_by_isbn
Description: This function iterates through the ISBN numbers of each book object from the book list until a match is found.
Parameters: book_list - required parameter(list) - the list of all the books loaded in. 
isbn - required parameter - the ISBN value for match checking
Returns: book_list.index(book) - the index of the matching book
-1 - returned if no matches found
'''
def find_book_by_isbn(book_list,isbn):
    book_not_found = True
    for book in book_list:
        if(isbn == book.get_isbn()):
            book_not_found = False
            return book_list.index(book)
    if(book_not_found):
        return -1    

'''
Function Name: borrow_book
Description: This function takes an ISBN number entered by the user and checks for a match in the book list.
Depending on the matching book availability, it will display the appropriate message and and change the book availability status.
Parameters: book_list - required parameter(list) - the list of all the books loaded in. 
Returns: None
'''
def borrow_book(book_list):
    isbn = input('Enter the 13-digit ISBN (format 999-9999999999): ')
    book_index = find_book_by_isbn(book_list,isbn) 
    if(book_index!= -1):
        if(book_list[book_index].get_available()):
            print(f'"{book_list[book_index].get_title()}" with ISBN {book_list[book_index].get_isbn()} succesfully borrowed.')
            book_list[book_index].borrow_it()
        else:
            print(f'"{book_list[book_index].get_title()}" with ISBN {book_list[book_index].get_isbn()} is not currently available.')
    else:
        print('No book found with that ISBN.')

'''
Function Name: return_book
Description: This function takes an ISBN number entered by the user and checks for a match in the book list.
Depending on the matching book availability, it will display the appropriate message and and change the book availability status.
Parameters: book_list - required parameter(list) - the list of all the books loaded in. 
Returns: None
'''
def return_book(book_list):
    isbn = input('Enter the 13-digit ISBN (format 999-9999999999): ')
    book_index = find_book_by_isbn(book_list,isbn)  
    if(book_index!= -1):
        if(not book_list[book_index].get_available()):
            print(f'"{book_list[book_index].get_title()}" with ISBN {book_list[book_index].get_isbn()} succesfully returned.')
            book_list[book_index].return_it()
        else:
            print(f'"{book_list[book_index].get_title()}" with ISBN {book_list[book_index].get_isbn()} is not currently borrowed.')
    else:
        print('No book found with that ISBN.')

'''
Function Name: remove_book
Description: This function takes an ISBN number entered by the user and if the ISBN matches a book from the book list it will remove that book from the list and display the appropriate message.
Parameters: book_list - required parameter(list) - the list of all the books loaded in. 
Returns: None
'''
def remove_book(book_list):
    isbn = input('Enter the 13-digit ISBN (format 999-9999999999): ')
    book_index = find_book_by_isbn(book_list,isbn)  
    if(book_index!= -1):
        print(f'"{book_list[book_index].get_title()}" with ISBN {book_list[book_index].get_isbn()} succesfully removed.')
        del book_list[book_index]
    else:
        print('No book found with this ISBN.')

'''
Function Name: add_book
Description: This function receives a book list and uses user input to create a new instance of a book and ammends 
it to the book list. 
Parameters: book_list - required parameter (list) - a list of book objects
Returns: None
'''
def add_book(book_list):
    isbn = input('Enter the 13-digit ISBN (format 999-9999999999): ')
    title = input('Enter book title: ')
    author = input('Enter name of book author: ')
    available = True
    valid_genre = ['Romance', 'Mystery', 'Science Fiction', 'Thriller', 'Young Adult', "Children's Fiction", 'Self-help', 'Fantasy', 'Historical Fiction', 'Poetry']
    genre = input('Enter genre of book: ')
    while genre not in valid_genre:
        print("Invalid genre. Please choose from Romance, Mystery, Science Fiction, Thriller, Young Adult, Children's Fiction, Self-help, Fantasy, Historical Fiction, Poetry")
        genre = input('Enter genre of book: ')
    else:
        new_book = b.Book(isbn, title, author, valid_genre.index(genre), available)
        book_list.append(new_book)
        print(f"'{title}' with ISBN {isbn} sucessfully added.")

'''
Function Name: save_books
Description: This function iterates over a book list 
and forms a comma seperated string with the values of each
book object then saves the string with the book object values to 
a CSV file as seperate lines and returns the number of books saved
to the file.
Parameters: book_list - required parameter (list) - a list of book objects
path_name - required parameter - a name of the CSV file containing book information
Returns: num_of_books - a value for the number of books saved
'''
def save_books(book_list, path_name):
    with open(path_name, 'w') as file:
        for book in book_list:
            fixed_availability = book.get_availability()
            if fixed_availability == "Available":
                fixed_availability = "True"
            elif fixed_availability == "Borrowed":
                fixed_availability = "False"
            book_info = f'{book.get_isbn()},{book.get_title()},{book.get_author()},{book.get_genre()},{fixed_availability}\n'
            file.writelines(book_info)
        num_of_books = len(book_list)
        return num_of_books

def main():
    #Book list is initialized and user enters book catalog filename which is validated
    print('Starting the system ...')
    book_list = []
    path_name = input('Enter book catalog filename: ')

    #while not statement used to check if file exists
    while not os.path.exists(path_name):
        path_name = input('File not found. Re-enter book catalog filename: ')
    load_books(book_list, path_name)

    #Menu heading formatted string is stored in menu_heading variable
    #Menu options are stored in menu_options variable as a dictionary
    menu_heading = f"\nReader's guild library - Main Menu\n{'='*34}"
    menu_options = {
        1: 'Search for books',
        2: 'Borrow a book',
        3: 'Return a book',
        0: 'Exit the system'
    }

    #Menu heading and menu options are displayed using the print_menu() function
    #User selection is stored in the menu_selection variable
    menu_selection = print_menu(menu_heading,menu_options)

    #while statement used to validate selection options that exist in both the main menu or librarian menu
    while main_menu or librarian_menu:
        #if user selects option 0 the system will print appropriate message and save the book list to the CSV file, then exit the program
        if (menu_selection == 0):
            print(f'\n-- Exit the system --'
                  '\nBook catalogue has been saved.'
                  '\nGood Bye!')
            #save_books() used to save book list to CSV file
            save_books(book_list, path_name)
            #exit() exits the program
            exit()
        #if user selects option 1 they will be able to search the book list for any book that has information which matches their inputted search value
        if (menu_selection == 1):
            print(f'\n-- Search for Books --')
            search_string = input('Enter search value: ')
            #User search performed by search_books() function and stored in searched_books variable
            searched_books = search_books(book_list,search_string)
            #if statement used to validate whether searched_books contains any items which match the user search
            if(searched_books != []):
                print_books(searched_books)
            #Menu is displayed again for the user to make another selection
            menu_selection = print_menu(menu_heading,menu_options)
        #if user selects option 2 they will have the option of borrowing a book if it is available
        if (menu_selection == 2):
            print(f'\n-- Borrow a book --')
            #The user is able to attempt to borrow a book using the borrow_book() function
            borrow_book(book_list)
            #Menu is displayed again for the user to make another selection
            menu_selection = print_menu(menu_heading,menu_options)
        #if user selects option 3 they will be given the option to return a book
        if (menu_selection == 3):
            print(f'\n-- Return a book --')
            #The user is able to attempt to return a book using the return_book() function
            return_book(book_list)
            #Menu is displayed again for the user to make another selection
            menu_selection = print_menu(menu_heading,menu_options)
        #if the user enters 2130 they are directed to the Librarian Menu
        if (menu_selection == 2130):
            #while statement used to display correct menu while user is in Librarian Menu
            while librarian_menu:
                #Librarian Menu heading and menu selection options are stored in the variables menu_heading and menu_options
                menu_heading = f"\nReader's guild library - Librarian Menu\n{'='*34}"
                menu_options = {
                    1: 'Search for books',
                    2: 'Borrow a book',
                    3: 'Return a book',
                    4: 'Add a book',
                    5: 'Remove a book',
                    6: 'Print catalog',
                    0: 'Exit the system'
                }
                #Librarian Menu displayed to user with menu options
                menu_selection = print_menu(menu_heading,menu_options)
                #if user selects option 0 the system will print appropriate message and save the book list to the CSV file, then exit the program
                if (menu_selection == 0):
                    print(f'\n-- Exit the system --'
                  '\nBook catalogue has been saved.'
                  '\nGood Bye!')
                    #save_books() used to save book list to CSV file
                    save_books(book_list, path_name)
                    #exit() exits the program
                    exit()
                #if user selects option 1 they will be able to search the book list for any book that has information which matches their inputted search value
                if (menu_selection == 1):
                    print(f'\n-- Search for Books --')
                    search_string = input('Enter search value: ')
                    #Books with values that match the user inputted search value are validated through the search_books() function and displayed using the print_books() function
                    print_books(search_books(book_list,search_string))
                #if user selects option 2 they will have the option of borrowing a book if it is available
                if (menu_selection == 2):
                    print(f'\n-- Borrow a book --')
                    #The user is able to attempt to borrow a book using the borrow_book() function
                    borrow_book(book_list)
                #if user selects option 3 they will be given the option to return a book
                if (menu_selection == 3):
                    print(f'\n-- Return a book --')
                    #The user is able to attempt to return a book using the return_book() function
                    return_book(book_list)
                #if user selects option 4 they will be given the option to add a book to the book list by providing all necessary information 
                if(menu_selection == 4):
                    print(f'\n-- Add a book --')
                    #A new book is added to the book list by the user using the add_book() function
                    add_book(book_list) 
                #if user selects option 5 they will be given the option to remove a book from the book list
                if(menu_selection == 5):
                    print(f'\n-- Remove a book --')
                    #The program will remove a book from the book list using the remove_book function and receiving user input
                    remove_book(book_list) 
                #if user selects option 6 the complete book list will be displayed 
                if(menu_selection == 6):
                    print(f'\n-- Print book catalog --')
                    #The book list is displayed to the user using the print_books() function
                    print_books(book_list) 
      
main()

