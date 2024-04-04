

print("python List")

# List (Lists are used to store multiple items in a single variable.)
print("\n")
mylist = ["Vidhi", "Ekta", "Deep", "Savan"]
print(mylist)


# Duplicates (Lists allow duplicate values)
print("\n")
mylist = ["Vidhi", "Ekta", "Deep", "Savan", "Ekta", "Vidhi"]
print(mylist)


# List Length (To determine how many items a list has, use the len() function)
print("\n")
mylist = ["Vidhi", "Ekta", "Deep", "savan"]
print(len(mylist))


# List Items - Data Types
print("\n")
mylist = ["Vidhi", 1498, "Ekta", True, "Deep"]
print(mylist)


# type (Python's perspective, lists are defined as objects with the data type 'list')
print("\n")
mylist = ["Vidhi", "Ekta", "Deep", True, 123]
print(type(mylist))
newlist = {"Ekta", "Deep", 2510, "Vidhi"}
print(type(newlist))
list1 = ("Deep", True, "Vidhi", "Ekta")
print(type(list1))
thisdict = {
    "name": "vidhi",
    "age": "26",
    "gender": "female"
}
print(type(thisdict))


# list() Constructor (Using the list() constructor to make a List)
# It is also possible to use the list() constructor when creating a new list
print("\n")
mylist = list(("Vidhi", "Ekta", True, 1498, "Deep")) # note the double round-brackets
print(mylist)

# Access Items (List items are indexedand you can access them by referring to the index number)
print("\n")
thislist = ["apple", "Banana", "Cherry"]
print(thislist[1])


#Range of Indexes
print("\n")
mylist = ["apple", "banana", "cherry", "kivi", "mango", "chiku"]
print(mylist[2:5])


#Range of Negative Indexes
print("\n")
mylist = ["apple", "banana", "cherry", "kivi", "mango", "chiku"]
print(mylist[-5:-1])


#Check if Item Exists
print("\n")
mylist = ["apple", "banana", "cherry", "kivi", "mango", "chiku"]
if "cherry" in mylist:
    print("yes", "cherry is fruit")


#Change Item Value (To change the value of a specific item, refer to the index number)
print("\n")
mylist = ["apple", "banana", "cherry"]
mylist[1] = ["mango"]
print(mylist)


#Change a Range of Item Values
print("\n")
mylist = ["apple", "banana", "cherry"]
mylist[1:2] = ["mango", "kivi"]
print(mylist)


#Insert Items (To insert a new list item, without replacing any of the existing values, we can use the insert() method)
print("\n")
mylist = ["apple", "banana", "kiwi", "cherry", "mango"]
mylist.insert(2, "chiku")
print(mylist)


#Append Items (To add an item to the end of the list, use the append() method)
print("\n")
mylist = ["apple", "banana", "cherry"]
mylist.append("kiwi")
print(mylist)


#Extend List (To append elements from another list to the current list, use the extend() method.)
print("\n")
mylist = ["apple", "banana", "chiku"]
x = ["kivi", "cherry", "mango"]
mylist.extend(x)
print(mylist)


#Add Any Iterable (The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.)\
print("\n")
mylist = ["apple", "banana", "cherry"]
thistuple = ("chiku", "kiwi", "mango")
mylist.extend(thistuple)
print(mylist)


#Remove Specified Item
print("\n")
mylist = ["apple", "banana", "kiwi", "chiku"]
mylist.remove("kiwi")
print(mylist)


#Remove Specified Index (The pop() method removes the specified index)
print("\n")
mylist = ["apple", "banana", "cherry"]
mylist.pop(1)
mylist.pop() # If you do not specify the index, the pop() method removes the last item
print(mylist)


#delete (The del keyword also removes the specified index)
print("\n")
mylist = ["apple", "banana", "cherry",]
del mylist[0]
print(mylist)


#Clear the List (The clear() method empties the list)
print("\n")
mylist = ["apple", "banana", "chiku"]
mylist.clear()
print(mylist)


#Loop Through a List (Print all items in the list, one by one:)
print("\n")
mylist = ["apple", "banana", "kiwi", "chiku"]
for x in mylist:
    print(x)


#Loop Through the Index Numbers
print("\n")
mylist = ["apple", "banana", "chiku"]
for x in range(len(mylist)):
    print(x, mylist[x])


# Using a While Loop (Print all items, using a while loop to go through all the index numbers)
print("\n")
mylist = ["apple", "Kiwi", "banana"]
x = 0
while x < len(mylist):
    print(mylist[x])
    x = x + 1


# List Comprehension (List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.)
print("\n")
mylist = ["apple", "banana", "kiwi", "orange", "cherry"]
newlist = []
for y in mylist:
    if 'a' in y:
        newlist.append(y)
print(newlist)

# same syntax write in one line
print("\n")
mylist = ["apple", "banana", "kiwi", "mango", "cherry"]
newlist = [x for x in mylist if 'a' in x]
print(newlist)


#Condition (The condition is like a filter that only accepts the items that valuate to True)
print("\n")
mylist = ["apple", "banana", "kiwi", "cherry",]
newlist = [x for x in mylist if x != 'banana']
print(newlist)


