import json
import os
import math

FILE_NAME = 'books.json'

class Book:
    def __init__(self, title, author, price, stock):
        self.title = title
        self.author = author
        self.price = price
        self.stock = stock

    def __str__(self):
        return f'"{self.title}" by {self.author} | Price: ₦{self.price:.2f} | Stock: {self.stock}'

def save_inventory(books):
    with open(FILE_NAME, 'w') as file:
        json.dump([b.__dict__ for b in books], file, indent=4)
    print("Inventory saved.")

def load_inventory():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            books_data = json.load(file)
            return [Book(**data) for data in books_data]
    return []

def add_book(books):
    title = input("Enter title: ")
    author = input("Enter author: ")
    try:
        price = math.ceil(float(input("Enter price: ")))
        stock = int(input("Enter stock: "))
        new_book = Book(title, author, price, stock)
        books.append(new_book)
        print(f'Added "{title}" to inventory.')
    except ValueError:
        print("Invalid input. Price must be a number, stock must be an integer.")

def search_book(books):
    term = input("Enter title or author to search: ")
    found = False
    for book in books:
        if term.lower() in book.title.lower() or term.lower() in book.author.lower():
            print(book)
            found = True
    if not found:
        print("No books found matching that search term.")
