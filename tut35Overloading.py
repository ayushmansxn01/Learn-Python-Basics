class A:
    var1 = "Class A class variable "
    def __init__(self):
        self.var1 = "instance variable from class A"
        self.var2 = "can be used using super if class b object is there"

class B(A):
    var1 = "Class B variable"
    def __init__(self):

        self.var1 = "instance variable in class b"
        super().__init__()



har=B()
print(har.var1)
print(har.var2)
  