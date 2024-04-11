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
        

menu_heading = f"Reader's guild library - Main Menu\n{'='*34}"
menu_options = {
    1: 'Search for books',
    2: 'Borrow a book',
    3: 'Return a book',
    0: 'Exit the system'
}
print_menu(menu_heading,menu_options)