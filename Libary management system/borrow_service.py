from storage import books, issued_records
from books import find_book_by_id
from users import find_user_by_id

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
    while i < len(issued_records):
        rec = issued_records[i]
        if rec["student_id"] == student_id and rec["book_id"] == book_id:
            print("Error: Student already borrowed this book!")
            return False
        i = i + 1

    book["quantity"] = book["quantity"] - 1
    record = {
        "student_id": student_id,
        "book_id": book_id,
        "days_issued": days
    }
    issued_records.append(record)
    print("Success: Book issued successfully to", user["name"])
    return True

def calculate_fine(days_issued):
    allowed_days = 14
    fine_per_day = 5
    
    if days_issued > allowed_days:
        extra_days = days_issued - allowed_days
        return extra_days * fine_per_day
    else:
        return 0

def return_book(student_id, book_id):
    found_index = -1
    i = 0
    while i < len(issued_records):
        rec = issued_records[i]
        if rec["student_id"] == student_id and rec["book_id"] == book_id:
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