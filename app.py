# print("Hello, World!")

# print("   /|")
# print("  / |")
# print(" /  |")
# print("/___|")

# variables

# character_name = "John"
# character_age = "35"
# print("There once was a person named " + character_name + ", ")
# print("they were " + character_age + ".")
# character_name = "Tom"
# print("They really liked the name " + character_name + ".")

# strings

# print("Coding\nSchool")
# # Coding
# # School
#
# print("Coding\'s cool")
# Coding's cool

# phrase = "Coding School"
# print(phrase.upper().isupper())
# True
# print(len(phrase))
# 13
# print(phrase[0])
# C
# print(phrase.index("School"))
# 7
# print(phrase.replace("School", "is Cool"))
# Coding is Cool

# numbers
# print(3 + 4.5)
# 7.5
# print(3 * (4 + 5))
# adds parenthesis first
# 27
# print(10 % 6)
# 4
# num = 5
# print(str(num))
# 5
# print(str(num) + " is a number")
# 5 is a number

# abs
# my_num = -5
# print(abs(my_num))
# 5
# pow
# print(pow(3, 2))
# 9
# print(pow(4, 6))
# 4096
# print(max(3, 5))
# 5
# print(min(3, 5))
# 3
# print(round(3.2))
# 3.0
# print(round(3.7))
# 4.0

# `math` is a module
# from math import *
# print(floor(3.7))
# 3.0
# print(ceil(3.7))
# 4.0 - rounds up
# print(sqrt(36))
# 6.0

# Getting input from user
# write prompt to user in parenthesis
#  use `raw_input` for python version 2.7
# name = raw_input("Enter your name: ")
# age = raw_input("Enter your age: ")
# print("Hello " + name + ". you are " + age)

# Building a basic calculator

# num1 = raw_input("Enter a number: ")
# num2 = raw_input("Enter another number: ")
# result = int(num1) + int(num2)
# print(result)

# num1 = raw_input("Enter a number: ")
# num2 = raw_input("Enter another number: ")
# result = float(num1) + float(num2)
# print(result)

# Creating a mad libs game

# color = raw_input("Enter a color: ")
# pluralnoun = raw_input("Enter a plural noun: ")
# celebrity = raw_input("Enter a celebrity: ")
#
# print("Roses are " + color)
# print(pluralnoun + " are blue")
# print("I love " + celebrity)

# Lists

# friends = ["Lisa", "Karen", "Kevin", "Tony", "Oscar"]
# print(friends[1:])
# Prints elements after first index ['Karen', 'Kevin', 'Tony', 'Oscar']
# print(friends[1:3])
# Specifying a range ['Karen', 'Kevin']
# friends[2] = "Mike"
# print(friends[2])
# Updated index to: Mike

# lucky_numbers = [4, 8, 15, 16, 23, 42]
# Add 2 lists together
# friends.extend(lucky_numbers)
# Add to end of list
# friends.append("Creed")
# friends.insert(1, "Kelly")
# friends.remove("Tony")
# remove last index:
# friends.pop()
# print(friends.index("Lisa"))
# 0
# sorts alphabetically or ascending order
# friends.sort()
# lucky_numbers.reverse()
# lucky_numbers.sort()
# To copy
# friends2 = friends[:]
# print(friends)
# print(friends2)

# Tuples = data structure that stores information

# ie: coordinates
# Tuples are immutable but potentially changing
#  Use tuples for data that is never going to change
# coordinates = [(4, 5), (6, 7), (80, 34)]
# print(coordinates[2][0])
# 80

# Functions
# Say hi to user
# def say_hi(name, age):
    # print("Hello " + name + ", you are " + str(age))

#  call the Function
# say_hi("Mike", 70)
# say_hi("Jane", 35)
# Hello Mike, you are 70
# Hello Jane, you are 35


# Return Statement
# cube a number
# def cube(num):
#     return num*num*num
#
# result = cube(4)
# print(result)


# if Statement
# is_female = True
# is_tall = False
#
# if is_female and is_tall:
#     print("You are a tall female")
# elif is_female and not(is_tall):
#     print("You are a short female")
# elif not is_female and (is_tall):
#     print("You are not a female and are tall")
# else:
#     print("You are either not a female or tall")

# If Statements & Comparisons
# passing in 3 numbers and function will return the larger of the three
# def max_num(num1, num2, num3):
#     if num1 >= num2 and num1 >= num3:
#         return num1
#     elif num2 >= num1 and num2 >= num3:
#         return num2
#     else:
#         return num3
#
# print(max_num(3,40,5))


