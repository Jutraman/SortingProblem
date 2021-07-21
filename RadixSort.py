"""
Project name: SortingProblem
File name: RadixSort.py
Description: 
version: 
Author: Jutraman
Email: jutraman@hotmail.com
Date: 13/07/2021 00:11
LastEditors: Jutraman
LastEditTime: 13/07/2021
Github: https://github.com/Jutraman
"""


def radixSort(array, maxDigit):
    mod = 10
    dev = 1
    for i in range(maxDigit):
        for j in range(len(array)):
            bucket = parseInt((array[j] % mod) / dev)
            if counter[bucket] == None:
                counter[bucket] = []
            counter[bucket].push(array[i])
        dev *= 10
        mod *= 10
        pos = 0
        for k in range(len(counter)):
            if counter[k] != None:
                while counter[].shift() != None:
                    pos += 1
                    array[pos] = None
    return array
