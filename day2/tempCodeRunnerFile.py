
num1 = int(input("enter first number "))
num2 = int(input("enter second number "))
num3 = int(input("enter third number "))
sum = num1 + num2 + num3

if num1 % 2 == 0:
    print('error')
if num2 % 2 == 0:
    print('error')
if num3 % 2 == 0:
    print('error')
else:
    print(sum)