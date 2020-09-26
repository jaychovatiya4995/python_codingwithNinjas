# Given a decimal number (integer N), convert it into binary and print.
# The binary number should be in the form of an integer.
# Note : The given input number could be large, so the corresponding binary number can exceed the integer range. So you may want to take the answer as long for CPP and Java.

n = int(input())
ans = 0
pv = 1
while(n>0):
    d = n%2
    s = int(d)
    ans = ans + (s*pv)
    pv = 10*pv
    n=n//2
print(ans,end=" ")
    