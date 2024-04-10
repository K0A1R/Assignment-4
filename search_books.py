def search_books(book_list,search_string):
    search_result = []
    for book in book_list:
        if (search_string in book):
            search_result.append(book)
    if (search_result == []):
        print('No matching books found.')
    return search_result