#print hello world
import add_twonumber

print("Hello World!")


#print hello using variables
print("\n")
a = 'Hello'
print(a)


#Global Variables (Variables that are created outside of a function  are known as global variables.)
#Global variables can be used by everyone, both inside of functions and outside.
print("\n")
x = "Vidhi"

def func():
    x = "Deep"
    print("my name is = " + x)

func()
print("my name is = " + x)


#global Keyword (If you use the global keyword, the variable belongs to the global scope)
print("\n")
def func():
    global x
    x = "Ekta"

func()
print("my name is = " + x)


#multiline comment
print("\n")
"""hello my name is vidhi. 
i am come from mehsana
i am computer engineer"""

print("\n")
#data types
a = int(10)
y = str(100)
z = float(1000)

print(a)
print(y)
print(z)

#define types
print("\n")
x = 10
y = 'vidhi'
print(type(x))
print(type(y))


#Variable Names Define
print("\n")
myvar = '14vidhi'
MyVar = 'vidhi'
_my_var = 'vidhi'
MYVAR = 'vidhi'
myVar = 'vidhi'
myvar1 = 'vidhi'

print(myvar)
print(MyVar)
print(_my_var)
print(MYVAR)
print(myVar)
print(myvar1)

#Many Values to Multiple Variables
print("\n")
x, y, z = "Orange", "Banana", "mango"
print(x)
print(y)
print(z)

#One Value to Multiple Variables
print("\n")
x = y = z = "orange"
print(x)
print(y)
print(z)

#Unpack a Collection
print("\n")
fruits = ['orange', 'banana', 'mango']
x, y, z = fruits
print(x)
print(y)
print(z)

#Addition 2 number
print("\n")
x = 10
y = 20
print(x+y)

#Slicing string
print("\n")
x = "Ekta vidhi Deep"
print(x[3:11])

#Slice From the Start
print("\n")
x = "Ekta vidhi Deep"
print(x[:11])

#Definne string Lenght
print("\n")
x = 'Ekta vidhi deep'
print(len(x))

#slicing string from the start with skip character
print("\n")
x = 'Ekta vidhi deep'
print(x[:13:2])

#Slice From the Start to end with skip character
print("\n")
x = 'Ekta vidhi deep'
print(x[::2])

#slice with skip character
print("\n")
x = 'Ekta vidhi deep'
print(x[2:13:2])


#Negative Indexing
print("\n")
x = 'vidhi deep'
print(x[-6:-2])


#sclice negative indexing with skip character
print("\n")
x = 'vidhideep'
print(x[-6:-2:2])


#convert upper case
print("\n")
x = 'vidhi'
print(x.upper())


#convert lower case
print("\n")
x = 'VIDHI'
print(x.lower())


#Remove Whitespace
print("\n")
x = ' VIDHI patel '
print(x.strip())


#Replace String
print("\n")
x = 'VIDHI'
print(x.replace("V", "N"))


#Split String
print("\n")
x = 'VIDHI patel'
print(x.split())


#capitalize string (first character is convert into capital)
print("\n")
x = 'vidhi'
print(x.capitalize())


#casefold string (first character is convert in to small)
print("\n")
x = 'Vidhi Patel'
print(x.casefold())

#center string
print("\n")
txt = 'vidhi patel'
x = txt.center(20)
print(x)

#Count string
print("\n")
txt = 'vidhi patel vidhi'
x = txt.count('vidhi')
print(x)

#encode method string
print("\n")
txt = 'vidhi Ståle'
x = txt.encode()
print(x)

#endswith string (end with punctuation sign (.))
print("\n")
txt = 'vidhi patel.'
x = txt.endswith(".")
print(x)


#expandtabs (give the space between string)
print("\n")
txt = 'v\ti\td\th\ti'
x = txt.expandtabs(3)
print(x)


#find (finds the first occurrence of the specified value.)
print("\n")
txt = 'vidhi patel'
x = txt.find("patel")
print(x)


#formate (Use "f" to convert a number into a fixed point number, default with 6 decimals,
# but use a period followed by a number to specify the number of decimals:)

#txt = "The price is {:.2f} dollars."
#print(txt.format(45)) = 45.00

#without the ".2" inside the placeholder, this number will be displayed like this:

#txt = "The price is {:f} dollars."
#print(txt.format(45)) = 45.000000

print("\n")
txt = 'The Price {price:.2f} is fix'
print(txt.format(price=49))


#index  (finds the first occurrence of the specified value)
print("\n")
txt = 'vidhi patel'
x = txt.index("t")
print(x)

#isalnum (Returns True if all characters in the string are alphanumeric)
print("\n")
txt = 'vidhipatel145'
x = txt.isalnum()
print(x)


#isalpha (Returns True if all characters in the string are in the alphabet)
print("\n")
txt = 'vidhipatel'
x = txt.isalpha()
print(x)

#isascii (Returns True if all characters in the string are ascii characters)
print("\n")
txt = 'v2udkjwsl'
x = txt.isascii()
print(x)


#isdecimal	(Returns True if all characters in the string are decimals)
print("\n")
txt = '123'
x = txt.isdecimal()
print(x)

#isdigit (Returns True if all characters in the string are digits)
print("\n")
txt = '1498'
x = txt.isdigit()
print(x)


#isidentifier (Returns True if the string is an variable identifier like its camel case , pascle case, snake case its true)
print("\n")
txt = 'vidhiPatel_14'
x = txt.isidentifier()
print(x)

#islower (Returns True if all characters in the string are lower case)
print("\n")
txt = 'vidhi'
x = txt.islower()
print(x)


