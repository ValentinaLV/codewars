"""
https://www.codewars.com/kata/54147087d5c2ebe4f1000805

https://www.codewars.com/kata/5921c0bc6b8f072e840000c0
"""


def _if(bool, func1, func2):
    """
    def truthy(): print("True")
    def falsey(): print("False")
    _if(True, truthy, falsey)
    # prints 'True' to the console
    :param bool:
    :param func1:
    :param func2:
    :return:
    """
    return func1() if bool else func2()


def sequence_classifier(arr):
    if all(arr[i] == arr[i + 1] for i in range(len(arr) - 1)):
        return 5
    elif all(arr[i] < arr[i + 1] for i in range(len(arr) - 1)):
        return 1
    elif all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1)):
        return 2
    elif all(arr[i] > arr[i + 1] for i in range(len(arr) - 1)):
        return 3
    elif all(arr[i] >= arr[i + 1] for i in range(len(arr) - 1)):
        return 4
    else:
        return 0
