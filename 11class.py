class Book:
    total_books = 0       #class variable
    def __init__(self,book_name): 
        self.book_name = book_name
        Book.total_books += 1    

    def display_book_name(self):
        print(f"The book name is {self.book_name.capitalize()}.")    
    @classmethod
    def increment_book_count(cls):
        print(f"Total updated book count: {cls.total_books}.")
book1 = Book("the silent patient" )
book2 = Book("the girl in the ice" )
book1.display_book_name()
book2.display_book_name()       
Book.increment_book_count()


