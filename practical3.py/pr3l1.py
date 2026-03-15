def input_student_id():
    while True:
        sid = input("Enter student ID: ").strip()
        if sid:
            return sid
        print("Student ID cannot be empty.")

def input_non_empty(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty.")

def add_student(students):
    print("\n--- Add Student ---")
    sid = input_student_id()
    existing = next((s for s in students if s['id'] == sid), None)
    if existing:
        print(f"Student with ID {sid} already exists.")
        return
    name = input_non_empty("Enter student name: ")
    age = input_non_empty("Enter student age: ")
    grade = input_non_empty("Enter student grade: ")
    students.append({'id': sid, 'name': name, 'age': age, 'grade': grade})
    print("Student added successfully.")

def view_students(students):
    print("\n--- Student List ---")
    if not students:
        print("No students found.")
        return
    print(f"{'ID':<10}{'Name':<20}{'Age':<6}{'Grade':<8}")
    print('-' * 45)
    for s in students:
        print(f"{s['id']:<10}{s['name']:<20}{s['age']:<6}{s['grade']:<8}")

def update_student(students):
    print("\n--- Update Student ---")
    sid = input_student_id()
    student = next((s for s in students if s['id'] == sid), None)
    if not student:
        print(f"Student with ID {sid} not found.")
        return
    print(f"Current name: {student['name']}")
    new_name = input("Enter new name (leave blank to keep current): ").strip()
    if new_name:
        student['name'] = new_name
    print(f"Current age: {student['age']}")
    new_age = input("Enter new age (leave blank to keep current): ").strip()
    if new_age:
        student['age'] = new_age
    print(f"Current grade: {student['grade']}")
    new_grade = input("Enter new grade (leave blank to keep current): ").strip()
    if new_grade:
        student['grade'] = new_grade
    print("Student updated successfully.")

def delete_student(students):
    print("\n--- Delete Student ---")
    sid = input_student_id()
    index = next((i for i, s in enumerate(students) if s['id'] == sid), None)
    if index is None:
        print(f"Student with ID {sid} not found.")
        return
    students.pop(index)
    print("Student deleted successfully.")

def search_students(students):
    print("\n--- Search Students ---")
    query = input_non_empty("Enter student name or ID to search: ")
    query_lower = query.lower()
    results = [s for s in students if query_lower in s['id'].lower() or query_lower in s['name'].lower()]
    if not results:
        print("No students matched your search.")
        return
    print(f"Found {len(results)} student(s):")
    print(f"{'ID':<10}{'Name':<20}{'Age':<6}{'Grade':<8}")
    print('-' * 45)
    for s in results:
        print(f"{s['id']:<10}{s['name']:<20}{s['age']:<6}{s['grade']:<8}")

def student_manager():
    students = []
    while True:
        print("\n=== Student Manager ===")
        print("1. Add student")
        print("2. View students")
        print("3. Update student")
        print("4. Delete student")
        print("5. Search students")
        print("6. Back to main menu")
        choice = input("Select an option: ").strip()
        if choice == '1':
            add_student(students)
        elif choice == '2':
            view_students(students)
        elif choice == '3':
            update_student(students)
        elif choice == '4':
            delete_student(students)
        elif choice == '5':
            search_students(students)
        elif choice == '6':
            return
        else:
            print("Invalid choice. Please choose 1-6.")

def inventory_operations():
    print("\n=== Inventory Shop Item Operations ===")
    raw = input("Enter item numbers separated by spaces or commas: ").strip()
    if not raw:
        print("No items entered.")
        return
    items = []
    for part in raw.replace(',', ' ').split():
        if part.strip().isdigit():
            items.append(int(part.strip()))
        else:
            print(f"Ignoring invalid input '{part}'.")
    if not items:
        print("No valid item numbers found.")
        return

    print(f"a) Total number of items: {len(items)}")
    print(f"b) Last item number: {items[-1]}")
    sorted_items = sorted(items)
    print(f"c) Sorted items: {sorted_items}")
    contains_515 = 'Yes' if 515 in items else 'No'
    print(f"d) Contains item 515? {contains_515}")
    items.extend([121, 321])
    items = sorted(items)
    print(f"e) Added 121 and 321, sorted updated list: {items}")


def main():
    while True:
        print("\n=== Main Menu ===")
        print("1. Student manager")
        print("2. Inventory shop operations")
        print("3. Exit")
        choice = input("Select an option: ").strip()
        if choice == '1':
            student_manager()
        elif choice == '2':
            inventory_operations()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose 1-3.")


if __name__ == '__main__':
    main()
