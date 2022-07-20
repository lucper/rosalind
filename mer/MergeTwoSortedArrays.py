#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given: A positive integer n≤105 and a sorted array A[1..n] of integers from −105 to 
105, a positive integer m≤105 and a sorted array B[1..m] of integers from −105 to 105.

Return: A sorted array C[1..n+m] containing all the elements of A and B.
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

if __name__ == '__main__':
    with open('rosalind_mer.txt') as file:
        left_length, left_list, right_length, right_list = file.readlines() # returns a list with the lines read
        left_list = [int(value) for value in list(left_list.split())]
        right_list = [int(value) for value in list(right_list.split())]
    with open('rosalind_mer_result.txt', 'w') as file:
        file.write(" ".join([str(value) for value in merge(left_list, right_list)]))
