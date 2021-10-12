d1={"Ayush":"paneer", "kirti":"rosagulla", "Aru":{"morning":"Pasta", "afternoon":"Dal Roti", "Evening":"Mummy aaj kuch accha banao !!"}}
print(d1)
print(type(d1))
print(d1["Aru"])
print(d1["Aru"]["afternoon"])
print(d1.items())
d2=d1.copy()
d2["Ayush"]="Butter chicken"
print("new")
print(d1)
print(d2)

