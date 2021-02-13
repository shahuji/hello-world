# Python Basics
# Basic Template tags
# Models
# Views

class Stud:
    leave = 2

    # def __init__(self):
    #     pass

    def __init__(self, aname, asalary, arole, leave):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.leave = leave

    def detail(self):
        """ Class name is STUDENT. Holds simple attributes. Basic information class """
        return f"The name is {self.name} and the salary is {self.salary}. The role is {self.role}. " \
               f"No. of leaves are {self.leave}. "

    @classmethod
    def scls(cls, nleaves):
        cls.leave = nleaves

    @classmethod
    def gcls(cls):
        print(cls.leave)
        return 0


s1 = Stud("Vishal", "15000", "Developer", 3)
# s1.leave = 3
s1.role = "Python Developer"
s1.gcls()
s1.scls(5)
s1.gcls()
s3 = Stud
print(s1.detail.__doc__)
# print(Stud.__dict__)
print(s1.detail())

print(s1.__dict__)
print(Stud.__basicsize__)
# print(s2.leave)
