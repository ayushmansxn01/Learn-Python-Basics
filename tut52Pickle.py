import pickle

cars=["Harley Davidson", "Arley Shevidson"]
file="mycar.pkl"
fileobj=open(file,'wb')
pickle.dump(cars, fileobj)
fileobj.close()

file="mycar.pkl"
fileobj=open(file,'rb')
mycar=pickle.load(fileobj)
print(mycar)
