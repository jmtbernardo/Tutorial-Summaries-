# Python Summaries Tutorial

# Sources:
# https://www.youtube.com/watch?v=N4mEzFDjqtA&index=3&list=PLGLfVvz_LVvSX7fVd4OUFp_ODd86H0ZIY&t=0s
# http://www.newthinktank.com/2014/11/python-programming/
# https://www.youtube.com/watch?v=rfscVS0vtbw



#Home‎ > ‎Programming‎ > ‎Python‎ > ‎

# Basics/Variables
# Arithmetic
# Strings
# Lists
# Tuples
# Dictionary
# Conditionals
# For Loop
# While Loop
# Functions
# User Input
# File I/O
# Classes / Objects
# Constructors
# Inheritance
# Overwriting
# Overloading s
# Polymorphism


# Name of File: Hellopython.py
#-------------------------------------------------------------------------------------- MODULES
# Import is used to make specialty functions available
# Imports enables extra functions into your file
# Imports enables extra functions into your file
# There are  3 types of modules one is built in, external, and default
# Also you can import code from another file you created for example: import second_page
# External Libraries/lib/site-packages/
import random
import sys
import os


import math
print(math.floor(18.7))
#O 18.0

#----------------------------------------------------------------------------------------------- COMMENT
# Comment
# It will not be run by the program, invisible to the program ''' '''
# Used to disable code, to explain the code, reminder, to communicate with other programmers
# It is highly recommend to write lot of comments on your code

'''
This is a multi-line comment
'''

# Invisible Comment

#-----------------------------------------------------------------------------------------  STRINGS
# A string is a string of characters surrounded by " or '
# print() outputs data to the screen
# This is a String is just one line of code

# Example
print("This is a String")
#O This is a String

# Drawing a Shape
# Example
print("   /|")
print("  / |")
print(" /  |")
print("/___|")
#O Displays a Triangle

# Creating new line with escape character \n
# Example
print("Jose \n Bernardo")
#O Jose
#O      Bernardo

# To keep from printing newlines use end=""
print("I don't like ",end="")
print("newlines")
#O I don't like newlines

# You can print a string multiple times with *
print('\n' * 5)
#O
#O
#O
#O
#O


# A string is a series of characters surrounded by ' or "
long_string = "I'll catch you if you fall - The Floor"

print(long_string[0:4])                      # Retrieve the first 4 characters
#O I'll

print(long_string[-5:])                      # Get the last 5 characters
#O Floor

print(long_string[:-5])                      # Everything up to the last 5 characters
#O I'll catch you if you fall - The


print(long_string[:4] + " be there")         # Concatenate part of a string to another
#O I'll be there

print("%c is my %s letter and my number %d number is %.5f" % ('X', 'favorite', 1, .14))     # String formatting
#O X is my favorite letter and my number 1 number is 0.14000

print(long_string.capitalize())              # Capitalizes the first letter
#O I'll catch you if you fall - the floor


print(long_string.find("Floor"))             # Returns the index of the start of the string
#O 33                                        # case sensitive

print(long_string.isalpha())                 # Returns true if all characters are letters ' isn't a letter
#O False

print(long_string.isalnum())                 # Returns true if all characters are numbers
#O False

print(len(long_string))                      # Returns the string length
#O 38


print(long_string.replace("Floor", "Ground")) # Replace the first word with the second (Add a number to replace more)
#O I'll catch you if you fall - The Ground

print(long_string.strip())                    # Remove white space from front and end
#O I'll catch you if you fall - The Floor


quote_list = long_string.split(" ")          # Split a string into a list based on the delimiter you provide
print(quote_list)
#O ["I'll", 'catch', 'you', 'if', 'you', 'fall', '-', 'The', 'Floor']

#--------------------------------------------------------------------------------------- VARIABLES
# A variable is a place to store values
# Variable = "Value"
# Its name is like a label for that value
# A variable name can contain letters, numbers, or _
# RULE can't start with a number

# Data Types
# Variable = "Value/data type"
# There are 5 data types: Numbers, Strings, List, Tuple, Dictionary
# You can store any of them in the same variable

name = 15
print(name)
#O 15

# printing only a variable in a string.
# Example
name = "Jose"
print(name)
#O Jose

# Joining two strings/variables
# Example
name = "Jose "
last_name = "Bernardo "
print(name + last_name)
#O Jose Bernardo

# Example
name = "Jose"
age = "30"
print("There once was a man named " +name+ ",")
print("He was " + age + " years old.")

