import book as b

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
            book_list.append([new_book])
            num_books += 1
    print('Book catalog has been loaded.')
    return num_books

def print_menu(menu_heading,menu_options):
    print(menu_heading)
    for key, value in menu_options.items():
        print(f'{key}. {value}')
    selection = int(input('Enter your selection: '))
    while (selection>3 or selection<0):
        print('Invalid option')
        selection = int(input('Enter your selection: '))
    else:
        return selection

def search_books(book_list,search_string):
    search_result = []
    for b in book_list:
        for book in b:
            if (search_string in book.get_isbn() or search_string.lower() in book.get_title().lower() or 
                search_string.lower() in book.get_author().lower() or search_string.lower() in book.get_genre_name().lower()):
                print(book)
                search_result.append(book)
    if (search_result == []):
        print('No matching books found.')
    return search_result

def main():
    book_list = []
    path_name = input('Enter book catalog filename: ')
    load_books(book_list,path_name)

    menu_heading = f"Reader's guild library - Main Menu\n{'='*34}"
    menu_options = {
        1: 'Search for books',
        2: 'Borrow a book',
        3: 'Return a book',
        0: 'Exit the system'
    }
    for book in book_list: #REMOVE! Checking to see if books.csv loaded into book_list
        print(book) #REMOVE
    print_menu(menu_heading,menu_options)

main()


