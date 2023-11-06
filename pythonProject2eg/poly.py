l=[10,20,30,40]
print(len(l))
s="welcome"
print(len(s))
class Ws:
    def displayinfo(self,name=''):
        print("Welcome to IITP "+ name)
obj=Ws()
obj.displayinfo()
obj.displayinfo("Python")

class Ws:
    def displayinfo(self):
        print("Welcome to IITP")

class IIP(Ws):
    def displayinfo(self):
        super().displayinfo()
        print("Welcome to ws")

obj=IIP()
obj.displayinfo()

