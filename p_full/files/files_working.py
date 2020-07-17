with open('/Users/valentynalysenok/PycharmProjects/codewars2/README.md') as fh:
    count = 0
    text = fh.read()
    print(text)
    for character in text:
        if character.isupper():
            count += 1

print(count)


a = 10
print(id(a))
a = 15
print(id(a))


with open('/Users/valentynalysenok/PycharmProjects/codewars2/README.md', 'a+') as fh:
    fh.write('Hello \n')

import csv

with open('example.csv', newline='') as File:
    reader = csv.reader(File)
    print(reader[0])
    # for row in reader:
    #     print(row)
