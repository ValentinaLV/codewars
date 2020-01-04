"""
https://www.w3schools.com/python/ref_string_format.asp
:<		Left aligns the result (within the available space)
:>		Right aligns the result (within the available space)
:^		Center aligns the result (within the available space)
:=		Places the sign to the left most position
:+		Use a plus sign to indicate if the result is positive or negative
:-		Use a minus sign for negative values only
: 		Use a space to insert an extra space before positive numbers (and a minus sign befor negative numbers)
:,		Use a comma as a thousand separator
:_		Use a underscore as a thousand separator
"""

txt1 = "for only {price:.2f} dollars".format(price=49.9)
txt2 = "for only {:.2f} dollars".format(49.9)
txt3 = "for only {0:.2f} dollars".format(49.9)
print(txt1)
print(txt2)
print(txt3)

txt4 = "My name is {fname}, I'am {age}".format(fname="John", age=36)
txt5 = "My name is {0}, I'am {1}".format("John", 36)
txt6 = "My name is {}, I'am {}".format("John", 36)
print(txt4)
print(txt5)
print(txt6)