#isnumeric (Returns True if all characters in the string are numeric)
print("\n")
txt = '2510'
x = txt.isnumeric()
print(x)

#isprintable (Returns True if all characters in the string are printable)
print("\n")
txt = 'vidhi\n!@patel'
x = txt.isprintable()
print(x)

#isspace (Returns True if all characters in the string are whitespaces)
print("\n")
txt = '  '
x = txt.isspace()
print(x)

#istitle (Returns True if the string follows the rules of a title)
print("\n")
txt = 'Vidhi Patel'
x = txt.istitle()
print(x)


#isupper (Returns True if all characters in the string are upper case)
print("\n")
txt = 'VIDHI PATEL'
x = txt.isupper()
print(x)


#join (Converts the elements of an iterable into a string)
print("\n")
txt = ["vidhi", "patel"]
x = '#'.join(txt)
print(x)


#ljust (Returns a left justified version of the string, ljust consider as a white space)
print("\n")
txt = 'vidhi patel'
x = txt.ljust(15)
print(x, 'this is my name')


#lower (Converts a string into lower case)
print("\n")
txt = 'VIDHI PATEL'
x = txt.lower()
print(x)


#lstrip (Returns a left trim version of the string , its remove left space in string)
print("\n")
txt = '   vidhi patel     '
x = txt.lstrip()
print('this is', x, 'my name')

#maketrans (Returns a translation table to be used in translations , its replace element)
print("\n")
txt = 'vidhi patel'
x = str.maketrans('v','n')
print(txt.translate(x))


#partition (Returns a tuple where the string is parted into three parts)
print("\n")
txt = 'vidhi 12 deep 12 Ekta'
x = txt.partition('deep')
print(x)


#replace (Returns a string where a specified value is replaced with a specified value)
print("\n")
txt = 'vidhi patel'
x = txt.replace("vidhi", "nidhi")
print(x)


#rfind (Searches the string for a specified value and returns the last position of where it was found)
print("\n")
txt = 'vidhi patel, vidhi patel'
x = txt.rfind("patel")
print(x)

#rindex (Searches the string for a specified value and returns the last position of where it was found)
print("\n")
txt = 'vidhi patel, vidhi patel'
x = txt.rindex("vidhi")
print(x)

#rjust (Returns a right justified version of the string)
print("\n")
txt = "vidhi patel"
x = (txt.rjust(20))
print(x, 'is my name')


#rpartition	(Returns a tuple where the string is parted into three parts)
print("\n")
txt = "vidhi 12 deep 12 Ekta vidhi"
x = (txt.rpartition("12"))
print(x)

#rsplit	(Splits the string at the specified separator, and returns a list)
print("\n")
txt = "vidhi , deep , Ekta"
x = txt.rsplit(", ")
print(x)

#rstrip	 (Returns a right trim version of the string)
print("\n")
txt = "  vidhi deep Ekta  "
x = txt.rstrip()
print('this is', x, 'my name')

#split	(Splits the string at the specified separator, and returns a list)
print("\n")
txt = "vidhi patel"
x = txt.split()
print(x)

#splitlines (Splits the string at line breaks and returns a list)
print("\n")
txt = "vidhi deep\n Ekta"
x = txt.splitlines()
print(x)

#startswith (Returns true if the string starts with the specified value)
print("\n")
txt = "vidhi patel"
x = txt.startswith('vidhi')
print(x)

#strip (Remove spaces at the beginning and at the end of the string)
print("\n")
txt = "   vidhi patel   "
x = txt.strip()
print('this is', x, 'name')

#swapcase (Make the lower case letters upper case and the upper case letters lower case)
print("\n")
txt = "Vidhi pATEL"
x = txt.swapcase()
print(x)

#title (Converts the first character of each word to upper case)
print("\n")
txt = "vidhi patel"
x = txt.title()
print(x)

#problem
print("\n")
mydict = {83: 80}
txt = 'vidhi sam'
print(txt.translate(mydict))

#upper (Converts a string into upper case)
print("\n")
txt = "vidhi patel"
x = txt.upper()
print(x)

#zfill (Fill the string with zeros until it is 10 characters long)
print("\n")
txt = '100'
x = txt.zfill(10)
print(x)


#Concatenation (concatenate, or combine, two strings you can use the + operator.)
print("\n")
a = "Hello"
b = "World"
c = a + b
print(c)

#Boolean Values (In programming you often need to know if an expression is True or False)
#Any string is True, except empty strings.
print("\n")
print(bool(10 > 9))
print(bool(10 == 9))
print(bool(10 < 9))
print(bool("")) #empty string



#String Format (The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {})
print("\n")
quantity = 5
price = 50
itemno = 200
order = "I want to pay {1} dollars for {0} pieces of itemno {2}"
print(order.format(quantity, price, itemno))



#print specific word
print('\n')
txt = "my name is vidhi"
x = txt.split(" ")
b = x[3:]
print(b)

#swap two values without using temporary variable
print('\n')
a = 5
b = 10
b = b - a
a = a + b
print('a = ', a, '\n' 'b = ', b)




# Python input() Function
# Ask for the user's name and print it
#print("\n")
#x = input("enter your name:")
#print('hello, ' + x)

# Add Input
print("\n")
#mylist = ["vidhi", "ekta", "deep"]
#y = input("enter the string: ")
#mylist.append(y)
#mylist.remove(y)
#mylist.sort()
#print(y[1:10:2].split())
#print(mylist)


# Addition
x = int(input("enter a number: "))
y = int(input("enter a second number: "))
z = x % y
print(z)

