class College:
    def __init__(self):
        self.students = []
        self.courses = []
    
    def add_student(self, name): self.students.append(name)
    def add_course(self, course): self.courses.append(course)
    
    def view_students(self): print("Students:", self.students)
    def view_courses(self): print("Courses:", self.courses)

cms = College()
cms.add_student("Alice")
cms.add_student("Bob")
cms.add_course("Math 101")
cms.add_course("CS 101")
cms.view_students()
cms.view_courses()
