"""
Nested Dictionary Comprehension
https://www.datacamp.com/community/tutorials/python-dictionary-comprehension?utm_source=adwords_ppc&utm_campaignid=1455363063&utm_adgroupid=65083631748&utm_device=c&utm_keyword=&utm_matchtype=b&utm_network=g&utm_adpostion=1t1&utm_creative=332602034358&utm_targetid=aud-748597547652:dsa-473406574715&utm_loc_interest_ms=&utm_loc_physical_ms=1012851&gclid=CjwKCAiA6bvwBRBbEiwAUER6JUcAn2La9BZ2Sr41Rmkfe61k1t54zuc8ur_R5_cm9mQcI_WCTqRr_RoCw9MQAvD_BwE
"""

nested_dict = {'first': {'a': 1}, 'second': {'b': 2}}
float_dict = {outer_k:
                  {inner_k: float(inner_v) for (inner_k, inner_v) in outer_v.items()}
              for (outer_k, outer_v) in nested_dict.items()
              }
float_dict2 = {outer_k:
                  {float(inner_v) for (inner_k, inner_v) in outer_v.items()}
              for (outer_k, outer_v) in nested_dict.items()
              }
print(float_dict2)
print(float_dict)

nested_dict2 = {'first': {'a': 1}, 'second': {'b': 2}}
for (outer_k, outer_v) in nested_dict2.items():
    for (inner_k, inner_v) in outer_v.items():
        outer_v.update({inner_k: float(inner_v)})

nested_dict2.update({outer_k: outer_v})

print(nested_dict2)
