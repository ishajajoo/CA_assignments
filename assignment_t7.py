# Q1
# import math
# def calc_sqroot(c=50, h=30):
#     d = int(input("Enter diameter\n"))
#     q = math.sqrt(2*c*d)/h
#     return q

# print(calc_sqroot())

# Q2
# class Shape:
#     def __init__(self, area):
#         self.area = area

#     def area_(self):
#         self.area = 0
#         return self.area

# class Square(Shape):
#     def __init__(self, length):
#         self.length = length

#     def area_(self):
#         return (self.length*self.length)

# sh = Shape(0)
# print(sh.area_())  
# s = Square(3)
# print(s.area_())

# Q3
# class ThreeSum:
#     def __init__(self, numbers):
#         self.numbers = numbers

#     def find_three_sum(self):
#         n = len(self.numbers)
#         if n < 3:
#             return []

#         self.numbers.sort()  # Sort the numbers in ascending order

#         triplets = []

#         for i in range(n - 2):
#             if i > 0 and self.numbers[i] == self.numbers[i - 1]:
#                 continue  # Skip duplicates

#             left = i + 1
#             right = n - 1

#             while left < right:
#                 total_sum = self.numbers[i] + self.numbers[left] + self.numbers[right]

#                 if total_sum == 0:
#                     triplets.append((self.numbers[i], self.numbers[left], self.numbers[right]))
#                     left += 1
#                     right -= 1

#                     while left < right and self.numbers[left] == self.numbers[left - 1]:
#                         left += 1  # Skip duplicates
#                     while left < right and self.numbers[right] == self.numbers[right + 1]:
#                         right -= 1  # Skip duplicates

#                 elif total_sum < 0:
#                     left += 1
#                 else:
#                     right -= 1

#         return triplets


# # Example usage:
# numbers = [-1, 0, 1, 2, -1, -4, 5]
# three_sum = ThreeSum(numbers)
# result = three_sum.find_three_sum()
# print("Triplets with sum zero:")
# for triplet in result:
#     print(triplet)

#Q4
# class Time:
#     def __init__(self):
#         # self.hrs = hrs
#         # self.mins = mins
#         pass

#     def addTime(self):
#         hr_1=int(input("Enter hours\n"))
#         min_1=int(input("Enter minutes\n"))
#         hr_2=int(input("Enter hours\n"))
#         min_2=int(input("Enter minutes\n"))
#         self.hrs = hr_1 + hr_2 #2, 3
#         self.mins = min_1 + min_2 #30, 30
#         if self.mins>=60:
#             self.h = int(self.mins/60)
#             self.mins%=60
#             self.hrs+=self.h
#         return "{} hrs {} mins".format(self.hrs, self.mins)
    
#     def displayTime(self):
#         return "{} hrs {} mins".format(self.hrs, self.mins)
    
#     def displayMinute(self):
#         self.minut = self.hrs*60+self.mins
#         return "Total {} mins".format(self.minut)

# t = Time()
# print(t.addTime())
# print(t.displayTime())
# print(t.displayMinute())

#Q5
# class Person:
#     def __init__(self, age):
#         self.age = age

#     def yearPasses(self):
#         self.age+=1

#     def amIOld(self):
#         if self.age < 0:
#             #self.age = 0
#             print(self.age)
#             return "Age is not valid, setting age to 0"
#         elif self.age in range(0, 13):
#             return "You are young"
#         elif self.age in range(13,20):
#             return "You are a teenager"
#         else:
#             return "You are old"

    
# p = Person(-1)
# #print(p.yearPasses())
# print(p.amIOld())
    