# Building a better calculator
# num1 = float(raw_input("Enter first number: "))
# operator = raw_input("Enter operator: ")
# num2 = float(raw_input("Enter second number: "))
#
# if operator == "+":
#     print(num1 + num2)
# elif operator == "-":
#     print(num1 - num2)
# elif operator == "/":
#     print(num1 / num2)
# elif operator == "*":
#     print(num1 * num2)
# else:
#     print("Invalid operator")


# Dictionaries
# monthConversions = {
#     # define key/value pairs here
#     0: "January",
#     1: "February",
#     2: "March",
#     "Apr": "April",
#     "May": "May",
#     "Jun": "June",
#     "Jul": "July",
#     "Aug": "August",
#     "Sep": "September",
#     "Oct": "October",
#     "Nov": "November",
#     "Dec": "December",
# }

# print(monthConversions["Mar"])
# print(monthConversions.get("Luv", "Not a valid Key"))

# print(monthConversions[0])
# January

# While Loop
# i = 1
# while i <= 10:
#     print(i)
#     i += 1
#
# print("Done with loop")


#  Build guessing game
# secret_word = "giraffe"
# guess = ""
# guess_count = 0
# guess_limit = 3
# out_of_guesses = False
#
# while guess != secret_word and not(out_of_guesses):
#     if guess_count < guess_limit:
#         guess = raw_input("Guess the secret word: ")
#         guess_count += 1
#     else:
#         out_of_guesses = True
#
# if out_of_guesses:
#     print("Out of guesses, You lost!")
# else:
#     print("You win!")


# For Loop
# friends = ["Lisa", "Karen", "Kevin", "Tony", "Oscar"]
# for friend in friends:
#     print(friend)
# for index in range(5):
#     if index == 0:
#         print("first iteration")
#     else:
#         print("not first")


# Exponent Function
# def raise_to_power(base_num, power_num):
#     result = 1
#     for index in range(power_num):
#         result = result * base_num
#     return result
#
# print(raise_to_power(2, 3))


# 2D Lists & Nested Loops
# number_grid = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     [0]
# ]
#
# for row in number_grid:
#     for col in row:
#         print(col)

# Build a translator
# def translate(phrase):
#     translation = ""
#     for letter in phrase:
#         if letter.lower() in "aeiou":
#             if letter.isupper():
#                 translation = translation + "G"
#             else:
#                 translation = translation + "g"
#         else:
#             translation = translation + letter
#     return translation
#
# print(translate(raw_input("Enter a phrase: ")))


# Try Except block: catching errors
# try:
#     number = int(raw_input("Enter a number: "))
#     print(number)
# except:
#     print("Invalid Input")


# Reading files
# Modes: r = read, w = write, a = append, r+ = read & write
# readable, read, readline, readlines
# employee_file = open("employees.txt", "r")
# for employee in employee_file.readlines():
#     print(employee)
#     # print(employee_file.readlines()[1])
# employee_file.close()

# Writing to files using append
# employee_file = open("employees.txt", "a")
# employee_file.write("\nKelly - Customer Service")
# employee_file.close()

# Writing to files using write
# employee_file = open("employees1.txt", "w")
# employee_file.write("\nKelly - Customer Service")
# employee_file.close()

# Writing to HTML file
# employee_file = open("index.html", "w")
# employee_file.write("<p>This is an HTML page</p>")
# employee_file.close()


# Modules and Pip
# import useful_tools
#
# print(useful_tools.roll_dice(10))


# Classes & Objects
# from student import Student
#
# student1 = Student("Jim", "Business", 3.1, True)
# student2 = Student("Pam", "Art", 4.0, False)
#
# print(student2.name)

# from question import Question
#
# # Building a multiple choice quiz
# question_prompts = [
# "What color are apples?\n(a) Red\n(b) Purple\n(c) Orange\n\n",
# "What color are Bananas?\n(a) Blue\n(b) Pink\n(c) Yellow\n\n",
# "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
# ]
#
# questions = [
#     Question(question_prompts[0], "a"),
#     Question(question_prompts[1], "c"),
#     Question(question_prompts[2], "b"),
# ]
#
# def run_test(questions):
#     score = 0
#     for question in questions:
#         answer = raw_input(question.prompt)
#         if answer == question.answer:
#             score+= 1
#     print("You got " + str(score) + "/" + str(len(questions)) + " Correct")
#
# run_test(questions)


# Object Functions
# from student import Student
#
# student1 = Student("Oscar", "Accounting", 3.1)
# student2 = Student("Phyllis", "Business", 3.8)
#
# print(student2.on_honor_roll())


# Inheritance
# from chef import Chef
# from chineseChef import ChineseChef
#
# theChef = Chef()
# theChef.make_special_dish()
#
# theChineseChef = ChineseChef()
# theChineseChef.make_special_dish()

# output
# The chef makes a chicken with cream sauce
# The chef makes orange chicken and rice
