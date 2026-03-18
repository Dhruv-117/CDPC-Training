# https://leetcode.com/problems/two-sum/description/
# class Solution(object):
#     def twoSum(self, nums, target):
#         seen={}
#         for i, num in enumerate(nums):
#             comp=target - num
#             if comp in seen:
#                 return [seen[comp], i]
#             seen[num]=i

# https://leetcode.com/problems/fizz-buzz/description/
# class Solution(object):
#     def fizzBuzz(self, n):
#         ar=[]
#         for i in range(1,n+1):
#             if i%3==0 and i%5==0:
#                 ar.append("FizzBuzz")
#             elif i%3==0:
#                 ar.append("Fizz")
#             elif i%5==0:
#                 ar.append("Buzz")
#             else:
#                 ar.append(str(i))
#         return ar

# https://leetcode.com/problems/running-sum-of-1d-array/description/
# class Solution(object):
#     def runningSum(self, nums):
#         ar=[]
#         b=0
#         for i in nums:
#             b+=i
#             ar.append(b)
#         return ar
# Implementation of Stack:
# class Stack:
#     def __init__(self):
#         self.stack = []

#     # Push element onto stack
#     def push(self, item):
#         self.stack.append(item)
#         print(f"Pushed: {item}")

#     # Pop element from stack
#     def pop(self):
#         if self.is_empty():
#             return "Stack is empty"
#         return self.stack.pop()

#     # Peek top element
#     def peek(self):
#         if self.is_empty():
#             return "Stack is empty"
#         return self.stack[-1]

#     # Check if stack is empty
#     def is_empty(self):
#         return len(self.stack) == 0


# # Example usage
# s = Stack()
# s.push(10)
# s.push(20)
# s.push(30)

# print("Top element:", s.peek())
# print("Popped element:", s.pop())
# print("Stack after pop:", s.stack)

# Larger number nearest to the current number:
# def next_greater_elements(arr):
#     n = len(arr)
#     result = [-1] * n
#     stack = []

#     for i in range(n):
#         while stack and arr[i] > arr[stack[-1]]:
#             index = stack.pop()
#             result[index] = arr[i]
#         stack.append(i)

#     return result


# # Example
# arr = list(map(int, input("Enter array elements: ").split()))
# print(next_greater_elements(arr))
