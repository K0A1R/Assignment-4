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
