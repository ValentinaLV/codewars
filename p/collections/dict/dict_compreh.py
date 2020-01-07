"""
https://www.datacamp.com/community/tutorials/python-dictionary-comprehension?utm_source=adwords_ppc&utm_campaignid=1455363063&utm_adgroupid=65083631748&utm_device=c&utm_keyword=&utm_matchtype=b&utm_network=g&utm_adpostion=1t1&utm_creative=332602034358&utm_targetid=aud-748597547652:dsa-473406574715&utm_loc_interest_ms=&utm_loc_physical_ms=1012851&gclid=CjwKCAiA6bvwBRBbEiwAUER6JUcAn2La9BZ2Sr41Rmkfe61k1t54zuc8ur_R5_cm9mQcI_WCTqRr_RoCw9MQAvD_BwE
"""

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(dict1.keys())
print(dict1.values())
print(dict1.items())  # dict_items([('a', 1), ('b', 2), ('c', 3), ('d', 4)])

# dict_variable = {key:value for (key,value) in dictonary.items()}
dict1_1 = {k*2: v for (k, v) in dict1.items()}
print(dict1_1)
dict1_2 = {k: v**2 for (k, v) in dict1.items()}
print(dict1_2)

numbers = range(10)
dict2 = {n: n**2 for n in numbers if n % 2}
print(dict2)
dict3 = {n: n**2 for n in numbers if n % 2 == 0}
print(dict3)