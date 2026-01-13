class Book:
    def __str__(self):
        return "Library Books"

    def __repr__(self):
        return "Book(id=534, title='Novel')"


book = Book()

print(book)          
list_of_books = [book]
print(list_of_books) 
