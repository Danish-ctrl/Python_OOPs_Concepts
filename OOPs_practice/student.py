class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def info(self):
        print(f"Name of the student is {self.name}, his age is {self.age} and his grades are {self.grades}")


s = Student('Danish', 28, 2.1)
s.info()