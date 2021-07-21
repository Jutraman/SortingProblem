"""
Project name: SortingProblem
File name: InsertionSort.py
Description: 
version: 
Author: Jutraman
Email: jutraman@hotmail.com
Date: 04/07/2021 23:27
LastEditors: Jutraman
LastEditTime: 04/07/2021
Github: https://github.com/Jutraman
"""


def insertionSort(array):
    length = array
    for i in range(length):
        pre_index = i - 1
        current = array[i]
        while pre_index >= 0 & array[pre_index] > current:
            array[pre_index + 1] = array[pre_index]
            pre_index -= 1
        array[pre_index + 1] = current
    return array
