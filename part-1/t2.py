class cc:
    salary = 0

    def __init__(self, salary, name, age):
        self.salary = salary
        self.name = name
        self.age = age

    def __add__(self, other):
        return self.salary + other.salary


c1 = cc(20, 'Vishal', 22)

c2 = cc(30, 'Shahu', 42)

print("Total salary paided is: ", c1 + c2)
print("Age total is: ", c1.age + c2.age)
