from abc import ABC, abstractmethod

class A(ABC):
    def __init__(self):
        pass

    def print(self, a):
        out = self.compute(a)
        print(out)

    @abstractmethod
    def compute(self, a):
        pass

class B(A):
    def compute(self, a):
        return a + 1

class C(B):
    def compute(self, a):
        return a + 2

if __name__ == "__main__":
    c = C()
    c.print(0)
