#if a abstract class is defined, it will be compulsary for the class inheriting that class to define that abstract function


from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def printarea(self):
        return 0
class B(A):
    def printarea(self):
        print("66")

a=B()
print(a.printarea())
