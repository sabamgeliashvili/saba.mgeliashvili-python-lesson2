name = 'saba'
print(len(name))

if len(name) > 3:
    print('hello')

full_name = 'saba mgeliashvili'
print(full_name[5])
print('a' in full_name)
print( 'v' not in full_name)
print(full_name[1:4])
print(full_name[1:])

 
num1 = int(input("enter first number "))
num2 = int(input("enter second number "))
multiply = num1 * num2

if multiply > 100:
    print(multiply)
else:
    print('you lose')




#  დავალება

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