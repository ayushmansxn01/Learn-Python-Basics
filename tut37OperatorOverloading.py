class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    def __add__(self, other):
        return self.salary+other.salary

    def __floordiv__(self, other):
        return self.salary - other.salary

    def __truediv__(self, other):
        return self.salary/other.salary

har=Employee("harry", 472, "programmer")
lar=Employee("larry", 77, "programmer")
print(har/lar)