# Write a program that asks the user for a number N and a choice C. And then give them the possibility to choose between computing the sum and computing the product of all integers in the range 1 to N (both inclusive).
# If C is equal to -
#  1, then print the sum
#  2, then print the product
#  Any other number, then print '-1' (without the quotes)

n = int(input())
c = int(input())
sum = 0
mul=1
if c==1:
    for i in range(n+1):
        sum = i + sum
    print(sum)
elif c==2:
    for i in range(1,n+1):
        mul = mul * i 
    print(mul)
else:
    print('-1') 
