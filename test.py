def load_books(book_list,path_name):
    num_books = 0
    with open(path_name) as file:
        for line in file:
            book = line.rstrip().split(',')
            isbn = book[0]
            title = book[1]
            author = book[2]
            genre = book[3]
            available = book[4]
            book_obj = isbn +','+ title +','+ author +','+ genre +','+ available
            book_list.append(book_obj)
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
    for book in book_list:
        if (search_string in book):
            search_result.append(book)
    if (search_result == []):
        print('No matching books found.')
    return search_result

def main():
    book_list = []
    path_name = input('Enter book catalog filename: ')
    load_books(book_list,path_name)
    print(book_list) #REMOVE

    menu_heading = f"Reader's guild library - Main Menu\n{'='*34}"
    menu_options = {
        1: 'Search for books',
        2: 'Borrow a book',
        3: 'Return a book',
        0: 'Exit the system'
    }
    print_menu(menu_heading,menu_options)
    
    #SEARCH STRING
    '''search_string = input('Enter your selection: ')
    search_books(book_list,search_string)'''

main()