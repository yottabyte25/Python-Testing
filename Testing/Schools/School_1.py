class School1:
    def __init__(self, rating, total):
        self.rating = rating
        self.total = total

    def get_total(self):
        return self.total
    
    def get_rating(self):
        return self.rating
    
    def add(self):
        for total in self.total:
            total.get_total() + 1

s = School1(4.5, 400)
s.add()
print(s.total)

class S1_Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def get_grade(self):
        return self.grade

class S1_course_1:
    def __init__(self, subject, students, max_students):
        self.subject = "Math"
        self.students = 4
        self.max_students = 10
    
    def get_subject(self):
        return self.subject
    
    def get_students(self):
        return self.students
    
    def get_max_students(self):
        return self.max_students

class S1_course_2:
    def __init__(self, subject, students, max_students):
        self.subject = "Science"
        self.students = 6
        self.max_students = 10

    def get_subject(self):
        return self.subject
    
    def get_students(self):
        return self.students
    
    def get_max_students(self):
        return self.get_max_students