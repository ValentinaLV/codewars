# Maximum subarray sum
# https://www.codewars.com/kata/maximum-subarray-sum/train/python


def maxSequence(arr):
    max_ending = max_current = arr[0]
    for i in arr[1:]:
        max_ending = max(i, max_ending + i)
        max_current = max(max_current, max_ending)
    return max_current


print(maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6)
