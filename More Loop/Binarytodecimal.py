# Binary to decimal
# Given a binary number as an integer N, convert it into decimal and print.

n = int(input())

pv = 0
# c = 1
ans = 0
temp = n
while(temp!=0):
    d = n%10 
    temp = int(temp/10)
    c = 2**pv
    ans = ans + (d*c)
    pv+=1

print(ans) 