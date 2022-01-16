class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@codewithharry.com"
skillf = Employee("Skill", "F")


import inspect
print(inspect.getmembers(skillf))