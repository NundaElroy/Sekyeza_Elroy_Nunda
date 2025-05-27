# Base class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

# Child classes 
class Student(Person):
    def __init__(self, name, age, student_id, course):
        super().__init__(name, age)  # Call parent constructor
        self.student_id = student_id
        self.course = course
    
    def display_info(self):
        super().display_info()  # Call parent method
        print(f"Student ID: {self.student_id}")
        print(f"Course: {self.course}")
        print("Role: Student")

class Lecturer(Person):
    def __init__(self, name, age, employee_id, department):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.department = department
    
    def display_info(self):
        super().display_info()
        print(f"Employee ID: {self.employee_id}")
        print(f"Department: {self.department}")
        print("Role: Lecturer")

class Staff(Person):
    def __init__(self, name, age, employee_id, position):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.position = position
    
    def display_info(self):
        super().display_info()
        print(f"Employee ID: {self.employee_id}")
        print(f"Position: {self.position}")
        print("Role: Staff")


if __name__ == "__main__":
  
    student = Student("Kyaga How", 20, "23/U/1379", "Computer Science")
    lecturer = Lecturer("Dr. Mark Magumba", 45, "BSSE2020", "Mathematics")
    staff = Staff("Kyeyune Born", 35, "ST111", "Admin Assistant")
    
    # Display information
    print("=== STUDENT INFO ===")
    student.display_info()
    
    print("\n=== LECTURER INFO ===")
    lecturer.display_info()
    
    print("\n=== STAFF INFO ===")
    staff.display_info()