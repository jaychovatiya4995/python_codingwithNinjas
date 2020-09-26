# Write a program that performs the tasks of a simple calculator. The program should first take an integer as input and then based on that integer perform the task as given below.
# 1. If the input is 1, 2 integers are taken from the user and their sum is printed.
# 2. If the input is 2, 2 integers are taken from the user and their difference(1st number - 2nd number) is printed.
# 3. If the input is 3, 2 integers are taken from the user and their product is printed.
# 4. If the input is 4, 2 integers are taken from the user and the quotient obtained (on dividing 1st number by 2nd number) is printed.
# 5. If the input is 5, 2 integers are taken from the user and their remainder(1st number mod 2nd number) is printed.
# 6. If the input is 6, the program exits.
# 7. For any other input, print "Invalid Operation".

flag=True
while(flag):
    n = int(input())
    if n==1:
        a = int(input())
        b = int(input())
        print(a+b)
    elif n==2:
        a = int(input())
        b = int(input())
        print(a-b)
    elif n==3:
        a = int(input())
        b = int(input())
        print(a*b)
    elif n==4:
        a = int(input())
        b = int(input())
        print(a//b)
    elif n==5:
        a = int(input())
        b = int(input())
        print(a%b)
    elif n==6:
        flag=False
    else:
        print('Invalid Operation')