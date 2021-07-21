"""
Project name: SortingProblem
File name: CountingSort.py
Description: 
version: 
Author: Jutraman
Email: jutraman@hotmail.com
Date: 12/07/2021 19:10
LastEditors: Jutraman
LastEditTime: 12/07/2021
Github: https://github.com/Jutraman
"""


def countingSort(array, maxValue):
    bucket = [None] * (maxValue + 1)
    sortedIndex = 0
    length = len(array)
    buketLength = length + 1

    for i in range(length):
        if bucket[array[i]] is None:
            bucket[array[i]] = 0
        bucket[array[i]] += 1

    for i in range(buketLength):
        while bucket[i] > 0:
            sortedIndex += 1
            array[sortedIndex] = i
            bucket[i] -= 1

    return array
