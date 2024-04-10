
# Python Dictionaries
# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# Dictionaries are written with curly brackets

print("\n")
mydict = {"name": "vidhi",
          "age": 26,
          "year": 1998}
print(mydict)


# Dictionary Items
# Dictionary items are ordered, changeable, and do not allow duplicates
print("\n")
mydict = {"fruits": "apple",
          "color": "red",
          "kg": 1}
print(mydict["fruits"])


# Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.

# Duplicates Not Allowed
# Dictionaries cannot have two items with the same key
print("\n")
mydict = {"name": "vidhi",
          "surname": "patel",
          "year": 1998,
          "year": 1999}
print(mydict)


# Dictionary Length
# To determine how many items a dictionary has, use the len() function
print("\n")
mydict = {"fruits": "mango",
         "fruits2": "kiwi",
        "fruits3": "orange"}
print(len(mydict))

# Dictionary Items - Data Types
# The values in dictionary items can be of any data type
print("\n")
mydict = {
         "brand": "ford",
         "electric": False,
         "year": 1964,
         "colors": ["white", "black", "blue"]
         }
print(mydict)


# type()
print("\n")
mydict = {"name": "vidhi",
          "age": 26,
          "year": 1998}
print(type(mydict))


# The dict() Constructor
# It is also possible to use the dict() constructor to make a dictionary
print("\n")
mydict = dict(name = "ekta", age = 23, year = 2001)
print(mydict)


# Accessing Items
# You can access the items of a dictionary by referring to its key name, inside square brackets
print("\n")
mydict = {"brand": "ford",
          "color": "white",
          "year": 1964}
print(mydict["color"])
# OR
x = mydict.get("color")  # using get() method that will give you the same result
print(x)

# Get Keys
# The keys() method will return a list of all the keys in the dictionary.
print("\n")
mydict = {"name": "vidhi",
          "age": 26,
          "year": 1998}
x = mydict.keys()
print(x)

# add keys
# Add a new item to the original dictionary, and see that the keys list gets updated as well
print("\n")
mydict = {"brand": "ford",
          "model": "mustang",
          "year": 1964}

x = mydict.keys()
print(x)

mydict["color"] = "white"  #add kyes
print(x)

# Get Values
# The values() method will return a list of all the values in the dictionary.
print("\n")
mydict = {"fruits": "apple",
          "price": 50,
          "kg": 1}
x = mydict.values()
print(x)

mydict["kg"] = 2  #Change value
print(x)

mydict["color"] = "red"  #add value
print(x)


# Get Items
# The items() method will return each item in a dictionary, as tuples in a list.
print("\n")
mydict = {"name": "vidhi",
          "surname": "patel",
          "age": 26}
x = mydict.items()
print(x)

mydict["age"] = 25  #change item
print(x)

mydict["year"] = 1998 #add item
print(x)


# Check if Key Exists
# To determine if a specified key is present in a dictionary use the in keyword
print("\n")
mydict = {"brand": "ford",
          "model": "mustang",
          "year": 1964}
if "model" in mydict:
    print("yes, 'model' is one of the keys in the mydict dictionary")


# Change Values
# You can change the value of a specific item by referring to its key name
print("\n")
mydict = {"name": "vidhi",
          "age": 26,
          "year": 1998}
mydict["age"] = 25
print(mydict)


# Update Dictionary
# The update() method will update the dictionary with the items from the given argument
print("\n")
mydict = {"brand": "ford",
          "model": "mustang",
          "year": 1964}
mydict.update({"year": 1980})  #update value
print(mydict)


# Adding Items
# Adding an item to the dictionary is done by using a new index key and assigning a value to it
print("\n")
mydict = {"brand": "Ford",
          "model": "mustang",
          "year": 1964,
          }
mydict["color"] = "blue"
print(mydict)


# Update Dictionary
# The update() method will update the dictionary with the items from a given argument. If the item does not exist, the item will be added.
print("\n")
mydict = {"name": "vidhi",
          "surname": "patel",
          "age": 26
          }
mydict.update({"year": 1998})
print(mydict)


# Removing Items
# The pop() method removes the item with the specified key name
print("\n")
mydict = {"fruits": "apple",
          "price": 50,
          "kg": 1,
          "color": "red"
          }
mydict.pop("color")   #pop method to remove
print(mydict)


# popitem()
print("\n")
mydict = {"fruits": "banana",
          "price": 30,
          "kg": 1
          }
mydict.popitem()  #popitem method remove last inserted
print(mydict)


# del
# The del keyword removes the item with the specified key name
print("\n")
mydict = {"brand": "ford",
           "model": "mustang",
           "year": 1996
           }
del mydict["model"]
print(mydict)


# clear()
# The clear() method empties the dictionary
print("\n")
mydict = {"brand": "ford",
          "model": "mustang",
          "year": 1996
          }
mydict.clear()
print(mydict)


# Copy a Dictionary
# Make a copy of a dictionary with the copy() method
print("\n")
dict1 = {"name": "vidhi",
         "age": 26,
         "year": 1998
         }
dict2 = dict1.copy()
print(dict2)


# Another way to make a copy is to use the built-in function dict()
print("\n")
mydict = {"brand": "ford",
          "model": "mustang",
          "year": 1964
          }
x = dict(mydict)
print(x)


# Nested Dictionaries
# A dictionary can contain dictionaries, this is called nested dictionaries
print("\n")
family = {"child1":
            {
            "name": "vidhi",
            "year": 1998
            },
          "child2":
            {
             "name": "deep",
              "year": 1996
            },
            "child3":
            {
             "name": "ekta",
             "year":  2001
            }
          }
print(family)

#OR
# Create three dictionaries, then create one dictionary that will contain the other three dictionaries
print("\n")
child1 = {
        "name": "vidhi",
        "year": 1998
        }
child2 = {
          "name": "deep",
          "year": 1996
          }
child3 = {
           "name": "ekta",
           "year": 2001
          }

family = {"child1": child1,
          "child2": child2,
          "child3": child3
          }
print(family)


# Access Items in Nested Dictionaries
# To access items from a nested dictionary, you use the name of the dictionaries, starting with the outer dictionary
print("\n")
family = {
         "child1": {
             "name": "vidhi",
             "year": 1998
         },
        "child2": {
            "name": "ekta",
            "year": 2001
        },
        "child3": {
            "name": "deep",
            "year": 1996
        }}
print(family["child2"]["name"])


# Loop Through Nested Dictionaries
# You can loop through a dictionary by using the items() method like this
print("\n")
myfamily = {
            "child1": {
                "name": "vidhi",
                "year": 1998
            },
            "child2": {
                "name": "deep",
                "year": 1996
            },
            "child3": {
                "name": "ekta",
                "year": 2001
            }}

for x, obj in myfamily.items():
    print(x)

    for y in obj:
       print(y + ":", obj[y])


# fromkeys()
# Returns a dictionary with the specified keys and value
print("\n")
x = ('key1', 'key2', 'key3')
y = 10
mydict = dict.fromkeys(x, y)
print(mydict)


# get() Method
# The get() method returns the value of the item with the specified key
print("\n")
mydict = {"name": "vidhi",
          "age": 26,
          "year": 1998}
x = mydict.get("age")
y = mydict.get("year")
print(x, ",", y)


# setdefault()
# Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
print("\n")
mydict = {"brand": "ford",
          "model": "mustang",
          "year": 1964}
x = mydict.setdefault("model", "bronco")
#OR
x = mydict.setdefault("color", "black")
print(x)