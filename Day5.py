#https://www.hackerrank.com/challenges/solve-me-first/problem
# Solve me first
# def solveMeFirst(a,b):
# 	# Hint: Type return a+b below
#     return a+b

# num1 = int(input())
# num2 = int(input())
    
# res = solveMeFirst(num1,num2)
# print(res)
# op: 2
# 3
# Expected Output
# 5
# 
# 2. https://www.hackerrank.com/challenges/simple-array-sum/problem
# #!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# #
# # Complete the 'simpleArraySum' function below.
# #
# # The function is expected to return an INTEGER.
# # The function accepts INTEGER_ARRAY ar as parameter.
# #

# def simpleArraySum(ar):
#     # Write your code here
#     return sum(ar) 
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     ar_count = int(input().strip())

#     ar = list(map(int, input().rstrip().split()))

#     result = simpleArraySum(ar)

#     fptr.write(str(result) + '\n')

#     fptr.close()


# function of finding maximum and minimum

# def maxmin(ar):
#     b=0
#     c=ar[1]
#     for i in ar:
#         if i>b:
#             b=i
#         if i<c:
#             c=i
#     print("largest ",b)
#     print("smallest ",c)
# n=int(input("Enter range: "))
# ar=[]
# for i in range(0,n):
#     b=int(input("Enter digit: "))
#     ar.append(b)
# maxmin(ar)

# Types of taking input
# 1. n=int(input(""))
# 2. a=int(input(""))
#    b=int(input(""))
# 3. a,b=map(int(input("").split())
# 4. ls=list(map(int(input("").split()))
# 5. arr=eval(input())

# Remove duplicate
# def remove(ar):
#     ls=[]
#     for i in ar:
#         if i not in ls:
#             ls.append(i)
#     return(ls)
# n=int(input("Enter range: "))
# ar=[]
# for i in range(0,n):
#     b=int(input("Enter digit: "))
#     ar.append(b)
# print(remove(ar))

