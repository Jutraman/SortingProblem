"""
Project name: SortingProblem
File name: QuickSort.py
Description: 
version: 
Author: Jutraman
Email: jutraman@hotmail.com
Date: 11/07/2021 18:30
LastEditors: Jutraman
LastEditTime: 11/07/2021
Github: https://github.com/Jutraman
"""

def partition(array,left,right):
    pivot=left
    index=pivot+1

    for i in range(index,right+1):
        if array[i]<array[pivot]:
            array[i],array[index]=array[index],array[i]
    array[pivot],array[index-1]=array[index-1],array[pivot]

    return index-1

def quicksort(array,left,right):
    length = len(array)

    if left<right:
        partitionIndex=partition(array,left,right)
        quicksort(array,left,partitionIndex-1)
        quicksort(array,partitionIndex+1,right)

    return array


