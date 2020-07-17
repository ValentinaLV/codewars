"""
https://www.datacamp.com/community/tutorials/python-dictionary-comprehension?utm_source=adwords_ppc&utm_campaignid=1455363063&utm_adgroupid=65083631748&utm_device=c&utm_keyword=&utm_matchtype=b&utm_network=g&utm_adpostion=1t1&utm_creative=332602034358&utm_targetid=aud-748597547652:dsa-473406574715&utm_loc_interest_ms=&utm_loc_physical_ms=1012851&gclid=CjwKCAiA6bvwBRBbEiwAUER6JUcAn2La9BZ2Sr41Rmkfe61k1t54zuc8ur_R5_cm9mQcI_WCTqRr_RoCw9MQAvD_BwE
Alternative to lambda functions
"""

# 1
fahrenheit = {'t1': -30, 't2': -20, 't3': -10, 't4': 0}
# Get the corresponding `celsius` values
celsius = list(map(lambda t: round(((float(5) / 9) * (t - 32)), 2), fahrenheit.values()))
# Create the `celsius` dictionary
celsius_dict = dict(zip(fahrenheit.keys(), celsius))
print(celsius_dict)

# 2_str
# the same using by dict comprehension
# dictionary comprehension as compared to the two step process and understanding
# the working of three functions (lambda, map() and zip()) for the first implementation.
fahrenheit2 = {'t1': -30, 't2': -20, 't3': -10, 't4': 0}
celsius2 = {k: round(((float(5) / 9) * (v - 32)), 2) for (k, v) in fahrenheit2.items()}
print(celsius2)

