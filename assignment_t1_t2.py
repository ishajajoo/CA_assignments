# 1
# a, b, c = 1, 2.01, 'string'
# print(c)

#2
# x = 2+5j
# y = 5
# x, y = y, x
# print(x)
# print(y)

#3
# x = 2
# y = 5
## swap using third variable
# temp = x
# x = y
# y = temp
# print(x)
# print(y)
## swap without third variable
# x = x+y #7
# y = x-y #2
# x = x-y #5
# print(x)
# print(y)

#4
# x = input("Enter a number")
# print(x)
# print x

#5
# x = input("Enter number between 1 and 10\n")
# y = input("Enter another number between 1 and 10\n")
# z = int(x) + int(y)
# w = z + 30
# print(w)

#6
# x = 4
# print(type(x))
# z = 4.1
# print(type(z))
# y = 'tr'
# print(type(y))

#7
# x = "HelloLady"
# y = "hello_lady"
# z = "helloLady"
# a = "hellolady"
# print("a = {}, x = {}, y = {}, z is {}".format(a, x, y, z))

#8
# x = 4
# x = 4.5
# print(type(x))
# "Yes, it is changing the value, Python variable takes the latest value assigned to it, making it a dynamic and versatile feature for developing programs"

#TASK-2
# x = 10
# if x%3==0:
#     print("Consultadd")
# if x%5==0 and x%3==0:
#         print("Consultadd - Python Training")
# elif x%5==0:
#     print("Python Training")

#TASk-2, Q2:
# num1 = input("Enter any number\n")
# num2 = input("Enter another number\n")
# num = input("Enter any number from 1 to 5\n")
# match num:
#     case "1":
#         z = int(num1)+int(num2)
#         print(z)
#     case "2":
#         z = int(num1)-int(num2)
#         print(z)
#     case "3":
#         z = int(num1)/int(num2)
#         print(z)
#     case "4":
#         z = int(num1)*int(num2)
#         print(z)
#     case "5":
#         num3 = input("Enter 4th number\n")
#         num4 = input("Enter 5th number\n")
#         z = (int(num1)+int(num2)+int(num3)+int(num4))/4
#         print(z)
# if z<0:
#     print("NEGATIVE")

#TASK-2, Q3:
# a, b, c = 10, 20, 30
# avg = (a+b+c)/3
# print("avg = ", avg)
# if avg>a and avg>b and avg>c:
#     print("avg is higher than a, b, c")
# elif avg>a and avg>b:
#     print("avg is higher than a, b, c")
# elif avg>a and avg>c:
#     print("avg is higher than a, c")
# elif avg>b and avg>c:
#     print("avg is higher than b, c")
# elif avg>a:
#     print("avg is just higher than a")
# elif avg>b:
#     print("avg is just higher than b")
# elif avg>c:
#     print("avg is just higher than c")

#TASK-2, Q4
# p = input("Enter any number\n")
# while True:
#     if int(p)>0:
#         print("Good Going")
#         continue
#     else:
#         print("It's Over")
#         break

#TASK-2, Q5
# for i in range(2000, 3200):
#     if i%7==0:
#         if i%5!=0:
#             print(i)

#TASK-2, Q6
#output-1
##TypeError: 'int' object is not iterable

#output-2
##0, error, 1, error, 2

# name 'Break' is not defined

#TASK-2, Q7
# for i in range(0, 6):
#     if i!=3:
#         print(i)
#     else:
#         continue

#TASK-2, Q8
# word = input("Enter any word\n")
# count_digit = 0
# count_letter = 0
# for i in word:
#     if i.isalpha():
#         count_letter+=1
#     elif i.isdigit():
#         count_digit+=1
# print("Letters ", count_letter)
# print("Digits ", count_digit)

#TASK-2, Q9
# Program 1
# n = input("Guess the lucky number\n")
# while n!=4:
#     continue

# Program 2
# import random
# n = random.randrange(1,10)
# print(n)
# answer = input("Do you want to continue guessing\n")
# number = int(input("Enter the number\n"))
# while n!=number and 'Yes'==answer:
#     if number<5:
#         print("Too low\n")
#         number = int(input("Enter the number again\n"))
#     elif number>5:
#         print("Too high\n")
#         number = int(input("Enter the number again"))
#     else:
#         break

#TASK-2, Q10 and Q11
# import random
# counter = 1
# n = random.randrange(1, 10)
# print(n)
# while counter<=5:
#     x = int(input("Enter any number\n"))
#     if n==x:
#         print("Good guess!\n")
#         break
#     else:
#         print("Try again!\n")
#         print("Sorry but that was not very successful")
#         counter+=1
# print("Game over!\n")







