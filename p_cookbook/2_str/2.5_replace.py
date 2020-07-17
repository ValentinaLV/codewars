import re

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
text_format_date = datepat.sub(r'\3-\1-\2', text)
print(text_format_date)
