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

# friends2 = friends[:]
# print(friends)
# print(friends2)
