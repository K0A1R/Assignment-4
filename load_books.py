import book
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
            new_book = book.Book(isbn, title, author, int(genre), available.lower() == 'true')
            book_list.append(new_book)
            num_books += 1
            print (new_book)
    print('Book catalog has been loaded.')
    return num_books

book_list = []
path_name = input('Enter book catalog filename: ')
load_books(book_list, path_name)