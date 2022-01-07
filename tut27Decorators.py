def fun1():
    print("hello")
fun2=fun1
del fun1
fun2()

def fun3(fun):
    fun("This is while using print function")
fun3(print)

def dec(fun):
    def funx():
        print("Executing")
        fun()
        print("executed")
    return funx


def who_am_I():
    print("Ayush is a very hardworking boy")

who_am_I=dec(who_am_I)
who_am_I()

#another method of writing "who_am_I=dec(who_am_I)" using @
@dec
def who_am_I():
    print("Ayush is a very hardworking boy")

#printing
who_am_I()