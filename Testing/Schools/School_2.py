class School2:
    def __init__(self, rating, total):
        self.rating = 3.8
        self.total = 780
    
    def get_total(self):
        return self.total
    
    def get_rating(self):
        return self.rating

class S2_Student:
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

class S2_Course_1:
    def __init__(self, subject, students, max_students):
        self.subject = "Language Arts"
        self.students = 20
        self.max_students = 30

    def get_subject(self):
        return self.subject
    
    def get_students(self):
        return self.students
    
    def get_max_students(self):
        return self.max_students
    
class S2_Course_2:
    def __init__(self, subject, students, max_students):
        self.subject = "Literature"
        self.students = 50
        self.max_students = 100
    
    def get_subject(self):
        return self.subject
    
    def get_students(self):
        return self.students
    
    def get_max_students(self):
        return self.max_students
