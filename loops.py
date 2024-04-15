
# loops

# Python If ... Else
print("\n")
x = 9
y = 10
if 10 > 9:
    print("y is greater then x")


# Elif
# The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition"
print("\n")
x = 10
y = 9
if 10 < 9:
    print("x is less than y")
elif 10 > 9:
    print("x is greater than y")


# else
# The else keyword catches anything which isn't caught by the preceding conditions.
print("\n")
x = 100
b = 200
if x > b:
    print("x is greater than b")
elif x == b:
    print("x and b are equal")
else:
    print("x is less than b")


# Short Hand If
# If you have only one statement to execute, you can put it on the same line as the if statement.
print("\n")
a = 5
b = 2
if a > b: print("a greater than b")


# Short Hand If ... Else
# If you have only one statement to execute, one for if, and one for else, you can put it all on the same line
print("\n")
a = 12
b = 22
print("true") if a < b else print("false")
# This technique is known as Ternary Operators, or Conditional Expressions.

print("\n")
a = 10
b = 10
print("true") if a > b else print("both equal") if a==b else print("false")


#And
# The and keyword is a logical operator, and is used to combine conditional statements
print("\n")
a = 10
b = 20
c = 5
if a < b and a > c:
    print("both are true")

#Or
# The or keyword is a logical operator, and is used to combine conditional statements:
print("\n")
a = 10
b = 20
c = 5
if a < b or a < b:
    print("at least one condition is true ")


# Not
# The not keyword is a logical operator, and is used to reverse the result of the conditional statement
print("\n")
a = 10
b = 20
if not a > b:
    print("true")
else:
    print("false")

# Nested If
# You can have if statements inside if statements, this is called nested if statements.
print("\n")
x = 15
if x > 10:
    print("x is above 10")
    if x > 20:
        print(" also x is above 20")
    else:
        print("x is not above 20")

# The pass Statement
# You can have if statements inside if statements, this is called nested if statements.
print("\n")
x = 10
y = 20
if x < y:
    pass



# Python Loops

# primitive loop :
# while loop
# for loop

# The while Loop
# while loop we can execute a set of statements as long as a condition is true.
print("\n")
i = 1
while i < 6:
    print(i)
    i += 1

# The break Statement
# break statement we can stop the loop even if the while condition is true
print("\n")
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# The continue Statement
# continue statement we can stop the current iteration, and continue with the next
print("\n")
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

# The else Statement
# else statement we can run a block of code once when the condition no longer is true
print("\n")
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer then 6")


# Python For Loops
print("\n")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

# Looping Through a String
print("\n")
for x in "cherry":
    print(x)

# The break Statement
# break statement we can stop the loop before it has looped through all the items
print("\n")
fruits = ("apple", "banana", "cherry", "mango")
for x in fruits:
    print(x)
    if x == "cherry":
        break

print("\n")
fruits = ("apple", "banana", "cherry", "mango")
for x in fruits:
    if x == "cherry":
        break
    print(x)


# The continue Statement
# continue statement we can stop the current iteration of the loop, and continue with the next
print("\n")
fruits = {"apple", "banana", "cherry", "chiku"}
for x in fruits:
    if x == "banana":
        continue
    print(x)


# The range() Function
# loop through a set of code a specified number of times, we can use the range() function
print("\n")
for x in range(6):
    print(x)
#OR
print("\n")
for y in range(2, 6):
    print(y)
#OR
print("\n")
for z in range(2,20,3):
    print(z)


# Else in For Loop
# The else keyword in a for loop specifies a block of code to be executed when the loop is finished
print("\n")
for x in range(6):
    print(x)
else:
    print("loop end")

#OR
print("\n")
for x in range(6):
    if x == 3:
        break
    print(x)
else:
    print("loop end")


# Nested Loops
# A nested loop is a loop inside a loop.
print("\n")
color = ["red", "yellow", "pink"]
fruits = ["banana", "cherry", "chiku"]
for x in color:
    for y in fruits:
     print(x, y)

# The pass Statement
# for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.
print("\n")
for x in [0, 1, 2]:
    pass

