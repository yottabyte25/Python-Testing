import tkinter as tk

class School:
   def __init__(self, total):
      self.total = total

   def get_total(self):
      return self.total

   def add(self):
      for total in self.total:
         total.get_total += 1

s = School(0)

class Student:
   def __init__(self, name, age, grade):
      self.name = name
      self.age = age
      self.grade = grade
   
class Course:
   def __init__(self, subject, students, max_students):
      self.subject = subject
      self.students = students
      self.max_students = max_students

root = tk.Tk()

def Choose():
   pass

root.mainloop()