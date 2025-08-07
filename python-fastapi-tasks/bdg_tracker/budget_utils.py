import json
import os
from transaction import Transaction

FILE_NAME = 'budget_data.json'

def save_transactions(transactions):
    try:
        with open(FILE_NAME, 'w') as file:
            json.dump([t.__dict__ for t in transactions], file, indent=4)
        print("Transactions saved.")
    except IOError:
        print("Error: Could not save transactions.")

def load_transactions():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, 'r') as file:
                transactions_data = json.load(file)
                return [Transaction(**data) for data in transactions_data]
        except (IOError, json.JSONDecodeError):
            print("Error: Could not load data from file.")
    return []

def group_by_category(transactions):
    grouped = {}
    for t in transactions:
        if t.category not in grouped:
            grouped[t.category] = 0
        grouped[t.category] += t.amount
    return grouped