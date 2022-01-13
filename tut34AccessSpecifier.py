class employee:
    leaves = 8
    var = 7
    _protec = 9         #protected
    __pr = 98           #private

    def __init__(self, name, age, nick):
        self.name = name
        self.age = age
        self.nick = nick


#class prof:
    #leaves = 15
    #def __init__(self, college, degree):
     #   self._college = college  # protected attribute
     #   self.__degree = degree  # private attribute
     #   leaves = 15

har = employee("Larry", 52, "vhunnu")
print(har.leaves)
#print(harry._employee_fruit)
print(har._employee__pr)            #private
print(har.var)
print(har._protec)                  #protected


