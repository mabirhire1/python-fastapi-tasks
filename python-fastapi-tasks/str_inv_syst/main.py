from inventory import add_book, save_inventory, load_inventory, search_book

def main():
    books = load_inventory()
    
    while True:
        print("\nBookstore Inventory System")
        print("..........................")
        print("\n1. Add a new book")
        print("2. Search for a book")
        print("3. View all books")
        print("4. Save & Exit")
        choice = input("\nEnter your choice: ")
        
        if choice == '1':
            add_book(books)
        elif choice == '2':
            search_book(books)
        elif choice == '3':
            if not books:
                print("Inventory is empty.")
            else:
                for book in books:
                    print(book)
        elif choice == '4':
            save_inventory(books)
            print("\nExiting.......")
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == '__main__':
    main()