# Override/change variable
name = "Bernardo"
print("He really liked the name " +name+ ",")
print("but didn't like being " +age+ ".")
#O There once was a man named Jose,
#O He was 30 years old.
#O He really liked the name Bernardo,
#O but didn't like being 30.

#----------------------------------------------------------------------------- VARIABLE & FUNCTIONS
# Variable with built in function
# Code .upper ,is the function code, it will capitalize the string
# Example
name = "Jose Bernardo "
print(name.upper())
#O Jose BERNARDO

# Variable followed by two functions
# Code .upper() ,is the function, it will capitalize the string
# .isupper() ,is the function, condition is true if string is capitalized
# Example
name = "Jose Bernardo "
print(name.upper().isupper())
#O True

# Variable followed by function
# Code len() ,is the length function, it will tell how many characters are in this string
# Example
name = "Jose Bernardo "
print(len(name))
#O 14

# Variable followed by function
# Code[0] ,is the function, it will grab the character/index of the string
# 0 is considered a parameter
#Example
name = "Jose Bernardo "
print(name[0])
#O J

# Variable followed by function
# Code .index("") ,is the index function, it will tell the count number of that character in the string
# J is considered a parameter
#Example
name = "Jose Bernardo "
print(name.index("J"))
#O 0

# Variable followed by function
# Code .replace("") ,is the index function, it will replace the string with different string
# Example
name = "Jose Bernardo "
print(name.replace("Jose", "Manuel"))
#O Manuel Bernardo


# If you must use a " or ' between the same quote escape it with \
quote = "\"Always remember your unique,"

# A multi-line quote
multi_line_quote = ''' just
like everyone else" '''

print(quote + multi_line_quote)
#O "Always remember your unique, just like everyone else"

# To embed a string in output use %s
print("%s %s %s" % ('I like the quote', quote, multi_line_quote))
#O I like the quote "Always remember your unique,  just like everyone else"

#-------------------------------------------------------------------------------------------- ARITHMETIC

