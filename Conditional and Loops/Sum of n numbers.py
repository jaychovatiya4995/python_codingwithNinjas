# Given an integer n, find and print the sum of numbers from 1 to n

sum = 0
n = int(input())
for j in range(1,n+1):
    sum = sum + j 
               
print(sum)