from collections import Counter

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the', 'eyes', "don't", 'look', 'around', 'the',
    'eyes', 'look', 'into', 'my', 'eyes', "you're", 'under'
]
morewords = ['why','are','you','not','looking','in','my','eyes']

words_count = Counter(words)
print(words_count)
words_count.update(morewords)
print(words_count)
words_top_3 = words_count.most_common(3)
print(words_top_3)
