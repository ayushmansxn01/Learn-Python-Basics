import time

k=0
n=0
t=time.time()
print(t)
while(k<45):
    n=n+1
    k=k+1
print("time is ", time.time() - t, "seconds")
t=time.time()
print(t)
for k in range(45):
    n=n+1
print("time is ", time.time()-t, "seconds")

for k in range(2):
    if k==0:
        print("buddy  !!!")
    time.sleep(1)
    print("love the way you lie :) 😊")

localtime=time.asctime(time.localtime(time.time()))

print(localtime)