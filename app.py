class A():
    def a(self):
        print("I am in A section")
class B(A):
    def a(self):
        print("I am in B section")
class C(A):
    pass
    # def a(self):
        # print("I am in C section")
class D(C,B):
    pass
    # def a(self):
    #     print("I am in D section")
e=A()
b=B()
c=C()
d=D()
d.a()