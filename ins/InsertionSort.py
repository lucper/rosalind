#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
"""
Insertion sort is a simple algorithm with quadratic running time that builds the 
final sorted array one item at a time.

Given: A positive integer n≤10^3 and an array A[1..n] of integers.

Return: The number of swaps performed by insertion sort algorithm on A[1..n].
"""

def read_dataset(file_name):
    with open(file_name) as file:
        array_length = int(file.readline())
        array = [int(value) for value in file.readline().split()]
    return array, array_length

def insertion_sort(array, array_length):
    global number_of_swaps
    for index in range(1, array_length):
        index_being_analyzed = index
        while index_being_analyzed > 0 and array[index_being_analyzed] < array[index_being_analyzed-1]:
            array[index_being_analyzed], array[index_being_analyzed-1] = array[index_being_analyzed-1], array[index_being_analyzed]
            number_of_swaps += 1
            index_being_analyzed -= 1
            
if __name__ == '__main__':
    array, array_length = read_dataset('rosalind_ins.txt')
    number_of_swaps = 0
    insertion_sort(array, array_length)
    print('Sorted array: {}\nNumber of swaps: {}'.format(array, number_of_swaps))
