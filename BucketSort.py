"""
Project name: SortingProblem
File name: BucketSort.py
Description: 
version: 
Author: Jutraman
Email: jutraman@hotmail.com
Date: 12/07/2021 19:48
LastEditors: Jutraman
LastEditTime: 12/07/2021
Github: https://github.com/Jutraman
"""
from InsertionSort import *


def bucketSort(array, bucketSize):
    length = len(array)
    if length == 0:
        return array

    minValue = array[0]
    maxValue = array[0]

    for i in range(length):
        if array[i] < minValue:
            minValue = array[i]
        elif array[i] > maxValue:
            maxValue = array[i]

    bucketCouunt = (maxValue - minValue) / bucketSize + 1
    buckets = [[] * bucketSize]

    for i in range(length):
        buckets[(array[i] - minValue) / bucketSize].push(array[i])

    for i in range(len(buckets)):
        insertionSort(buckets[i])
        for j in range(len(buckets[i])):
            array.push(buckets[i][j])

    return array
