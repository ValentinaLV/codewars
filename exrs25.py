"""
https://www.codewars.com/kata/554e4a2f232cdd87d9000038

https://www.codewars.com/kata/54da539698b8a2ad76000228
"""


def DNA_strand(dna):
    pairs = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(pairs[d] for d in dna)


def is_valid_walk(walk):
    return len(walk) == 10 \
           and walk.count('n') == walk.count('s') \
           and walk.count('e') == walk.count('w')
