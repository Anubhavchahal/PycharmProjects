class Area:
    def find_area(self,x=None,y=None):
        if x!=None and y!=None:
            print(x*y)
        elif x!=None:
            print(x*x)
        else:
            print("nothing")

obj1=Area()
obj1.find_area()
obj1.find_area(10)
obj1.find_area(10,20)