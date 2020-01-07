"""
https://www.w3schools.com/python/python_strings.asp

+ capitalize()	Converts the first character to upper case
+ casefold()	Converts string into lower case
+ center()	Returns a centered string
+ count()	Returns the number of times a specified value occurs in a string
- encode()	Returns an encoded version of the string
+ endswith()	Returns true if the string ends with the specified value
+ expandtabs()	Sets the tab size of the string
+ find()	Searches the string for a specified value and returns the position of where it was found
+ format()	Formats specified values in a string
- format_map()	Formats specified values in a string
+ index()	Searches the string for a specified value and returns the position of where it was found
+ isalnum()	Returns True if all characters in the string are alphanumeric
+ isalpha()	Returns True if all characters in the string are in the alphabet
+ isdecimal()	Returns True if all characters in the string are decimals
+ isdigit()	Returns True if all characters in the string are digits
+ isidentifier()	Returns True if the string is an identifier
+ islower()	Returns True if all characters in the string are lower case
+ isnumeric()	Returns True if all characters in the string are numeric
- isprintable()	Returns True if all characters in the string are printable
+ isspace()	Returns True if all characters in the string are whitespaces
+ istitle()	Returns True if the string follows the rules of a title
+ isupper()	Returns True if all characters in the string are upper case
+ join()	Joins the elements of an iterable to the end of the string
- ljust()	Returns a left justified version of the string
+ lower()	Converts a string into lower case
+ lstrip()	Returns a left trim version of the string
- maketrans()	Returns a translation table to be used in translations
+ partition()	Returns a tuple where the string is parted into three parts
+ replace()	Returns a string where a specified value is replaced with a specified value
- 	Searches the string for a specified value and returns the last position of where it was found
- rindex()	Searches the string for a specified value and returns the last position of where it was found
- rjust()	Returns a right justified version of the string
+ rpartition()	Returns a tuple where the string is parted into three parts
+ rsplit()	Splits the string at the specified separator, and returns a list
+ rstrip()	Returns a right trim version of the string
+ split()	Splits the string at the specified separator, and returns a list
+ splitlines()	Splits the string at line breaks and returns a list
+ startswith()	Returns true if the string starts with the specified value
+ strip()	Returns a trimmed version of the string
+ swapcase()	Swaps cases, lower case becomes upper case and vice versa
+ title()	Converts the first character of each word to upper case
- translate()	Returns a translated string
+ upper()	Converts a string into upper case
+ zfill()	Fills the string with a specified number of 0 values at the beginning
"""

# Strings are Arrays
a = "Hello, World!"
print(a[1])
print(a[2:5])
print(a[-5:-2])

print(len(a))

# String Methods
# strip() -> removes any whitespace from the beginning or the end
b = " Hello, World! "
print(b.strip())

# lstrip()
print(" Hello, World! ".lstrip())  # "Hello, World! "
# rstrip()
print(" Hello, World! ".rstrip())  # " Hello, World!"

# lower()
c = "Hello, World!".lower()
print(c)
print(c.islower())

# casefold()
txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)  # hello, and welcome to my world!

# upper()
d = "Hello, World!".upper()
print(d)
print(d.isupper())

# title()
s = "hello, world!".title()
print(s)  # Hello, World!
print(s.istitle())

# capitalize()
s = "hello, world!".capitalize()
print(s)  # Hello, world!

# replace()
e = a.replace("e", "o")
print(e)


def replace_(s, old, new):
    return new.join(s.split(old))


print(replace_("Hollo, World!", "o", "e"))

# split()
print(a.split(", "))

# rsplit()
print("Hello, World, Hi!".rsplit(", "))  # ['Hello', 'World', 'Hi!']

# Check String
txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
print(x)
y = "ain" not in txt
print(y)

# String Concatenation
a = "Hello"
b = "World"
c = a + " " + b
print(c)

# swapcase()
print("eRtttYYY".swapcase())  # ErTTTyyy

# zfill()
a = "hello"
b = "welcome to the jungle"
c = "10.000"

print(a.zfill(10))
print(b.zfill(10))
print(c.zfill(10))

# startswith()
print("Valentyna".startswith("Valen"))

# endswith()
print("Valentyna".endswith("tyna"))

# find()
txt = "Hello, welcome to my world."
x = txt.find("e")
print(x)  # 1

y = txt.find("e", 5, 10)
print(y)  # 8

# count()
print("Hello".count("l"))  # 2

# index()
print("Hello".index("o"))  # 4

# isalnum()
txt = "Company12"
x = txt.isalnum()
print(x)

# isalpha()
txt = "CompanyX"
x = txt.isalpha()
print(x)

# isdecimal()
txt = "\u0033" #unicode for 3
x = txt.isdecimal()
print(x)  # T

s = "12345"
print(s.isdecimal())  # T
# contains alphabets
s = "12geeks34"
print(s.isdecimal())  # F
# contains numbers and spaces
s = "12 34"
print(s.isdecimal())  # F

# isdigit()
txt = "50800"
x = txt.isdigit()
print(x)  # T

# isidentifier()
str = 'Python'
print(str.isidentifier())  # T
str = 'Py thon'
print(str.isidentifier())  # F
str = '22Python'
print(str.isidentifier())  # F
str = ''
print(str.isidentifier())  # F

# isnumeric()
str = u"this2009"
print(str.isnumeric())  # F

str = u"23443434"
print(str.isnumeric())  # T

# isspace()
txt = "   s   "
x = txt.isspace()
print(x)  # F
txt2 = "      "
y = txt2.isspace()
print(y)  # T

# join()
myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)  # John#Peter#Vicky

# ljust()
txt = "banana"
x = txt.ljust(5)
print(x, "is my favorite fruit.")  # ???

# center()
txt = "banana"
x = txt.center(20)
print(x)  # "       banana       "
print(len(x))  # 20

# expandtabs()
txt = "H\te\tl\tl\to"
x = txt.expandtabs(2)
print(x)  # H e l l o

# partition()
# rpartition()
txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x)  # ('I could eat ', 'bananas', ' all day')

# splitlines()
txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines()  # ['Thank you for the music', 'Welcome to the jungle']
print(x)
