class Student:
    lassof=2021
    pass
ayu=Student();
ayu.name="Ayushman Saxena" #instance variable: properties of object and not inheriteed from class
ayu.grade="A+"
ayu.lassof=2022
print(ayu.lassof)
print(Student.lassof)
Student.lassof=2037
print(ayu.name, "has grade :",ayu.grade)
print(Student.lassof)