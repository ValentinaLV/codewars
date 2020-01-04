"""
https://www.geeksforgeeks.org/python-format-function/
s – strings
d – decimal integers (base-10)
f – floating point display
c – character
b – binary
o – octal
x – hexadecimal with lowercase letters after 9
X – hexadecimal with uppercase letters after 9
e – exponent notation
"""

my_string = "{}, is a {} science portal for {}"
print(my_string.format("GeeksforGeeks", "computer", "geeks"))

print("This is {} {} {} {}"
      .format("one", "two", "three", "four"))

print("This is {3} {2} {1} {0}"
      .format("one", "two", "three", "four"))

print("{gfg} is a {0} science portal for {1}"
      .format("computer", "geeks", gfg="GeeksforGeeks"))

# ------Type Specifying------
# Syntax :
# String {field_name:conversion} Example.format(value)
print("The temperature today is {0:f} degrees outside !"
      .format(35.567))  # 35.567000

print("The temperature today is {0:.2f} degrees outside !"
      .format(35.567))  # 35.57

print("My average of this {0} was {1:.0f}%"
      .format("semester", 78.234876))  # 78%

print("The {0} of 100 is {1:b}"
      .format("binary", 100))

print("The {0} of 100 is {1:o}"
      .format("octal", 100))

# -----Padding Substitutions or Generating Spaces-----
print("{0:4}, is the computer science portal for {1:8}!"
      .format("GeeksforGeeks", "geeks"))

print("It is {0:5} degrees outside !"
      .format(40))


# -----Organize data-----
def unorganized(a, b):
    for i in range(a, b):
        print(i, i ** 2, i ** 3, i ** 4)


def organized(a, b):
    for i in range(a, b):
        # Using formatters to give 6
        # spaces to each set of values
        print("{:6d} {:6d} {:6d} {:6d}"
              .format(i, i ** 2, i ** 3, i ** 4))


n1 = int(input("Enter lower range :-\n"))
n2 = int(input("Enter upper range :-\n"))

print("------Before Using Formatters-------")

# Calling function without formatters
unorganized(n1, n2)

print()
print("-------After Using Formatters---------")
print()

# Calling function that contain
# formatters to organize the data
organized(n1, n2)