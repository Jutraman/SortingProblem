"""
Project name: SortingProblem
File name: HeapSort.py
Description: 
version: 
Author: Jutraman
Email: jutraman@hotmail.com
Date: 11/07/2021 19:22
LastEditors: Jutraman
LastEditTime: 11/07/2021
Github: https://github.com/Jutraman
"""


def buildMaxHeap(array):
    length = len(array)
    i = length / 2
    while i >= 0:
        heapify(array, i)
        i -= 1


def heapify(array, i, length):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i

    if left < length & array[left] > array[largest]:
        largest = left

    if right < length & array[right] > array[largest]:
        largest = right

    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, largest, length)


def heapSort(array):
    buildMaxHeap(array)

    length = len(array)
    i = length - 1
    while i > 0:
        array[0], array[i] = array[i], array[0]
        length -= 1
        heapify(array, 0, length)
