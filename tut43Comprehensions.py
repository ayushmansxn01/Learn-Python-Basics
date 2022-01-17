#ls=[]
#for i in range(100):
#       if i%3==0:
#           ls.append(i)

ls=[i for i in range(100) if i%3==0]
print(ls)

dict1={i:f"item{i}" for i in range(1,1002) if i%7==0}
print(dict1)