import sqlite3
from error_handling import int_checker, input_checker

class Student:
    def __init__(self, first_name, last_name, course):
        self.first_name = first_name
        self.last_name = last_name
        self.course = course
        
class StudentRecordSystem:
    def __init__(self, db_name = "students.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor() # Runs SQL  
# If there is not table create it.     
        self.cursor.execute(""" 
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                firstname TEXT,
                lastname TEXT,
                course TEXT
                )
            """)
        
        self.conn.commit() # Peforming the action.
    
    def add_students(self):
        loop = int_checker("How many students would you like to add?: ")
        for i in range(loop):
            first_name = input_checker("Enter First Name: ")
            last_name = input_checker("Enter Last Name: ")
            course = input_checker("Enter the course their in: ")
            
            student_class_data = Student(first_name, last_name, course)
        
            print("-" * 50)
            print(f"You have added {student_class_data.first_name} {student_class_data.last_name} and their in {student_class_data.course}")
            print("-" * 50)
# Writing data too SQL database        
            self.cursor.execute(
                """
                INSERT INTO students (firstname, lastname, course)          
                VALUES (?, ?, ?)
                """,
                    (
                    student_class_data.first_name,
                    student_class_data.last_name,
                    student_class_data.course   
                                ))
            
            self.conn.commit() # Confirm changes
# Selecting the rows   
    def remove_students(self):
        print("Current Students")
        self.cursor.execute(
            """
            SELECT * FROM students
            """)
# Get all rows selected.
        students_sql_data = self.cursor.fetchall()
# Checks if it is empty        
        if not students_sql_data:
            print("No Data Found.")
            return
# Go through each line of data.        
        for students in students_sql_data:
            print(f"ID: {students[0]} | {students[1]} {students[2]} | Course(s): {students[3]} ")
        
        id_index_delete = int_checker("Choose by the ID of what student you want to remove: ")
# Deletes Student      
        self.cursor.execute(
            """
            DELETE FROM students WHERE id = ?
            """,
            (id_index_delete)
            )
# Checks if rowcount has changed to see if data changed
        if self.cursor.rowcount == 0:
            print("No Student Found with that ID")
        else:
            print("Successfully deleted")
        
        self.conn.commit() #Confirm Changes.
        
    def view_students(self):
        self.cursor.execute(
            """
            SELECT * FROM students
            """
        )
        
        student_sql_data = self.cursor.fetchall() # Takes all Data
        if not student_sql_data:
            print("No Data Found.")
            return
        
        for students in student_sql_data:
            print(f"ID: {students[0]} | {students[1]} {students[2]} | Course(s): {students[3]}")
            
        
        
