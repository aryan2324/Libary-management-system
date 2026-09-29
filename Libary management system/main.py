
books = [
    {"id": "C001", "title": "Calculus", "author": "B.S.Grewal", "quantity": 3},
    {"id": "D001", "title": "Data Structures", "author": "Alice Bob", "quantity": 2},
    {"id": "W001", "title": "Web Development", "author": "Carol David", "quantity": 1},
    {"id": "D002", "title": "Database Systems", "author": "Eve Frank", "quantity": 4}
]

users = [
    {"id": "bcy60", "name": "Divyanshu KL", "role": "student"},
    {"id": "bai69", "name": "Pratyush", "role": "student"},
    {"id": "A1", "name": "Admin User", "role": "admin"}
]

issued_records = [
    {"student_id": "bcy60", "book_id": "D001", "days_issued": 20},
    {"student_id": "bai69", "book_id": "W001", "days_issued": 16}
]



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
    clean_id = book_id.strip().lower()
    while i < len(books):
        if books[i]["id"].strip().lower() == clean_id:
            return books[i]
        i = i + 1
    return None

def add_new_book(book_id, title, author, quantity):
    existing = find_book_by_id(book_id)
    if existing != None:
        print("Error: Book ID already exists!")
        return False
    
    new_book = {
        "id": book_id.strip(),
        "title": title.strip(),
        "author": author.strip(),
        "quantity": quantity
    }
    books.append(new_book)
    print("Success: Book added successfully!")
    return True


def find_user_by_id(user_id):
    i = 0
    clean_id = user_id.strip().lower()
    while i < len(users):
        if users[i]["id"].strip().lower() == clean_id:
            return users[i]
        i = i + 1
    return None

def register_student(user_id, name):
    existing = find_user_by_id(user_id)
    if existing != None:
        print("Error: Student ID already exists!")
        return False
    
    new_user = {
        "id": user_id.strip(),
        "name": name.strip(),
        "role": "student"
    }
    users.append(new_user)
    print("Success: Student registered successfully!")
    return True

def list_all_students():
    print("\n--- Registered Students ---")
    i = 0
    while i < len(users):
        u = users[i]
        if u["role"] == "student":
            print("ID:", u["id"], "| Name:", u["name"])
        i = i + 1


def issue_book(student_id, book_id, days):
    user = find_user_by_id(student_id)
    if user == None:
        print("Error: Student ID not found!")
        return False
    
    book = find_book_by_id(book_id)
    if book == None:
        print("Error: Book ID not found!")
        return False
    
    if book["quantity"] <= 0:
        print("Error: Book is currently out of stock!")
        return False
    
    
    i = 0
    s_id_clean = student_id.strip().lower()
    b_id_clean = book_id.strip().lower()
    while i < len(issued_records):
        rec = issued_records[i]
        if rec["student_id"].strip().lower() == s_id_clean and rec["book_id"].strip().lower() == b_id_clean:
            print("Error: Student already borrowed this book!")
            return False
        i = i + 1

    book["quantity"] = book["quantity"] - 1
    record = {
        "student_id": user["id"],
        "book_id": book["id"],
        "days_issued": days
    }
    issued_records.append(record)
    print("Success: Book issued successfully to", user["name"])
    return True

def calculate_fine(days_issued):
    allowed_days = 14
    fine_per_day = 5
    if days_issued > allowed_days:
        return (days_issued - allowed_days) * fine_per_day
    return 0

def return_book(student_id, book_id):
    found_index = -1
    i = 0
    s_id_clean = student_id.strip().lower()
    b_id_clean = book_id.strip().lower()
    while i < len(issued_records):
        rec = issued_records[i]
        if rec["student_id"].strip().lower() == s_id_clean and rec["book_id"].strip().lower() == b_id_clean:
            found_index = i
            break
        i = i + 1

    if found_index == -1:
        print("Error: No active loan found for this student and book!")
        return False

    record = issued_records[found_index]
    fine = calculate_fine(record["days_issued"])
    
    book = find_book_by_id(book_id)
    if book != None:
        book["quantity"] = book["quantity"] + 1

    issued_records.pop(found_index)
    
    print("Success: Book returned.")
    if fine > 0:
        print("Late Fine Due: Rs.", fine)
    else:
        print("No fine incurred. Thank you!")
    return True

def list_issued_books():
    print("\n--- Currently Issued Books ---")
    if len(issued_records) == 0:
        print("No books are currently issued.")
        return

    i = 0
    while i < len(issued_records):
        rec = issued_records[i]
        fine = calculate_fine(rec["days_issued"])
        print("Student:", rec["student_id"], "| Book:", rec["book_id"], "| Days Kept:", rec["days_issued"], "| Fine: Rs.", fine)
        i = i + 1


def display_menu():
    print("\n==================================")
    print(" LIBRARY MANAGEMENT SYSTEM ")
    print("==================================")
    print("1. View All Books")
    print("2. Add New Book")
    print("3. Register New Student")
    print("4. View All Students")
    print("5. Issue Book to Student")
    print("6. Return Book")
    print("7. View Issued Records & Fines")
    print("8. Exit")

def run():
    running = True
    while running:
        display_menu()
        choice = input("Enter option (1-8): ").strip()
        
        if choice == "1":
            list_all_books()

        elif choice == "2":
            b_id = input("Enter Book ID: ")
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")
            qty_input = input("Enter Quantity: ")
            if qty_input.isdigit():
                add_new_book(b_id, title, author, int(qty_input))
            else:
                print("Error: Quantity must be a number.")

        elif choice == "3":
            s_id = input("Enter Student ID: ")
            s_name = input("Enter Student Name: ")
            register_student(s_id, s_name)

        elif choice == "4":
            list_all_students()

        elif choice == "5":
            s_id = input("Enter Student ID: ")
            b_id = input("Enter Book ID: ")
            days_input = input("Enter number of days book was kept: ")
            if days_input.isdigit():
                issue_book(s_id, b_id, int(days_input))
            else:
                print("Error: Days must be a number.")

        elif choice == "6":
            s_id = input("Enter Student ID: ")
            b_id = input("Enter Book ID: ")
            return_book(s_id, b_id)

        elif choice == "7":
            list_issued_books()

        elif choice == "8":
            print("Exiting Library Management System. Goodbye!")
            running = False

        else:
            print("Invalid selection! Please enter a number between 1 and 8.")

if __name__ == "__main__":
    run()