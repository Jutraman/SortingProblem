"""
Project name: SortingProblem
File name: BubbleSort.py
Description: 
version: 
Author: Jutraman
Email: jutraman@hotmail.com
Date: 04/07/2021 21:49
LastEditors: Jutraman
LastEditTime: 04/07/2021
Github: https://github.com/Jutraman
"""


def bubble_sort(array):
    length = len(array)
    for i in range(length):
        for j in range(length - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array