# Write a program to determine if given number is palindrome or not. Print true if it is palindrome, false otherwise.
# Palindrome are the numbers for which reverse is exactly same as the original one. For eg. 121

def checkPalindrome(num):
#Implement Your Code Here
    sum=0
    while(num > 0):
        rm = num%10
        sum = (sum*10)+rm
        num = num//10
    return sum

N = int(input())
	
isPalindrome = checkPalindrome(N)
if(isPalindrome == N):
	print('true')
else:
	print('false')