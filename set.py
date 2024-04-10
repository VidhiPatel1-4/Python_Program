
# Python Set
# Sets are used to store multiple items in a single variable.
myset = {"vidhi", "deep", "ekta"}
print(myset)

# Note: the set list is unordered, meaning: the items will appear in a random order.

# Unchangeable set
# Set items are unchangeable, meaning that we cannot change the items after the set has been created.
# Once a set is created, you cannot change its items, but you can remove items and add new items.

# Add element from set
print("\n")
myset = {"apple", "orange", "cherry"}
myset.add("banana")
print(myset)


# Remove element from set
print("\n")
myset = {"apple", "orange", "cherry", "banana"}
myset.remove("banana")
print(myset)


# Duplicates Not Allowed
# Sets cannot have two items with the same value.
print("\n")
myset = {"vidhi", "ekta", "deep", "ekta"}
print(myset)


# True and 1 is considered the same value
# False and 0 is considered the same value
print("\n")
myset = {"apple", "cherry", "banana", True, 1, 2}
myset2 = {"apple", "chiku", "mango", False, 0, 1}
print(myset)
print(myset2)


# Get the Length of a Set
# To determine how many items a set has, use the len() function.
print("\n")
myset = {"vidhi", "ekta", "deep", "savan"}
myset = len(myset)
print(myset)

# Set Items - Data Types
print("\n")
set1 = {"vidhi", "deep", "ekta"}
set2 = {1, 2, 3}
set3 = {True, False, True}

print(set1)
print(set2)
print(set3)

# A set can contain different data types
print("\n")
myset = {"apple", "chiku", True, 10, "banana", False, 20}
print(myset)


# type()
print("\n")
myset = {"orange", "mango", "chiku"}
print(type(myset))


# set() Constructor
print("\n")
myset = set(("vidhi", "ekta", "deep"))
print(myset)

# Access Items
# You cannot access items in a set by referring to an index or a key
# loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.
print("\n")
myset = {"apple", "banana", "cherry"}
for x in myset:
    print(x)

# Check the value in set
print("\n")
myset = {"apple", "banana", "cherry"}
print("banana" in myset)

# Check the value NOT in set
print("\n")
myset = {"apple", "banana", "cherry"}
print("banana" not in myset)

# add item
# To add one item to a set use the add() method.
print("\n")
myset = {"vidhi", "ekta", "deep"}
myset.add("savan")
print(myset)

# Add Sets
# To add items from another set into the current set, use the update() method.
print("\n")
myset = {"mango", "chiku", "kiwi"}
myset1 = {"pineapple", "papaya", "apple"}
myset.update(myset1)
print(myset)

# Add Any Iterable
# The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
print("\n")
myset = {"vidhi", "ekta"} # set
myset1 = ["deep", "savan"] # list
myset2 = (1, 2) # tuple
myset.update(myset1, myset2)
print(myset)

# Remove Item
# To remove an item in a set, use the remove(), or the discard() method.
print("\n")
myset = {"apple", "kiwi", "mango", "chiku"}
myset.remove("kiwi") # if value does not exist remove() raise error
#OR
myset.discard("chiku") # if value does not exit discard() not raise error
print(myset)


# pop()
# pop() method remove random item
print("\n")
myset = {"vidhi", "deep", "ekta"}
myset.pop()
print(myset)

# clear()
# The clear() method empties the set
print("\n")
myset = {"apple", "mango", "orange"}
myset.clear()
print(myset)


"""# del()
# The del keyword will delete the set completely
print("\n")
myset = {"vidhi", "deep", "ekta"}
del myset
print(myset) #this will raise an error because the set no longer exists
"""

# Join Sets
# The union() and update() methods joins all items from both sets.
print("\n")
set1 = {"vidhi", "ekta", "deep"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
#OR
set3 = set1 | set2  #Use "|" to join two sets
print(set3)

# Join Multiple Sets
print("\n")
set1 = {"apple", "kiwi"}
set2 = {10, 20}
set3 = {True, False}

set4 = set1 | set2 | set3
print(set4)


# Join a Set, a Tuple and a List
print("\n")
myset = {"a", "b", "c"}
mylist = [11, 12, 13]
mytuple = (True, False)
x = myset.union(mylist, mytuple)
#x = myset | mytuple | mylist  #The | operator only allows you to join sets with sets
print(x)


# Intersection () method
# Join set1 and set2, but keep only the duplicates
print("\n")
set1 = {"vidhi", "ekta", "kushi"}
set2 = {"deep", "vidhi", "sonu"}

x = set1.intersection(set2)
#OR
x = set1 & set2  #also you can use "&" operator
print(x)


# Difference
# Keep all items from set1 that are not in set2
print("\n")
set1 = {"orange", "banana", "kiwi"}
set2 = {"kiwi", "mango", "chiku"}

x = set1.difference(set2)
#OR
x = set1 - set2  #also you can use "-" operator
print(x)


# Symmetric Differences
# Keep the items that are not present in both sets
print("\n")
set1 = {"vidhi", "deep", "ekta"}
set2 = {"vidhi", "savan", 1}

x = set1.symmetric_difference(set2)
#OR
x = set1 ^ set2  #also you can use "^" operator
print(x)


# copy()
# Returns a copy of the set
print("\n")
myset = {"apple", "orange", "mango"}
x = myset.copy()
print(x)


# isdisjoint()
# Returns whether two sets have intersection or not
print("\n")
set1 = {"vidhi", "ekta", "deep"}
set2 = {"savan", "kushi", "sonu"}

x = set1.isdisjoint(set2)
print("isdisjoint", x)

# issubset()
# Return True if all items in set x are present in set y
print("\n")
set1 = {10, 12, 24}
set2 = {10, 12, 24, 20, 36}
x = set1.issubset(set2)
#OR
x = set1 <= set2  #also you can use <= operator
print("issubset", x)

# issuperset()
# Return True if all items set y are present in set x
print("\n")
set1 = {10, 12, 24, 20, 36,}
set2 = {10, 12, 24}
x = set1.issuperset(set2)
print("issuperset", x)
