#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
"""
Given: A positive integer n≤105 and an array A[1..n] of integers from −105 to 105.

Return: A sorted array A[1..n].
"""

def merge(left, right):
    result = []
    left_index, right_index = 0, 0
    # Must be an AND operator to avoid IndexError (list index out of range)
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    # Append the remaining elements
    while left_index < len(left):
        result.append(left[left_index])
        left_index += 1
    while right_index < len(right):
        result.append(right[right_index])
        right_index += 1
    return result

def merge_sort(array):
    if len(array) == 1:
        return array[:]
    else:
        middle_index = len(array) // 2
        left = merge_sort(array[:middle_index])
        right = merge_sort(array[middle_index:])
        return merge(left, right)

if __name__ == "__main__":
    with open("rosalind_ms.txt") as file:
        _ = int(file.readline())
        array = [int(value) for value in file.readline().split()]
    with open("rosalind_ms_result.txt", "a") as file:
        sorted_array = merge_sort(array)
        file.write(" ".join([str(value) for value in sorted_array]))
