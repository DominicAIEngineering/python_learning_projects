import sqlite3

def create_connection():
    conn = sqlite3.connect('school.db')
    cursor = conn.cursor()
    return conn, cursor

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            department TEXT,
            matric_number TEXT
        )
        ''')
    conn.commit()

def add_student(cursor, conn):
    name = input("Enter student name: ")
    try:
        age = int(input("Enter student age: "))
        if age <= 0 or age > 120:
            print("Invalid age")
            return
    except ValueError:
        print("Invalid age! Please enter a number.")
        return
    department = input("Enter student department: ")
    matric_number = input("Enter student matric number: ")

    cursor.execute('''
        INSERT INTO students (name, age, department, matric_number)
        VALUES (?,?,?,?)
        ''', (name, age, department, matric_number))

    conn.commit()
    print("Student added successfully!")

def view_students(cursor):
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    for student in students:
        print(student)

def search_student(cursor):
    matric_number = input("Enter matric number: ")

    cursor.execute("""SELECT * FROM students WHERE matric_number = ?""",
                   (matric_number,))
    student = cursor.fetchone()

    if student:
        print("Student found!")
        print(student)
    else:
        print("Student not found!")

def update_student(cursor, conn):
    student_id = int(input("Enter student ID: "))
    new_department = input("Enter new department: ")

    cursor.execute("""UPDATE students 
    SET department = ? WHERE id = ?""",
    (new_department, student_id))
    conn.commit()

    if cursor.rowcount > 0:
        print("Student updated successfully!")
    else:
        print("Student not found!")

def delete_student(cursor, conn):
    student_id = int(input("Enter student ID: "))

    cursor.execute("""DELETE FROM students WHERE id = ?""",
                   (student_id,)
                   )
    conn.commit()

    if cursor.rowcount > 0:
        print("Student deleted successfully!")
    else:
        print("Student not found!")

def exit_programme():
    print("Thank you for using this program! Goodbye!")

def main(cursor, conn):
    while True:
        print("\n===========STUDENT MANAGEMENT SYSTEM==========")
        print("=======")
        print("""
            1. Add student
            2. View students
            3. Search students
            4. Update student
            5. Delete student
            6. Exit""")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                add_student(cursor, conn)

            elif choice == 2:
                view_students(cursor)

            elif choice == 3:
                search_student(cursor)

            elif choice == 4:
                update_student(cursor, conn)

            elif choice == 5:
                delete_student(cursor, conn)

            elif choice == 6:
                print("Goodbye!")
                break

            else:
                print("Invalid choice! Please choose from 1-6")

        except ValueError:
            print("Invalid choice! Please choose a numeric value from 1-6")

if __name__ == "__main__":
    conn, cursor = create_connection()
    try:
        main(cursor, conn)
    finally:
        conn.close()