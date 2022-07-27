#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given two strings s and t of equal length, the Hamming distance between s and t, 
denoted dH(s,t), is the number of corresponding symbols that differ in s and t.

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t).
"""

import fileinput

def hamming(dna1, dna2):
    return sum(base1 != base2 for base1, base2 in zip(dna1,dna2))

if __name__ == '__main__':
    with fileinput.input() as fin:
        strands = [line.strip() for line in fin]

    print(hamming(*strands))
