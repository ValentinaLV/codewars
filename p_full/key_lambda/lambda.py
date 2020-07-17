"""
https://www.educative.io/edpresso/what-is-a-python-lambda-function?https://www.educative.io/courses/grokking-the-object-oriented-design-interview?aid=5082902844932096&utm_source=google&utm_medium=cpc&utm_campaign=blog-dynamic&gclid=Cj0KCQiA0NfvBRCVARIsAO4930l_iGlbDKbXZrYWuZ_WOZZFi2p-W3AsnYNFX3loe13PHCLApNomNdAaArEwEALw_wcB
"""

square = lambda n: n * n
num = square(5)
print(num)

sub = lambda a, b: a - b
print(sub(12132, 3434))

my_list = [10, 25, 17, 9, 30, -5]
double_list = list(map(lambda n: n * 2, my_list))
print(double_list)

# Filters the elements which are multiples of 5
mult_five = list(filter(lambda n: n % 5 == 0, my_list))
print(mult_five)

# if else
max_val = lambda x, y: x if x > y else y
print(max_val(10, 12))

min_val = lambda x, y: x if x < y else y
print(min_val(-99, 99))
