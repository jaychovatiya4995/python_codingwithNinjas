# Write a program to input an integer N and print the sum of all its even digits and sum of all its odd digits separately.
# Digits mean numbers, not the places! That is, if the given integer is "13245", even digits are 2 & 4 and odd digits are 1, 3 & 5.

n = int(input())
even = 0
odd = 0
while(n>0):
    rm = n%10
    if(rm%2==0):
    	even=even+rm
    else:
    	odd=odd+rm
    n = n//10
    
print(even," ",odd)