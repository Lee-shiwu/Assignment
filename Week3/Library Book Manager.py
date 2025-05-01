class Library:
    def __init__(self):
        self.books=[]
    def add_book(self,book_name):
        self.books.append(book_name)
        print(f"✅ Book '{book_name}'added successfully.\n")
    def show_book(self):
        if not self.books:
             print("📚 No books in the library.\n")
        else:
            print("📖 List of books in the library:")
            for i, book_name in enumerate(self.books,start=1):
                print(f"{i}. {book_name}")
            print()
library=Library()
while True:
    print("📚 Library Manager")
    print("1. Add a book")
    print("2. Show all books")
    print("3. Exit")
    case = input("Choose an option (1-3): ")
    if case=='1':
        name=input("Enter book's name: ")
        library.add_book(name)
    elif case=='2':
        library.show_book()
    elif case=='3':
        print("BYE!!")
        break
    else:
        print("❌ Invalid option. Please try again.\n")
    