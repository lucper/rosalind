#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given two strings s and t of equal length, the Hamming distance between s and t, 
denoted dH(s,t), is the number of corresponding symbols that differ in s and t.

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t).
"""

def hamming_distance(strand1,strand2):
    """
    nucleobase_index = hamming = 0
    while nucleobase_index < len(strand1):
        if strand1[nucleobase_index] != strand2[nucleobase_index]:
            hamming += 1
        nucleobase_index += 1
    return hamming
    """
    return sum(nucleobase1 != nucleobase2 for nucleobase1, nucleobase2 in zip(strand1,strand2))

def read_dataset(file_name):
    with open(file_name) as file:
        first_line = file.readline().strip()
        second_line = file.readline().strip()
    return (first_line, second_line)

if __name__ == '__main__':
    strands = read_dataset('rosalind_hamm.txt')
    result = hamming_distance(strands[0],strands[1])
    print(result)
