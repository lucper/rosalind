#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
"""
The problem is to find a given set of keys in a given array.

Given: Two positive integers n≤105 and m≤105, a sorted array A[1..n] of integers 
from −10^5 to 10^5 and a list of m integers −10^5≤k1,k2,…,km≤ 10^5.

Return: For each ki, output an index 1≤j≤n s.t. A[j]=ki or "-1" if there is 
no such index.
"""

def iterative_binary_search(array, key):
    low = 0
    high = len(array) - 1
    while low <= high:
        middle_index = (high + low) // 2
        if key == array[middle_index]:
            # O problema indexa a reposta começando em 1
            return middle_index + 1
        elif key < array[middle_index]:
            high = middle_index - 1
        elif key > array[middle_index]:
            low = middle_index + 1
    return -1

def recursive_binary_search(array, indexes, key):
    """
    Recebe, além do array e da key, uma lista de índices do array
    para que não se perca, durante as chamadas recursivas, os
    índices do array original, visto que o problema requer que
    o algoritmo retorne o índice.
    Essa solução usa mais memória já que alocamos espaço para duas
    listas!
    """
    middle_index = len(array) // 2
    if len(array) == 1 and key != array[middle_index]:
        return -1
    elif key == array[middle_index]:
        return indexes[middle_index]
    elif key > array[middle_index]:
        return recursive_binary_search(array[middle_index:], indexes[middle_index:], key)
    elif key < array[middle_index]:
        return recursive_binary_search(array[:middle_index], indexes[:middle_index], key)

if __name__ == "__main__":
    with open("rosalind_bins.txt") as file:
        array_size = int(file.readline())
        _ = int(file.readline())
        sorted_array = [int(value) for value in file.readline().split()]
        keys = [int(value) for value in file.readline().split()]
        
    with open("rosalind_bins_result.txt", "a") as file:
        for key in keys:
            result = str(recursive_binary_search(sorted_array, range(1,array_size), key))
            file.write("{} ".format(result))
