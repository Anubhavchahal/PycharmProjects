class A:
    def displayA(self):
        print("Welcome to Wscubetech A")

class B(A):
    def displayB(self):
        print("Welcome to IITP B")

class C(B):
    def displayC(self):
        print("Welcome to CVR ")

obj=C()
obj.displayA()
obj.displayB()
obj.displayC()

class A:
    def displayA(self):
        print("Welcome to Wscubetech A")

class B:
    def displayB(self):
        print("Welcome to IITP B")

class C(A,B): # multiple inheritence
    def displayC(self):
        print("Welcome to CVR ")

obj=C()
obj.displayA()
obj.displayB()
obj.displayC()