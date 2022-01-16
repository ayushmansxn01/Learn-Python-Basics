#if you want to change something after it has been declared without using functions
# and treating them as variable rather than functions as in this case "email"

class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@codewithharry.com"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname == None or self.lname == None:
            return "Email is not set. Please set it using setter"
        return f"{self.fname}.{self.lname}@gmail.com"

    @email.setter
    def email(self,string):
        names=string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

har=Employee("Harry","Bhaiya")
print(har.email)
har.fname="love"
har.lname="Babbar"
print(har.email)