# Iterable (The iterable can be any iterable object, like a list, tuple, set etc)
# You can use the range() function to create an iterable
print("\n")
newlist = [x for x in range(10)]
print(newlist)
#with condition
newlist = [x for x in range(10) if x < 7]
print(newlist)


# Expression (The expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list)
print("\n")
mylist = ["apple", "banana", "kiwi", "cherry"]
newlist = [x.upper() for x in mylist]
print(newlist)

# other example
print("\n")
mylist = ["apple", "banana", "kiwi", "chiku"]
newlist = ['hello' for x in mylist]
print(newlist)

print("\n")
mylist = ["apple", "banana", "kiwi", "chiku"]
print(mylist)
newlist = [x if x != 'banana' else 'orange' for x in mylist]
print(newlist)


# Sort List Alphanumerically
# List objects have a sort() method that will sort the list alphanumerically, ascending, by default
print("\n")
mylist = ["apple", "orange", "kiwi", "mango", "cherry"]
mylist.sort()
print(mylist)

# Numerically sort
mylist = [23, 67, 4, 58, 100]
mylist.sort()
print(mylist)


#  Sort Descending
#To sort descending, use the keyword argument reverse = True
print("\n")
mylist = ["cherry", "mango", "kiwi", "apple"]
mylist.sort(reverse = True)
print(mylist)
mylist1 = [2, 78, 43, 100, 50]
mylist1.sort(reverse=True)
print(mylist1)


'''#Customize Sort Function (problem)
print("\n")
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)'''


# Case Insensitive Sort
# By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters
print("\n")
mylist = ["banana", "Apple", "chiku", "Kiwi", "Mango"]
mylist.sort()
print(mylist)

print("\n")
# Key function
mylist = ["banana", "Orange", "Kiwi", "cherry", "chiku"]
mylist.sort(key=str.lower)
print(mylist)

# Reverse Order (The reverse() method reverses the current sorting order of the elements.)
print("\n")
mylist = ["apple", "cherry", "banana", "kiwi"]
mylist.reverse()
print(mylist)


# Copy a List (There are ways to make a copy, one way is to use the built-in List method copy())
print("\n")
mylist = ["apple", "kiwi", "mango"]
print("mylist =", mylist)
newlist = mylist.copy()
print("newlist =", newlist)

# other example of copy
print("\n")
mylist = ["apple", "kiwi", "orange"]
print("mylist =", mylist)
newlist = list(mylist)
print("newlist =", newlist)


# Join Two Lists(One of the easiest ways are by using the + operator)
print("\n")
mylist1 = ["a", "b", "c"]
mylist2 = [1,2,3]
mylist3 = mylist1 + mylist2
print(mylist3)

# other way to join using append
print("\n")
mylist1 = ["a", "b", "c"]
mylist2 = [1, 2, 3]
for x in mylist2:
     mylist1.append(x)
print(mylist1)

# Or you can use the extend() method, where the purpose is to add elements from one list to another list
print("\n")
mylist1 = ["a", "b", "c"]
mylist2 = [1, 2, 3]
mylist1.extend(mylist2)
print(mylist1)

# append() (Adds an element at the end of the list)
print("\n")
mylist = ["apple", "orange", "cherry"]
mylist.append("chiku")
print(mylist)

# another way to append list
print("\n")
mylist1 = ["vidhi"]
mylist2 = ["deep"]
mylist1.append(mylist2)
print(mylist1)

# clear() (Removes all the elements from the list)
print("\n")
mylist = ["apple", "banana", "cherry"]
mylist.clear()
print(mylist)


# copy()	Returns a copy of the list
print("\n")
mylist = ["apple", "cherry", "mango", "kiwi"]
x = mylist.copy()
print(x)


# count() (Returns the number of time elements appears in the list)
print("\n")
mylist = ["apple", "kiwi", "cherry", "orange", "cherry"]
x = mylist.count("cherry")
print(x)


# extend() (Add the elements of a list (or any iterable), to the end of the current list)
print("\n")
mylist1 = ["apple", "banana", "cherry", "chiku"]
mylist2 = [11, 12, 13, 14]
mylist1.extend(mylist2)
print(mylist1)

# index() (Returns the index of the first element with the specified value)
# The index() method returns the position at the first occurrence of the specified value
print("\n")
mylist = ["apple", "chiku", "cherry", "orange", "cherry"]
x = mylist.index("cherry")
print(x)


# insert() (Adds an element at the specified position)
print("\n")
mylist = ["apple", "chiku", "banana", "mango"]
mylist.insert(3,"kiwi")
print(mylist)


# pop() (Removes the element at the specified position)
print("\n")
mylist = ["apple", "chiku", "banana", "mango"]
mylist.pop(1)
print(mylist)


# remove() (Removes the item with the specified value)
print("\n")
mylist = ["apple", "chiku", "banana", "mango"]
mylist.remove("mango")
print(mylist)

# reverse() (Reverses the order of the list)
print("\n")
mylist = ["apple", "chiku", "cherry", "kiwi"]
mylist.reverse()
print(mylist)

# sort() (Sorts the list)
# The sort() method sorts the list ascending by default.
print("\n")
mylist = ["apple", "chiku", "kiwi", "cherry"]   
mylist.sort()
print(mylist)


# Sort the list descending
print("\n")
mylist = ["apple", "chiku", "kiwi", "cherry"]
mylist.sort(reverse=True)
print(mylist)




