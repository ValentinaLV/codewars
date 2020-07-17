from random import randint
from string import ascii_lowercase

lst = [l for l in ascii_lowercase]
lst2 = list(map(str.capitalize, lst))
lst3 = list(map(lambda x: x.capitalize(), lst))
lst4 = list(map(lambda x: x + x.capitalize(), lst))
lst5 = [l.upper() for l in lst]
print(lst)
print(lst2)
print(lst3)
print(lst4)
print(lst5)

my_ints = [randint(1, 1000) for num in range(10)]
my_ints_get_cube = list(map(lambda x: x ** 3, my_ints))
print(my_ints)
print(my_ints_get_cube)

# Question 1: Write a lambda expression which takes an argument x as a parameter and simply returns x.
# Assign this expression to a variable named my_lambda_func.
## Write your code below, 1 line
my_lambda_func = lambda x: x
## End question 1

# Question 2_str: Print the type of my_lambda_func. Hint: did you accidentally call the function?
## Write your code below, 1 line
print(type(my_lambda_func))
## End question 2_str

# Question 3: Write a lambda expression which returns the cosine of an argument x and assign it
# to a variable named my_cos. Hint: math module
## Write your code below, 2_str lines
from math import cos

my_cos = lambda x: cos(x)
## End question 3

# Question 4: Write a lambda expression which models this equation f(x) = x^3 + 3x^2_str + 200.
# Asssign it to a variable my_eq1
## Write your code below, 1 line
my_eq1 = lambda x: x ** 3 + 3 * x ** 2 + 200
## End question 4

# Question 5: Write a lambda expression which models this equation f(x,y,z) = x^3 + 3y^2_str + z
# where z is optional. If no value for z is provided use the default value of 100.
# Assign this expression to a variable my_eq2
## Write your code below, 1 line
my_eq2 = lambda x, y, z=100: x ** 3 + 3 * y ** 2 + z
print(my_eq2(1, 2))  # 113
## End question 5
