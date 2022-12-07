my_sentence = 'my name is {0} my age is {2} and my surname is {1}'.format('saba','20','mgeliashvili')
print(my_sentence)


my_name = input('enter your name: ')
my_surname = input('enter your surname: ')
my_age = int(input('enter your age: '))


# my_sent = 'my name is {} my surname is {} and my age is {}'.format(my_name,my_surname,my_age)
# print(my_sent)
my_age += 3
print('after 3 years i am now {} years old'.format(my_age))



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