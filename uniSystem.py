## create a university system display information of 
## classes: person(parent), and subclasses student and lecturer,staff.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, student_id, major):
        super().__init__(name, age)
        self.student_id = student_id
        self.major = major
    def display_info(self):
        super().display_info()
        print(f"Student ID: {self.student_id}, Major: {self.major}")

class Lecturer(Person):
    def __init__(self, name, age, lecturer_id, department):
        super().__init__(name, age)
        self.lecturer_id = lecturer_id
        self.department = department
    def display_info(self):
        super().display_info()
        print(f"Lecturer ID: {self.lecturer_id}, Department: {self.department}")

class Staff(Person):
    def __init__(self, name, age, staff_id, position):
        super().__init__(name, age)
        self.staff_id = staff_id
        self.position = position
    def display_info(self):
        super().display_info()
        print(f"Staff ID: {self.staff_id}, Position: {self.position}")

# Example usage:
if __name__ == "__main__":
    s = Student("Armand", 20, "S123", "Software Engineering")
    l = Lecturer("Dr. jeff", 45, "L456", "Python Programming")
    st = Staff("abdel", 35, "ST789", "Administrator")
    print("Student Info:")
    s.display_info()
    print("\nLecturer Info:")
    l.display_info()
    print("\nStaff Info:")
    st.display_info()
