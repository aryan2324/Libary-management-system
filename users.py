from storage import users

def find_user_by_id(user_id):
    i = 0
    while i < len(users):
        if users[i]["id"] == user_id:
            return users[i]
        i = i + 1
    return None

def register_student(user_id, name):
    existing = find_user_by_id(user_id)
    if existing != None:
        print("Error: Student ID already exists!")
        return False
    
    new_user = {
        "id": user_id,
        "name": name,
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