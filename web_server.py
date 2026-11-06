from .book_handler import *

book_handler = Book_Handler()

#Route /
def home():
    return "<p>Hello, World!</p>"

#Route /books
# METHODS GET POST
def books():
    return "<p>Books!!!</p>"

#Route /books/<book_id>
# METHODS GET DELETE
def book_index(book_id):
    return "<p>Searching</p>"