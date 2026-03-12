# 1.Write a program to check whether a number is even or odd.
# no=int(input("Enter no: "))
# if(no%2==0):
#     print("Even")
# else:
#     print("Odd")
# op: Enter no: 4
#     Even

# 2.Write a program to find the largest of three numbers.
# b=0
# for i in range(3):
#     a=int(input("Enter No:"))
#     if(a>b):
#         b=a
# print("Largest no is:",b)
# op: Enter No:4
#     Enter No:3
#     Enter No:5
#     Largest no is: 5

# 3.Check whether a number is positive, negative, or zero.
# a=int(input("Enter No: "))
# if a>0:
#     print("Positive")
# elif a<0:
#     print("Negative")
# else:
#     print("Zero")
# op: Enter No: -3
#     Negative

# 4.Write a program to check whether a number is divisible by both 3 and 5.
# a=int(input("Enter No.: "))
# if a%3==0:
#     if a%5==0:
#         print("Divisible by both 3 and 5")
#     else:
#         print("Not Divisible")
# op: Enter No.: 15
#     Divisible by both 3 and 5

# 5.Write a program to print numbers from 1 to N.
# n=int(input("Give n: "))
# for i in range(n):
#     print(i+1)
# op: Give n: 5
#     1
#     2
#     3
#     4
#     5

# 6.Write a program to print all even numbers from 1 to N.
# n=int(input("Give n: "))
# for i in range(n):
#     if (i+1)%2==0:
#         print(i+1)
# op: Give n: 9
#     2
#     4
#     6
#     8

# 7.Write a program to calculate the sum of first N natural numbers.
# n=int(input("Enter N: "))
# sum=0
# for i in range(n):
#     sum=sum+i+1
# print("Sum of first N natural numbers is:",sum)
# op: Enter N: 5
#     Sum of first N natural numbers is: 15

# 8.Write a program to calculate the factorial of a number.
# n=int(input("Enter a number:"))
# sum=1
# while n>0:
#     sum=sum*n
#     n-=1
# print("Factorial is: ", sum)
# op: Enter a number:5
#     Factorial is:  120

# 9.Write a program to print the multiplication table of a number.
# n=int(input("Enter no: "))
# for i in range(1,11):
#     print(n*i)
# op: Enter no: 5
# 5
# 10
# 15
# 20
# 25
# 30
# 35
# 40
# 45
# 50

# 10.Write a program to count the number of digits in a number.
# a=int(input("Enter no: "))
# count=len(str(a))
# print(count)

# ##Or

# a=int(input("Enter no: "))
# count=0
# while a>0:
#     count=count+1
#     a=a//10
# print(count)
# op: Enter no: 345
#     3

# 11.Write a program to reverse a number.
# a=int(input("Enter a no: "))
# rev=0
# while a>0:
#     rem=a%10
#     rev=rev*10 + rem
#     a=a//10
# print(rev)

# ##OR

# a=int(input("Enter a no: "))
# b=int(str(a)[::-1])
# print(b)
# op: Enter a no: 345
#     543   

# 12.Write a program to check whether a number is palindrome.
# a=int(input("Enter no: "))
# temp=a
# rev=0
# while a>0:
#     rem=a%10
#     rev=rev*10 + rem
#     a=a//10
# if temp==rev:
#     print("Palindrome")
# else:
#     print("Not Palindrome")
# op: Enter no: 121
#     Palindrome

# 13.Write a program to find the sum of digits of a number.
# a=int(input("Enter a no: "))
# sum=0
# while a>0:
#     rem=a%10
#     sum+= rem
#     a=a//10
# print(sum)
# op: Enter a no: 123
#     6

# 14.Write a program to check whether a number is an Armstrong number.
# a=int(input("Enter a no: "))
# temp=a
# sum=0
# count=0
# while a>0:
#     count=count+1
#     a=a//10
# while a>0:
#     rem=a%10
#     sum+= rem**count
#     a=a//10
# if temp==sum:
#     print("Armstrong")
# else:
#     print("Not Armstrong")
# op: Enter a no: 153
#     Armstrong

# 15.Write a program to print numbers divisible by 7 between 1 and N.
# n=int(input("Enter N: "))
# for i in range(n):
#     if (i+1)%7==0:
#         print(i+1)
# op: Enter N: 50
#     7
#     14
#     21
#     28
#     35
#     42
#     49

