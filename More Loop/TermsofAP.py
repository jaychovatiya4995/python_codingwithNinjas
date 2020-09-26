# Write a program to print first x terms of the series 3N + 2 which are not multiples of 4.
x = int(input())
i = 1
count = 0

while(count!=x):
    if count < x:
        ser = (3*i)+2
    
    if (ser%4)!=0:
        print(ser,end=' ')
        count += 1
    i+=1