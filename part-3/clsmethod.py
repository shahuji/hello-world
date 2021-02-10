from datetime import date


class Student:

    # this = 'self'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def byYear(cls, name, year):
        return cls(name, date.today().year - year)

    @staticmethod
    def isAdult(age):
        return True if age > 18 else False


if __name__ == '__main__':
    student = Student
    stu1 = Student("Vishal", 22)
    stu2 = Student.byYear("Punit", 1999)  # using classmethod to create object
    stu3 = stu1.byYear("Shahuji", 1956)  # using existing object with class methd to create another object
    print(student.__name__)

    print(stu1.age)
    print(stu3.age)

    print(Student.isAdult(23))
