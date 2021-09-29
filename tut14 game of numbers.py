n=15
ct=5
while(ct!=0 ):
    ct=ct-1
    a=int(input("enter a number : "))
    if(a==n):
        print("you won ")
        print("you took", 5-ct, "attempts")
        break
    if(a<n):
        print("try a bigger number")
        print(ct," Attempts left")
    if(a>n):
        print("try a smaller number")
        print(ct, " Attempts left")
    else:
        print("enter a valid number")