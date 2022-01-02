from collections import Counter


def solution(array):
    array = Counter(array)
    for i in array.keys():
        if array[i] % 2 != 0:
            return i
