
# Tuple(Tuples are used to store multiple items in a single variable.)
# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.

print("\n")
mytuple = ("apple", "chiku", "kiwi")
print(mytuple)


# Allow Duplicates tuple
print("\n")
mytuple = ("apple", "banana", "chiku", "apple")
print(mytuple)


# Tuple Length
# To determine how many items a tuple has, use the len() function
print("\n")
mytuple = ("apple", "banana", "orange", "cherry")
print(len(mytuple))


# Create Tuple With One Item
#To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple
print("\n")
mytuple = ("orange",)
print(type(mytuple))

# not tuple
mytuple = ("orange")
print(type(mytuple))


# Tuple Items - Data Types
# Tuple items can be of any data type
print("\n")
mytuple1 = ("apple", "kiwi", "banana")
mytuple = (1, 2, 3)
mytuple2 = (True, False, True)

print(mytuple)
print(mytuple2)
print(mytuple1)

# A tuple can contain different data types
print("\n")
mytuple = ("apple", 2, True, "orange", 3)
print(mytuple)


# Type()
# From Python's perspective, tuples are defined as objects with the data type 'tuple'
print("\n")
mytuple = ("vidhi", "deep", "ekta")
print(type(mytuple))

# The tuple() Constructor
# It is also possible to use the tuple() constructor to make a tuple.
print("\n")
mytuple = tuple(("Vidhi", "Ekta", "Deep")) # note the double round-brackets
print(mytuple)


# Access Tuple Items
# You can access tuple items by referring to the index number, inside square brackets
print("\n")
mytuple = ("orange", "apple", "kiwi", "banana")
print(mytuple[2])

# Negative Indexing
# Negative indexing means start from the end.
print("\n")
mytuple = ("kiwi", "banana", "apple", "orange")
print(mytuple[-2])

# Range of Indexes
# You can specify a range of indexes by specifying where to start and where to end the range
print("\n")
mytuple = ("banana", "kiwi", "apple", "cherry", "chiku", "orange")
print(mytuple[1:5])

# Check if Item Exists
print("\n")
mytuple = ("apple", "banana", "kiwi", "orange")
if "apple" in mytuple:
    print("yes, 'apple' is in the mytuple list")


# Change Tuple Values
# You can convert the tuple into a list, change the list, and convert the list back into a tuple.
print("\n")
x = ("apple", "orange", "banana")
y = list(x)
y[1] = ("kiwi")
x = tuple(y)
print(x)


# Add Items
# Just like the workaround for changing a tuple, you can convert it into a list, add your item(s), and convert it back into a tuple.
print("\n")
a = ("vidhi", "ekta", "deep")
b = list(a)
b.append("savan")
a = tuple(b)
print(a)


# Add tuple to a tuple.
# You are allowed to add tuples to tuples, so if you want to add one item, (or many), create a new tuple with the item(s), and add it to the existing tuple
print("\n")
mytuple = ("cherry", "mango", "orange")
x = ("apple",)
mytuple += x
print(mytuple)


# Remove Items
print("\n")
c = ("vidhi", "ekta", "deep", "savan")
d = list(c)
d.remove("savan")
c = tuple(d)
print(c)

# Unpacking a Tuple
# in Python, we are also allowed to extract the values back into variables. This is called "unpacking"
print("\n")
mytuple = ("apple", "orange", "kiwi")
(deep, vidhi, ekta) = mytuple
print(deep)
print(vidhi)
print(ekta)


# Using Asterisk*
# If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list
print("\n")
mytuple = ("orange", "kiwi", "banana", "cherry", "mango")
(vidhi, deep, *ekta) = mytuple
print(vidhi)
print(deep)
print(ekta)


# Loop Through a Tuple
# You can loop through the tuple items by using a for loop
print("\n")
mytuple = ("ekta", "vidhi", "deep")
for x in mytuple:
    print(x)


# Loop Through the Index Numbers
# You can also loop through the tuple items by referring to their index number.
# Use the range() and len() functions to create a suitable iterable
print("\n")
mytuple = ("banana", "apple", "cherry")
for x in range(len(mytuple)):
    print(mytuple[x])

# Using a While Loop
# You can loop through the tuple items by using a while loop.
print("\n")
mytuple = ("orange", "banana", "chiku")
i = 0
while i < len(mytuple):
    print(mytuple[i])
    i = i + 1


# Join Two Tuples
# To join two or more tuples you can use the + operator
print("\n")
mytuple = ("vidhi", "ekta", "deep")
mytuple1 = (1, 2, 3)
x = mytuple + mytuple1
print(x)

# Multiply Tuples
# If you want to multiply the content of a tuple a given number of times, you can use the * operator
print("\n")
fruits = ("kiwi", "cherry", "mango")
mytuple = fruits * 2
print(mytuple)


# count()
# Returns the number of times a specified value occurs in a tuple
print("\n")
mytuple = ("vidhi", "ekta", "deep", "vidhi", "savan")
x = mytuple.count("vidhi")
print(x)

# index()
# Searches the tuple for a specified value and returns the position of where it was found
print("\n")
mytuple = ("orange", "apple", "mango", "cherry", "banana")
y = mytuple.index("cherry")
print(y)



print("\n")
mytuple = ("orange", "kiwi", "banana", "chiku")
(vidhi, *deep, ekta) = mytuple
print(vidhi)
print(deep)
print(ekta)




 # vartiable name should be proper with same convention
# do add comments
# input:
# Enter a number:
# Enter second number:
# addition of ____ and ____ = _____
# subtraction " " " " =______

"""Num1 = int(input("Enter a number:"))
Num2 = int(input("Enter second number:"))

print("1. Addition" "\n"
      "2. Subtraction" "\n"
      "3. Multiplication" "\n"
      "4. Division" "\n"
      "5. Modulus")

Operation = int(input("Select operation:"))
def Add(Num1, Num2):
    return (Num1 + Num2)

def Sub(Num1, Num2):
    return (Num1 - Num2)

def Mul(Num1, Num2):
    return (Num1 * Num2)

def Div(Num1, Num2):
    return (Num1 / Num2)

def Mod(Num1, Num2):
    return (Num1 % Num2)

if Operation == 1:
    print(Num1, "+", Num2, "=", Add(Num1, Num2))

elif Operation == 2:
    print(Num1, "-", Num2, "=", Sub(Num1, Num2))"""
