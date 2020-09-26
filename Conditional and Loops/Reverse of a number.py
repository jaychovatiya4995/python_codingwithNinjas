# Write a program to generate the reverse of a given number N. Print the corresponding reverse number.
# Note : If a number has trailing zeros, then its reverse will not include them. For e.g., reverse of 10400 will be 401 instead of 00401.
def Reverse(num):
    res = 0 
    while(num>0):
        rm = num%10
        res = (res*10)+rm
        num = num//10
    return res
N = int(input())
print(Reverse(N))