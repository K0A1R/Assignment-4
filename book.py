class Book():
    def __init__(self, isbn, title, author, genre, available):
        self.__isbn = isbn
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__available = available
    def get_isbn(self):
        return self.__isbn
    def get_title(self):
        return self.__title
    def get_author(self):
        return self.__author
    def get_genre(self):
        return self.__genre
    def get_available(self):
        return self.__available
    def set_isbn(self, isbn):
        self.__isbn = isbn
    def set_title(self,title):
        self.__title = title
    def set_author(self,author):
        self.__author = author
    def set_genre(self,genre):
        self.__genre = genre
    def get_genre_name(self):
        match self.__genre:
            case 0:
                self.__genre = 'Romance'
                return self.__genre
            case 1:
                self.__genre = 'Mystery'
                return self.__genre
            case 3:
                self.__genre = 'Science Fiction'
                return self.__genre
            case 4:
                self.__genre = 'Thriller'
                return self.__genre
            case 5:
                self.__genre = 'Young Adult'
                return self.__genre
            case 6:
                self.__genre = "Children's Fiction"
                return self.__genre
            case 7:
                self.__genre = 'Self-help'
                return self.__genre
            case 8:
                self.__genre = 'Fantasy'
                return self.__genre
            case 8:
                self.__genre = 'Historical Fiction'
                return self.__genre
            case 9:
                self.__genre = 'Poetry'
                return self.__genre
    
    def get_availability(self):
        if (self.__available == True):
            self.__available = 'Available'
        else:
            self.__available = 'Borrowed'
        return self.__available

    def borrow_it(self):
        self.__available = False
    def return_it(self):
        self.__available = True

    def __str__(self):
        return (f'{self.__isbn} {self.__title} {self.__author} {self.__genre} {self.get_availability()}')

book1 = Book('978-0060000000','To Kill a Mockingbird','Harper Lee',3,True) #REMOVE
print(book1.get_genre_name()) #REMOVE
print(book1.__str__()) #REMOVE

