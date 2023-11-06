import module1
print(module1.sum(10,20))
print(module1.mul(10,20))
print()
import module1 as m
print(m.sum(10,20))
print(m.mul(10,20))
print()
from module1 import sum
print(sum(10,20))
print()
from module1 import *
print(sum(10,20))
print(mul(10,20))