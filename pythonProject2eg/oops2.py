class DemoClass:
    a=10
    def __init__(self):
        print("Welcome to IITP")
    def showvalue(self):
        self.c=self.a*self.a
        print(self.c)
    def showvalue1(self,a,b):
        print(a,b)

obj=DemoClass()
obj.showvalue()
obj.showvalue1(20,30)