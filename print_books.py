'''
Description: 
•	Receives a book list
•	Displays a book information heading, 
then iterates through the book list displaying 
each Book object on a separate line
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