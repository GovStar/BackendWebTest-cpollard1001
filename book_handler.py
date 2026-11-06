from dataclasses import dataclass
from typing import List, Optional, AnyStr, Any, Dict

@dataclass
class Book:
    author: str
    title: str
    year: int
    id: int
    tags: Optional[List[str]]

    def to_json(self) -> dict:
        return {}

@dataclass()
class Library:
    books: Dict[int: Book]

class Book_Handler:

    def __init__(self):
        pass

    def load_books_json(self) -> Optional[List[Book]]:
        return None

    def load_books(self) -> bool:
        return False

    def get_book_by_id(self, book_id: int)-> Optional[Dict[str, Any]]:
        return None

    def del_book_by_id(self, book_id: int)-> bool:
        return False
