import re

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
text1 = '11/27/2012'
text2 = 'Nov 27, 2012'
datepat = re.compile(r'\d+/\d+/\d+')

result1 = True if re.match(datepat, text1) else False
result2 = True if re.match(datepat, text2) else False
print(result1)
print(result2)

result = re.findall(datepat, text)
print(result)  # ['11/27/2012', '3/13/2013']

datepat2 = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datepat2.match('11/27/2012')
print(m.group(0))  # 11/27/2012
print(m.group(1))  # 11
print(m.group(2))  # 27
print(m.groups())
month, day, year = m.groups()

for m, d, y in datepat2.findall(text):
    print('{}-{}-{}'.format(year, month, day))

