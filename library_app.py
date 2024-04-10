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

def search_books(book_list,search_string):
    search_result = []
    for book in book_list:
        if (search_string in book):
            search_result.append(book)
    if (search_result == []):
        print('No matching books found.')
    print(search_result) #REMOVE
    return search_result

book_list = []
path_name = input('Enter book catalog filename: ')
load_books(book_list,path_name)
#SEARCH STRING
search_string = input('Enter your selection: ')
search_books(book_list,search_string)



