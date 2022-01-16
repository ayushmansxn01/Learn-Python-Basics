class A:
    def met(self):
        print("From class A")

class B(A):
    def met(self):
        print("From class B")

class C(A):
    def met(self):
        print("From class C")

class D(B,C):
        pass

a = A()
b = B()
c = C()
d = D()
print(d.met())