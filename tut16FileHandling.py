f=open("tut15filehandling.txt")
print(f.readline())
print(f.tell())
print(f.readline())
print(f.tell())
print(f.readline())
print(f.tell())
f.seek(26)
print(f.readline())
print(f.readline())
f.close()
