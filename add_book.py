''' 
Description:
•	Receives a book list
•	Inputs ISBN, title, author, and genre name from the user. Genre name is validated – it must be one of the names listed earlier in the description of get_genre_name() – and translated into its integer value.
•	Creates a new instance of Book and appends it to the list
'''
class Book:
    pass 
def add_book(book_list):
    isbn = input('Enter book ISBN number: ')
    title = input('Enter book title: ')
    author = input('Enter name of book author: ')
    genre = int(input('Enter genre of book: '))
    available = input('Enter availability: ')
    new_book = Book(isbn, title, author, genre, available)
    book_list.append(new_book)

'''
    valid_genre = get_genre_name()
    while genre not in valid_genre:
        print(f'Invalid genre. Please choose from:', {valid_genre})
        genre = input('Enter genre of book: ')
    else:
        new_book = Book(isbn, title, author, genre)
        book_list.append(new_book)
'''