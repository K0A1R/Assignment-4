import os
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

book_list = []
path_name = input('Enter book catalog filename: ')
print(load_books(book_list, path_name))

if(os.path.exists(path_name)):
    print("Book catalog has been loaded")
else:
    path_name = input("File not found. Re-enter book catalog filename: ")


