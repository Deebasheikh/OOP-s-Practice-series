# multiple inheritance
class A:
    def show(self):
        return "hello from A"
class B(A):
    def show(self):
        return "hello from B"
class C(A):
    def show(self):
        return "hello from C"
class D(B,C):
    pass     
# instantiation (create an instance)
d = D()    
print(D.mro())
print(d.show())
