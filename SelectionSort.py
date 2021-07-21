"""
Project name: SortingProblem
File name: SelectionSort.py
Description: 
version: 
Author: Jutraman
Email: jutraman@hotmail.com
Date: 04/07/2021 23:10
LastEditors: Jutraman
LastEditTime: 04/07/2021
Github: https://github.com/Jutraman
"""


def selection_sort(array):
    length = len(array)
    for i in range(length):
        min_index = i
        for j in range(i + 1, length):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array
