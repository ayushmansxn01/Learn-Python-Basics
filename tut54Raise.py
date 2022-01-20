a=input("what is your name")
b=input("how much do you earn")
if int(b)==0:
    raise  ZeroDivisionError("b is 0 so process stopped")
if a.isnumeric():
    raise  Exception("Numbers are not allowed")

print(f"Hello  {a}")

