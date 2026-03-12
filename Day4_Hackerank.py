# Q1 Say "Hello, World!" With Python
print("Hello, World!")
# Q2 Python If-Else
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if n%2!=0:
        print("Weird")
    elif n>2 and n<=5:
        print("Not Weird")
    elif n>6 and n<=20:
        print("Weird")
    elif n>20:
        print("Not Weird")
#Q3 Arithmetic Operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)
#Q4 Python: Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)
#Q5 Loops
if __name__ == '__main__':
    n = int(input())
    a=0
    while n>0:
        print(a**2)
        a+=1
        n-=1
