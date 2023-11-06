print('''
+ add
- subtract
* multiply
/ divide
''')
num1=int(input("Enter the value 1:"))
num2=int(input("enter the value 2:"))
opr=input("enter the opr")
if opr=="+":
    print(num1+num2)
elif opr=="-":
    print(num1-num2)
elif opr=="*":
    print(num1*num2)
elif opr=="/":
    print(num1/num2)
else :
    print("invalid operation")