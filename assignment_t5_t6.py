# TASK FIVE
# Q1
# try:
#     print(eval('six times seven'))
# except SyntaxError as se:
#     print(se)

# Q2
# import sys

# if len(sys.argv) < 2:
#     print("Please provide a file name as a command-line argument.")
#     sys.exit(1)

# file_name = sys.argv[1]

# while True:
#     try:
#         with open(file_name, 'r') as file:
#             # File opened successfully, perform required operations here
#             # For example, you can print the contents of the file
#             print(file.read())
#         break  # Exit the loop if the file is opened successfully
#     except FileNotFoundError:
#         print("File not found. Please enter a valid file name.")
#         file_name = input("Enter the file name: ")
#     except IOError:
#         print("Error occurred while reading the file. Please try again.")
#         file_name = input("Enter the file name: ")

#Q3
# number = input("Enter a four-digit number: ")

# try:
#     if len(number) != 4:
#         raise ValueError("The length is too short/long !!! Please provide only four digits")
#     int(number)  # Check if the input is a valid integer
#     print("Valid number:", number)
# except ValueError as e:
#     print(e)

#Q4
# MAX_ATTEMPTS = 3

# def login():
#     username = input("Enter your username: ")
#     password = input("Enter your password: ")
    
#     attempts = 1
#     while attempts <= MAX_ATTEMPTS:
#         re_enter_password = input("Re-enter your password: ")
#         if re_enter_password == password:
#             print("Login successful!")
#             return
#         else:
#             print("Password incorrect. Please try again.")
#             attempts += 1
    
#     print("Maximum login attempts exceeded. Exiting...")

# login()

# Q5
# def get_even_length_strings(file_name):
#     even_length_strings = []
    
#     try:
#         with open(file_name, 'r') as file:
#             content = file.read()
#             words = content.split()  # Split the content into words
            
#             for word in words:
#                 if len(word) % 2 == 0:
#                     even_length_strings.append(word)
    
#     except FileNotFoundError:
#         print(f"File '{file_name}' not found.")
    
#     return even_length_strings


# file_name = "doc.txt"
# even_length_strings = get_even_length_strings(file_name)
# print("Even Length Strings:")
# for word in even_length_strings:
#     print(word)

#TASK SIX
#Q1 
# def find_uppercase_chars(string):
#     uppercase_chars = [char for char in string if char.isupper()]
#     return uppercase_chars

# # Example usage:
# input_string = "Hello World"
# uppercase_chars = find_uppercase_chars(input_string)
# print("Uppercase Characters:", uppercase_chars)

#Q2
# def construct_student_subject_dictionary(students, subjects):
#     student_subject_dict = {}
    
#     # Using for loop
#     for i in range(len(students)):
#         student_subject_dict[students[i]] = subjects[i]
    
#     # Using dictionary comprehension
#     # student_subject_dict = {students[i]: subjects[i] for i in range(len(students))}
    
#     return student_subject_dict

# # Example usage:
# student_names = ['Smit', 'Jaya', 'Rayyan']
# subject_names = ['CSE', 'Networking', 'Operating System']

# student_subject_dict = construct_student_subject_dictionary(student_names, subject_names)
# print("Student-Subject Dictionary:", student_subject_dict)

#Q3
# def reverse_string(string):
#     length = len(string)
#     for i in range(length - 1, -1, -1):
#         yield string[i]

# # Example usage:
# input_string = "Consultadd Training"
# reversed_string = ''.join(reverse_string(input_string))
# print("Reversed String:", reversed_string)

#Q4
# def decorator_function(original_function):
#     def wrapper_function(*args, **kwargs):
#         print(f"Before executing {original_function.__name__} function")
#         result = original_function(*args, **kwargs)
#         print(f"After executing {original_function.__name__} function")
#         return result
#     return wrapper_function

# @decorator_function
# def greet(name):
#     print(f"Hello, {name}!")

# # Calling the decorated function
# greet("John")




