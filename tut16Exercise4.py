a=int(input("enter 0 for upside down else 1 : "))
n=int(input("enter the number of rows : "))
a=bool(a)
if (a==True):
    for i in range(n,0,-1):
        print("*"*i)
else:
    for i in range(1,n+1):
          print("*"*i)

