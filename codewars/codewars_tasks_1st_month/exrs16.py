"""
Hexadecimal Keys


---The Deaf Rats of Hamelin---
Story
The Pied Piper has been enlisted to play his magical tune and coax all the rats out of town.
But some of the rats are deaf and are going the wrong way!
Kata Task
How many deaf rats are there?
"""


def find_key(encryption_key):
    num = int(encryption_key, 16)
    for i in range(2, int(num ** .5) + 1):
        if not num % i:
            return (i - 1) * (num // i - 1)


sample1 = find_key("2533")
sample2 = find_key("1ba9")
print(sample1 == 9328)
print(sample2 == 6912)


def count_deaf_rats(town):
    return town.replace(" ", "")[::2].count("O")


print(count_deaf_rats("~O~O~O~O P") == 0)
print(count_deaf_rats("P O~ O~ ~O O~") == 1)
print(count_deaf_rats("~O~O~O~OP~O~OO~") == 2)