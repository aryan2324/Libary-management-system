# Library Management System

## Project Description
This is a simple console-based Library Management System written in Python. It lets a librarian manage books and students, issue books, return books, and calculate late fines. It is a first-year B.Tech CSE project made to practise basic Python concepts.

## Problem Statement
In many small libraries, records of books and students are still kept by hand. This makes it slow to check which books are available, who has borrowed a book, and how much fine is due. This project tries to solve this in a simple way using a menu-driven Python program.

## Objectives
- To practise lists, dictionaries, functions, loops and conditions in Python
- To build a menu-driven program that takes user input
- To manage books and students in one program
- To calculate late fines automatically
- To organise code into separate functions

## Features
- View all books with ID, title, author and quantity
- Add a new book (duplicate book IDs are not allowed)
- Register a new student (duplicate student IDs are not allowed)
- View all registered students
- Issue a book to a student
  - checks that the student ID and book ID exist
  - checks that the book is in stock
  - does not allow the same student to borrow the same book twice
- Return a book (quantity goes back up by 1)
- View all currently issued books along with the fine for each
- Fine calculation: Rs. 5 per day after 14 days
- IDs are not case-sensitive and extra spaces are removed (e.g. "c001" and " C001 " both work)
- Basic input checks: quantity and days must be numbers

## Technologies Used
- Python 3
- Only basic Python (lists, dictionaries, functions, while loops, if/else, input/print)
- No external libraries

## How the Program Works
1. The program starts and shows a menu with 8 options.
2. The user types a number (1-8) to choose an option.
3. The program asks for the needed details (for example, student ID and book ID) and runs the matching function.
4. After each action it shows the menu again, until the user chooses option 8 (Exit).

Data is stored in Python lists of dictionaries:
- `books` - id, title, author, quantity
- `users` - id, name, role
- `issued_records` - student_id, book_id, days_issued

Some sample books and students are already added at the start of the program so it can be tested easily.

**Project files**
- `main.py` - the complete working program (run this file)
- `storage.py`, `books.py`, `users.py`, `borrow_service.py` - the same code split into separate modules. These are not connected to `main.py` yet.

## How to Run the Project
1. Install Python 3 on your computer.
2. Download or clone this project folder.
3. Open a terminal in the project folder.
4. Run:
   ```
   python main.py
   ```
5. Follow the menu on the screen.

## Sample Usage
```
==================================
 LIBRARY MANAGEMENT SYSTEM
==================================
1. View All Books
2. Add New Book
3. Register New Student
4. View All Students
5. Issue Book to Student
6. Return Book
7. View Issued Records & Fines
8. Exit
Enter option (1-8): 7

--- Currently Issued Books ---
Student: bcy60 | Book: D001 | Days Kept: 20 | Fine: Rs. 30
Student: bai69 | Book: W001 | Days Kept: 16 | Fine: Rs. 10
```

Returning a book:
```
Enter option (1-8): 6
Enter Student ID: bcy60
Enter Book ID: D001
Success: Book returned.
Late Fine Due: Rs. 30
```

## Future Improvements
- Save data in a file (like a text or CSV file), because right now all data is lost when the program closes
- Use the separate module files (`books.py`, `users.py`, etc.) properly from `main.py` instead of keeping everything in one file
- Use real dates (issue date and return date) instead of typing the number of days manually
- Add login for the admin and students (the admin user exists in the data but has no special access yet)
- Add options to search, update and delete books
- Add unit tests
- Add a limit on how many books one student can borrow

## Author
Aryan Gupta
B.Tech CSE (1st Year), VIT
Registration Number: 26BCE10854
