https://leetcode.com/problems/palindrome-number/
class Solution(object):
    def isPalindrome(self, x):
        og=x
        reverse=0
        while x>0:
            temp=x%10
            reverse=reverse*10 + temp
            x=x//10
        return reverse==og

Input: x = 121
Output: true

https://leetcode.com/problems/richest-customer-wealth/
class Solution(object):
    def maximumWealth(self, accounts):
        br=[]
        for i in accounts:
            ar=i
            sum=0
            for j in ar:
                sum+=j
            br.append(sum)
        return max(br)

https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/find-product/
n = int(input())
ar = list(map(int, input().split()))
mod = 10**9 + 7

answer = 1
for i in range(n):
    answer = (answer * ar[i]) % mod

print(answer)
Sample Input
5
1 2 3 4 5
Sample Output
120

https://www.hackerrank.com/challenges/staircase/problem
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    for i in range(1, n+1):
        print(" "*(n-i)+"#"*i)
    # Write your code here
    

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)

Input (stdin)
6
Your Output (stdout)
     #
    ##
   ###
  ####
 #####
######


            