# The arithmetic operators +, -, *, /, %, **, //
# ** Exponential calculation
# // Floor Division
print("5 + 2 =", 5+2)
print("5 - 2 =", 5-2)
print("5 * 2 =", 5*2)
print("5 / 2 =", 5/2)
print("5 % 2 =", 5%2)
print("5 ** 2 =", 5**2)
print("5 // 2 =", 5//2)
#O 5 + 2 = 7
#O 5 - 2 = 3
#O 5 * 2 = 10
#O 5 / 2 = 2.5
#O 5 % 2 = 1
#O 5 ** 2 = 25
#O 5 // 2 = 2

# Order of Operation states * and / is performed before + and -

print("1 + 2 - 3 * 2 =", 1 + 2 - 3 * 2)
print("(1 + 2 - 3) * 2 =", (1 + 2 - 3) * 2)
#O 1 + 2 - 3 * 2 = -3
#O (1 + 2 - 3) * 2 = 0

#-----------------------------------------------------------------------------------------ARITHMETIC & FUNCTIONS
# Code str() ,is string function, converts integer into string
# Code abs() ,is absolute value function, converts number into absolute values
# Code pow() ,is power function, 3^2
# Code max() ,is maximum function, it will grab single highest number
# Code min() ,is minimum function, it will grab single lowest number
# Code round() ,is rounding function, it will round number to the highest power
# Code from math import * ,is a module enable to utilize additional functions
# Code floor() ,is a function, it will reduce round no matter what
# Code ceil() ,is a function, it will raise round no matter what
# Code sqrt() ,is function, it will square root the parameter
# Example
print(2)
print(5+5)
print(1*1+5)
Number = 5
print(Number)
print(str(Number)+" This number is now a string")
print(abs(Number))
print(pow(3, 2))
print(max(3, 2))
print(min(3, 2))
print(round(3.7))
from math import *
print(floor(3.7))
print(ceil(3.7))
print(sqrt(9))
#O 2
#O 10
#O 6
#O 5
#O 5 This number is now a string
#O 5
#O 9
#O 3
#O 2
#O 4
#O 3
#O 4
#O 3.0
#------------------------------------------------------------------------------------------------------- LISTS
# Lists
# A list allows you to create a list of values and manipulate them
# Each value has an index with the first one starting at 0
# Data structure that contains values
# Each word is considered an element and each element has index as whole
# 1%=0 index ,2%=1 index ,3%=2 index ,4%=3 index ,5% =4 or -1 index
# Example
list = ["1%","2%","3%","4%","5%"]
print(list[0])      #O 1%               # 0 index is first value
print(list[-1])     #O 5%               # -1 index is the last value
print(list[1:3])    #O ['2%', '3%']     # Range of values
print(len(list))    #O 5                # Get length of total values
print(max(list))    #O 5%               # Get the max value
print(min(list))    #O 1%               # Get the minimum value

list[0]= "10%"           # You can change the value stored in a list box
print(list)              #O ['10%', '2%', '3%', '4%', '5%']

del list[0]              # del deletes an value at specified index
print(list)              #O ['2%', '3%', '4%', '5%']

list.reverse()           # Organizes values into a numerical or alphabetic descending order
print(list)              #O ['5%', '4%', '3%', '2%']

list.sort()              # Organizes values into a numerical or alphabetic ascending order
print(list)              #O ['2%', '3%', '4%', '5%']

list.insert(5, "00")     # Insert value at given index
print(list)              #O ['2%', '3%', '4%', '5%', '00']

list.remove("00")        # Remove value from list
print(list)              #O ['2%', '3%', '4%', '5%']

list.append('99')        # Adds value at end of the list
print(list)              #O ['2%', '3%', '4%', '5%', '99']

list.pop()              # Removes last value from list
print(list)             #O ['2%', '3%', '4%', '5%']

list = list.copy()      # Makes identical copy of previous list
print(list)             #O ['2%', '3%', '4%', '5%']

print(list.count("5%")) #O 1   # Indicate how many copies of same value exist

print(list.index("4%")) #O 2    # Indicates the location of the value index, It helps find value index number

numbers=[" a, b, c, d, e, g,"] #O Second List
list.extend(numbers)           #O Adds another list
print(list)                    #E ['2%', '3%', '4%', '5%', ' a, b, c, d, e, g,']

list2 = ['blue', 'black', 'red'] # You can put any data type in a a list including a list
list3 = [list2, list]
#print(list3)                    #O ['blue', 'black', 'red', 'white', '4%', '3%', '2%']

list4 = list2 + list             # Combining lists with a +
print(list3)                     #O [['blue', 'black', 'red'], ['2%', '3%', '4%', '5%', ' a, b, c, d, e, g,']]

list.clear()                    # Delete entire list
print(list)                     #O []

# TUPLES ------------------------------------------------------------------ TUPLES
# Tuples
# Tuples can not be modified or changed "Immutable"
# Index 4 has index of [0], 5 has index of [2]
# add list in tuples you code: coordinates = [(4,5), (6,7)]
# tuples also have len(tuple), min(tuple) and max(tuple)

pi_tuple = (3, 1, 4, 1, 5, 9)

new_tuple = list(pi_tuple)         # Convert tuple into a list []
print(new_tuple)                   #O [3, 1, 4, 1, 5, 9]

new_list = tuple(new_tuple)         # Convert a list into a tuple ()
print(new_list)                     #O (3, 1, 4, 1, 5, 9)

#------------------------------------------------------------------------------------------------- DICTIONARY
# Dictionary
# # Made up of values with a unique key for each value
# # Similar to lists, but you can't join dicts with a +
# Is a structure, allows to store information in key value pairs
# When you want utilize information inside the dictionary you refer by using key
# Dictionary works like real dictionary, for example word is the key and definition is the value

# Example
month={
    "Jan":"January",
    "Feb":"February",
    "Mar":"March",
}

print(month["Jan"])                        #O January
print(month.get("Feb"))                    #O February
print(month.get("Love", "Not Valid Key"))  #O Not Valid Key

# Print the number of items in the dictionary
print(len(month))                          #O 3

# Replace a value
month["Jan"] = 'New Year'
print(month)
#O  {'Jan': 'New Year',
#O   'Feb': 'February',
#O   'Mar': 'March'}

# Delete an entry
del month["Jan"]
print(month)
#O {'Feb': 'February',
#O  'Mar': 'March'}

# Replace a value
month['Feb'] = 'Valentine'
print(month)
#O {'Feb': 'Valentine',
#O  'Mar': 'March'}


# Get the value for the passed key
print(month.get("Feb"))
#O Valentine

# Get a list of dictionary keys
print(month.keys())
#O dict_keys(['Feb', 'Mar'])

# Get a list of dictionary values
print(month.values())
#O dict_values(['Valentine', 'March'])

# CONDITIONALS ---------------------------------------------------------------------- CONDITIONAL STATEMENTS
# The if, else and elif statements are used to perform different
# actions based off of conditions
# Comparison Operators : ==, !=, >, <, >=, <=
# Code  == equal, != not equal, > Less , < higher , greater or equal >= , less or not equal <=

# The if statement will execute code if a condition is met
# White space is used to group blocks of code in Python
# Use the same number of proceeding spaces for blocks of code

age = 30
if age > 16 :
    print('You are old enough to drive')
#O You are old enough to drive

# Use an if statement if you want to execute different code regardless
# of whether the condition ws met or not

if age > 16 :
    print('You are old enough to drive')
else :
    print('You are not old enough to drive')
#O You are old enough to drive

# If you want to check for multiple conditions use elif
# If the first matches it won't check other conditions that follow

if age >= 21 :
    print('You are old enough to drive a tractor trailer')
elif age >= 16:
    print('You are old enough to drive a car')
else :
    print('You are not old enough to drive')
#O You are old enough to drive a tractor trailer

# You can combine conditions with logical operators
# Logical Operators : and, or, not

if ((age >= 1) and (age <= 18)):
    print("You get a birthday party")
elif (age == 21) or (age >= 65):
    print("You get a birthday party")
elif not(age == 30):
    print("You don't get a birthday party")
else:
    print("You get a birthday party yeah")
#O You get a birthday party yeah

#Example
male = True

if male:
    print("Male")
else:
    print("Not")
#O Male


# Code or
# Only one condition needs to be true for the condition to be executed,Code: or
# x = True , y = True  , condition is executed
# x = True , y = False , condition is executed
# x = False, y = True  , condition is executed
# x = False, y = false , else is executed (Default)
# Example
x = False
y = True

if x or y:
    print("x = True , y = True/ x = True , y = False / x = False , y = True ")
else:
    print("x = False , y = False")
#O x = True , y = True/ x = True , y = false / x = False , y = True


# Code and
# Both condition needs to be true for the condition to be executed, Code: and
# x = True  , y = True   , condition is executed
# x = True  , y = false  , else is executed (Default)
# x = False , y = True   , else is executed (Default)
# x = False , y = false  , else is executed (Default)
# Example
x = True
y = True

if x and y:
    print("x = True and y = True")
else:
    print("x = True but y = False / x = True but y =False / x = false and y = False")
#O x = True and y = True


# Code elif , not()
# Both condition needs to be true for the condition to be executed, Code: and
# x = True  , y = True   , condition is executed
# x = True  , y = False  , elif x and not(y): executed
# x = False , y = True   , elif not(x) and y: is executed
# x = False , y = False  , else is executed (Default)
# Example
x = False
y = True

if x and y:
    print("x = True and y = True")
elif x and not(y):
    print("x = True, y =  False")
elif not(x) and y:
    print("x = False, y = True")
else:
    print("x = False, y = False")
#O x = False, y = True

# Function
# Example
# This function prints out highest number/parameter you assign to it.
def maximum_number(number1, number2, number3):
    if number1 >= number2 and number1 >= number3:
        return number1
    elif number2 >=number1 and number2 >= number3:
        return number2
    else:
        return number3

print(maximum_number(10, 20, 30))
#O 30

# Calculator with condition statements
# Example
number1 = float(input("Enter first number: "))
operator = (input("Enter operator: "))
number2 = float(input("Enter second number: "))

if operator == "+":
    print(number1 + number2)
elif operator == "-":
    print(number1 - number2)
elif operator == "/":
    print(number1/number2)
elif operator == "*":
    print(number1 * number2)
else:
    print("Invalid operator")
#O Enter first number: 1
#O Enter operator: *
#O Enter second number: 2
#O 2.0

# FOR LOOPS ------------------------------------------------------------------------------------  LOOPS
# Enables to loop over different collections of string/arrays/etc
# Use same Array for all codes, but one at a time not all combined.?
# Allows you to perform an action a set number of times
# Range performs the action 10 times 0 - 9
for x in range(0, 10):
    print(x , ' ', end="")
#O 0  1  2  3  4  5  6  7  8  9

print('\n')

# You can use for loops to cycle through a list
grocery_list = ['Juice', 'Tomatoes', 'Potatoes', 'Bananas']

for y in grocery_list:
    print(y)
#O Juice
#O Tomatoes
#O Potatoes
#O Bananas

# You can also define a list of numbers to cycle through
for x in [2,4,6,8,10]:
    print(x)
#O 2 4 6 8 10

# You can double up for loops to cycle through lists
num_list =[[1,2,3],[10,20,30],[100,200,300]];

for x in range(0,3):
    for y in range(0,3):
        print(num_list[x][y])
#O 1 2 3 10 20 30 100 200 300

# Example with String
for letter in "Jose Bernardo":
    print(letter)
#O J o s e B e r n a r d o

# Examples with single Array
friends=["Edgar", "John", "Blake"]

for friends in friends:
    print(friends)
#O Edgar, John, Blake

for index in range(4):
    print(index)
#O 0, 1, 2, 3

for index in range(0,2):
    print(index)
#O 0, 1

for index in range(len(friends)):
    print(friends[index])
#O Edgar, John, Blake

for index in range(len(friends)):
    print(friends[2])
#O Blake Blake Blake

# Example as demonstration
print(2**3)
#O 8

# Example function with loop
def raise_to_power(base_number, pow_number):
    result = 1 #store result
    for index in range(pow_number):
        result = result * base_number
    return result

print(raise_to_power(2,3))
#O 8

# List with loops
# Example
# Array with elements
number_grid=[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
print(number_grid[0])
print(number_grid[2][1])

#O [1, 2, 3]
#O 8

# Example of Nested Loops
for row in number_grid:
    print(row)
#O [1, 2, 3][4, 5, 6][7, 8, 9][0]

for row in number_grid:
    for col in row:
        print(col)
#O 1, 2, 3, 4, 5, 4, 6, 7, 8, 9, 10,

# Translator
# Example
def translate(phrase):
    translation=""
    for letter in phrase:
        if letter in "OOooEEee":
            translation= translation+ "X"
        else:
            translation=translation+letter
    return translation

print(translate(input("Enter a phrase: ")))

#O Enter a Phrase: Jose
#O JXsX

# WHILE LOOPS ---------------------------------------------------------------------------- WHILE LOOPS DE

# While loops are used when you don't know ahead of time how many
# times you'll have to loop
random_num = random.randrange(0,100)

while (random_num != 15):
    print(random_num)
    random_num = random.randrange(0,100)
#O 75 53 38 40 8 70 10 2 21 44 87 13 31 26 96 77 36 66 97 35 57 65 20 42 86 47 23 11 18 87 74 20 98 82 66
#O 27 13 97 74 10 49 18 99 36 87 71 39 69 54 31 42 12 54 87 81 45 34 72 55 5 66 14 53 39 33 87 39 82
#O 61 78 56 40 4 84 88 51 75 62 90 81 46 62 71

# An iterator for a while loop is defined before the loop
i = 0;
while (i <= 20):
    if(i%2 == 0):
        print(i)
    elif(i == 9):
        # Forces the loop to end all together
        break
    else:
        # Shorthand for i = i + 1
        i += 1
        # Skips to the next iteration of the loop
        continue

    i += 1
#O 8

# WHILE LOOPS ---------------------------------------------------------------------------- WHILE LOOPS
# Is a structure, that allow loop execute through block of code multiple times, until certain condition is false
# While loops are used when you don't know ahead of time how many
# times you'll have to loop
import random

random_num = random.randrange(0,100)

while (random_num != 15):
    print(random_num)
    random_num = random.randrange(0,100)
#O 75 53 38 40 8 70 10 2 21 44 87 13 31 26 96 77 36 66 97 35 57 65 20 42 86 47 23 11 18 87 74 20 98 82 66
#O 27 13 97 74 10 49 18 99 36 87 71 39 69 54 31 42 12 54 87 81 45 34 72 55 5 66 14 53 39 33 87 39 82
#O 61 78 56 40 4 84 88 51 75 62 90 81 46 62 71

print("break")
# An iterator for a while loop is defined before the loop
i = 0;
while (i <= 20):
    if(i%2 == 0):
        print(i)
    elif(i == 9):
        # Forces the loop to end all together
        break
    else:
        # Shorthand for i = i + 1
        i += 1
        # Skips to the next iteration of the loop
        continue

    i += 1
#O 8

# Example
i = 1
while i <= 10:
    print(i)
    i=i+1

#O 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,

#-------------------------------------------------------------------------------------- Function

# Functions
        # Collection of code that performs specific task(procedure)"call"
        # Lot of functions are built in program and allows you to do things
                #without telling specific instructions.(Mathematical Formula) E = mc2
        #Allows you reuse and it eliminate repetitive code
        #information you write inside of function is called parameter
        #rule name the function all lower case, you can use underscore_
# Code def  ,enables you to create a function
# Order of code is executed in a customized function is different for example:
# 1Code print("Top")
# 2Code sayhi()
# 3Code def sayhi():
    #Code print("This is the function string")
# 4Code print("bottom")
# Code def watever():
                #the code has to be indented, to be inside of function, to work
# Function code will not be called by default, you need to execute it by calling it for example: return
# Example
def sayhi():
    print("This is the function string")

print("Top")
sayhi()
print("Bottom")
#O Top
#O This is the function string
#O Bottom

# Functions
# name, age the is the parameters
# Example
def sayhi(name, age):
    print("Hello " + name +" you are "+ str(age))

sayhi(" Jose", 30)
sayhi(" Bernardo", 18)
#O Hello Jose you are 30
#O Hello Bernardo you are 18
#-------------------------------------------------------------------------------------- Function with Return
# Return Statement
# Attain information back from the function
# Is either "return" or "return value", where value is a variable or other information
# coming back from the subroutine.
# 3^3
# result variable is going to store the value, that gets executing the function cube, its not gone store cube(4)
# Example
def cube(num):
    return num*num*num
    # print("this code here will not work, because you ended the function with return")
    # Code return ,ends operation , if you put code inside the function it will not be executed
    # code return ,it breaks is out of the function

print(cube(3))
#O 27

# Build a Translator
# Example
def translate(phrase):
    translation=""
    for letter in phrase:
        if letter in "OOooEEee":
            translation= translation+ "X"
        else:
            translation=translation+letter
    return translation

print(translate(input("Enter a phrase: ")))

#O Enter a Phrase: Jose
#O JXsX

# USER INPUT ---------------------------------------------------------------------------- USER INPUT DE
import sys

print('What is your name?')
#O What is your name?

# Stores everything typed up until ENTER
name = sys.stdin.readline()

print('Hello', name)
#O What is your name?
#O
#O Hello Jose


# Building A Basic Calculator
# Order of operations don't work with strings, you need convert strings into integers
# Code int() ,is a function, it converts a string into a integer/whole number, only works with whole numbers
# Code float() ,is a function, it converts a string into integer/Decimal numbers, only works with decimal numbers
# Example
number1 = input("Enter a number: ")
number2 = input("Enter another number: ")
result = int(number1) + int(number2)
print(result)
#O Enter a number: 1
#O Enter another number: 1
#O 2

# Mad Libs Game
# Example
color = input("Enter a color:")
plural_noun = input("Enter a Plural Noun:")
celebrity = input("Enter a celebrity")
print("Roses are "+color)
print( plural_noun+ " are blue")
print("I Love "+celebrity)
#O Enter a color:black
#O Enter a Plural Noun:Ships
#O Enter a celebrityLana Del Ray
#O Roses are black
#O Ships are blue
#O I Love Lana Del Ray

# FILE I/O ------------------------------------------------------------------------------------ FILE I/O DE

# Overwrite or create a file for writing
test_file = open("test.txt", "wb")

# Get the file mode used
print(test_file.mode)
#O wb

# Get the files name
print(test_file.name)
#O test.txt

print("\n")

# Write text to a file with a newline
test_file.write(bytes("Write me to the file\n", 'UTF-8'))
#O Write me to the file

# Close the file
test_file.close()

# Opens a file for reading and writing
test_file = open("test.txt", "r+")

# Read text from the file
text_in_file = test_file.read()

print(text_in_file)
#O

# Delete the file
os.remove("test.txt")

#-------------------------------------------------------------------------------------------- Reading Files

# Reading Files
# reading from external files such as text file, csv file, html file
# Parameter: "r" ,reading mode only
# Example "Checking" to see if program can read the file  #.readable
variable=open("testdocument.txt", "r")
print(variable.readable())
variable.close()
#O True

# Example "Reading" the file entire
variable=open("testdocument.txt", "r")
print(variable.read())

variable.close()
#O Chevy, Ford, Cadillac, GMC

# Example Reading Single line
variable=open("testdocument.txt", "r")
print(variable.readline())   #reads first line
print(variable.readline())   #reads second line

variable.close()
#O Chevy
#O Ford

# Reading Files
# Example puts lines of file into a list
variable=open("testdocument.txt", "r")
print(variable.readlines())

variable.close()
#O ['Chevy\n', 'Ford\n', 'Cadillac\n', 'GMC']

# Reading Files
# Example, index of one is Ford
variable=open("testdocument.txt", "r")
print(variable.readlines()[1])

variable.close()
#O Ford
#------------------------------------------------------------------------------------------ Writing to files

# Writing to files
# Example Appending  "a"
# Parameter: "a"   , enables you write on the document
# You need \n to write into new line, or else it will write on existing line
variable=open("testdocument.txt", "a")
variable.write("\n Honda")
print(variable.read())

variable.close()
#O Does not Print, Writes word Honda into new line in the document text

# Example Overriding File
# Parameter:  "w" ,enables you override a document(Erase Everything then add your writing)
variable=open("testdocument.txt", "w")
variable.write(" Honda")
print(variable.read())

variable.close()
#O Does not Print, Erases Everything, writes word Honda on file

# Example Creating New File
# added 1 at  testdocument.txt" and it creates new file when you run it
variable=open("testdocument1.txt", "w")
variable.write(" Honda")

variable.close()
#O Does not Print, It creates new file

# Example Overriding File
# Parameter:  "w" changed "testdocument" to "index.html" and it created new html file
variable=open("index.html", "w")
variable.write("<p>This is new HTML File <P>")
print(variable.read())

variable.close()
#O Does not Print, Creates New HTML file

# CLASSES AND OBJECTS ----------------------------------------------------------------------  CLASSES AND OBJECTS
# Object Functions
# Object Function is used inside of a class and can modify the objects for that class,
# or give specific information about those objects
# The concept of OOP allows us to model real world things using code
# Every object has attributes (color, height, weight) which are object variables
# Every object has abilities (walk, talk, eat) which are object functions

# Building a Multiple Choice Quiz
# Example
# Questions and Answers strings
question_prompts = [
    "What color are Apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are Bananas?\n(a) Teal/Green\n(b) Magenta\n(c) Yellow\n\n",
    "What color are Strawberries?\n(a) Yellow/Green\n(b) Red\n(c) Blue\n\n"
]

# Class to store questions and answers
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer= answer

# A2 Array of objects "right answers"
questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
]

# function of objects
def run_test(questions):                    # questions is the parameter for the questions to ask user
    score=0                                 # Variable to increment the score variable
    for question in questions:              # loop through the questions  "array' in Objects
        answer =  input(question.prompt)    # answer variable
        if answer == question.answer:       # To check if answer is right condition
            score += 1                      # If this is executed
            print("You got " + str(score) + "/" + str(len(questions)) + " Correct")

run_test(questions)

#O What color are Apples?
#O (a) Red/Green
#O (b) Purple
#O (c) Orange
#O a
#O You got 1/3 Correct

#O  color are Bananas?
#O (a) Teal/Green
#O (b) Magenta
#O (c) Yellow
#O c
#O You got 2/3 Correct

#O What color are Strawberries?
#O (a) Yellow/Green
#O (b) Red
#O (c) Blue
#O b
#O You got 3/3 Correct


class Animal:
    # None signifies the lack of a value
    # You can make a variable private by starting it with __
    __name = None
    __height = None
    __weight = None
    __sound = None

    # The constructor is called to set up or initialize an object
    # self allows an object to refer to itself inside of the class
    def __init__(self, name, height, weight, sound):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound

    def set_name(self, name):
        self.__name = name

    def set_height(self, height):
        self.__height = height

    def set_weight(self, height):
        self.__height = height

    def set_sound(self, sound):
        self.__sound = sound

    def get_name(self):
        return self.__name

    def get_height(self):
        return str(self.__height)

    def get_weight(self):
        return str(self.__weight)

    def get_sound(self):
        return self.__sound

    def get_type(self):
        print("Animal")

    def toString(self):
        return "{} is {} cm tall and {} kilograms and says {}".format(self.__name, self.__height, self.__weight, self.__sound)

# How to create a Animal object
cat = Animal('Whiskers', 33, 10, 'Meow')

print(cat.toString())
#O Whiskers is 33 cm tall and 10 kilograms and says Meow

# You can't access this value directly because it is private
# print(cat.__name)

# INHERITANCE ----------------------------------------------------------------------------------------- INHERITANCE DE
# You can inherit all of the variables and methods from another class

class Dog(Animal):
    __owner = None

    def __init__(self, name, height, weight, sound, owner):
        self.__owner = owner
        self.__animal_type = None

        # How to call the super class constructor
        super(Dog, self).__init__(name, height, weight, sound)

    def set_owner(self, owner):
        self.__owner = owner

    def get_owner(self):
        return self.__owner

    def get_type(self):
        print ("Dog")

    # We can overwrite functions in the super class
    def toString(self):
        return "{} is {} cm tall and {} kilograms and says {}. His owner is {}".format(self.get_name(), self.get_height(), self.get_weight(), self.get_sound(), self.__owner)

    # You don't have to require attributes to be sent
    # This allows for method overloading
    def multiple_sounds(self, how_many=None):
        if how_many is None:
            print(self.get_sound)
        else:
            print(self.get_sound() * how_many)

spot = Dog("Spot", 53, 27, "Ruff", "Derek")

print(spot.toString())
#O Spot is 53 cm tall and 27 kilograms and says Ruff. His owner is Derek


# Polymorphism allows use to refer to objects as their super class
# and the correct functions are called automatically

class AnimalTesting:
    def get_type(self, animal):
        animal.get_type()

test_animals = AnimalTesting()

test_animals.get_type(cat)
test_animals.get_type(spot)

spot.multiple_sounds(4)

# Building a Guessing Game
# Variables, if statement with comparison operators While Loop, Input,

secret_word = "Jose"
user_guess =""
user_guess_count=0
user_guess_limit = 3
user_out_of_guesses= False

while user_guess != secret_word and not(user_out_of_guesses):
    if user_guess_count < user_guess_limit:
       user_guess = input("Enter guess: ")
       user_guess_count += 1
    else:
     user_out_of_guesses= True

if user_out_of_guesses:
    print("You Loose")
else:
  print("You win")
#O Animal Dog RuffRuffRuffRuff Enter guess:
#O Enter guess:
#O Enter guess:
#O Enter guess:
#O You win

# Example has no Inheritance, but shows why you need it to use inheritance
# Cheff can make 3 actions
class Chef:
    def make_chicken(self):
        print("The chef makes a chicken")

    def make_salad(self):
        print("the chef makes a salad")

    def make_special_dish(self):
        print("the chef make a BBQ ribs")


# The Chinese chef can do everything regular chef can, plus more
class ChineseChef:
    def make_chicken(self):
        print("The chef makes a chicken")

    def make_salad(self):
        print("the chef makes a salad")

    def make_special_dish(self):
        print("the chef make a orange chicken")

    def make_fried_rice(self):
        print("The chef makes fried rice")

# Object
myChef = Chef()
myChef.make_special_dish()

myChineseChef = ChineseChef()
myChineseChef.make_fried_rice()

#O the chef make a BBQ ribs
#O The chef makes fried rice

# Example with inheritance
# Chef can make 3 actions
class Chef:
    def make_chicken(self):
        print("The chef makes a chicken")

    def make_salad(self):
        print("the chef makes a salad")

    def make_special_dish(self):
        print("the chef make a BBQ ribs")


# The Chinese chef can do everything regular chef can, plus more
# Instead of copying/paste all functions to the file you can use inheritance
# (Chef) Inheritance ,enables to use all functions of chef class
class ChineseChef(Chef):

    def make_fried_rice(self):
        print("The chef makes fried rice")

# Overrides make_special_dish from chef class function
    def make_special_dish(self):
        print("the chef make a Orange Chicken")

# Object
myChef = Chef()
myChef.make_special_dish()

myChineseChef = ChineseChef()
myChineseChef.make_fried_rice()
myChef.make_special_dish()

#O the chef make a BBQ ribs
#O The chef makes fried rice
#O the chef make a BBQ ribs

#-----------------------------------------------------------------------------------------------  Try Except
# Try Except
# If error occurs,"else" is executed
# Example
try:
    number = int(input("Enter a number: "))
    print(number)
except:
    print("Invalid Input")

#O Enter Number: Zero
#O Invalid Input

# Example with two "else" Try Except
try:
    Value = 10/0   #Error
    number = int(input("Enter a number: "))
    print (number)
except ZeroDivisionError:
    print("Divided by zero error")
except ValueError:
    print("Invalid Input")

#O Divided by Zero Error

# Example Try Except with, "else", containing information about specific error
try:
    answer= 10/0
    Value = 10/0   #Error
    number = int(input("Enter a number: "))
    print (number)
except ZeroDivisionError as Error:
    print("Error")
except ValueError:
    print("Invalid Input")

#O Error

#----------------------------------------------------
# You can use python on CMD, but you have install on command prompt


