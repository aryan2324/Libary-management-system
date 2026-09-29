from storage import books

def list_all_books():
    print("\n--- Available Books ---")
    if len(books) == 0:
        print("No books available in the library.")
        return
    
    i = 0
    while i < len(books):
        book = books[i]
        print("ID:", book["id"], "| Title:", book["title"], "| Author:", book["author"], "| Quantity:", book["quantity"])
        i = i + 1

def find_book_by_id(book_id):
    i = 0
    while i < len(books):
        if books[i]["id"] == book_id:
            return books[i]
        i = i + 1
    return None

def add_new_book(book_id, title, author, quantity):
    existing = find_book_by_id(book_id)
    if existing != None:
        print("Error: Book ID already exists!")
        return False
    
    new_book = {
        "id": book_id,
        "title": title,
        "author": author,
        "quantity": quantity
    }
    books.append(new_book)
    print("Success: Book added successfully!")
    return True