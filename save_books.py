
def save_books(book_list, path_name):
    with open(path_name, 'w') as file:
        for book in book_list:
            book_info = f'{book.__str__()}\n' #currently will always save with genre name and not availability number
            file.writelines(book_info)
        num_of_books = len(book_list)
        print(f'{num_of_books} books saved to the file')
