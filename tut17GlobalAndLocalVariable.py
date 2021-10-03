a=55
def function1():
    a=5
    print(a)
    global a
    a=55
    print(a)
def fun2():
    x=9
    def fun3():
        global x
        x=7
    fun3()
    print(x)
fun2()
print(x)