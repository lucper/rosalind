#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A string is simply an ordered collection of symbols selected from some alphabet and 
formed into a word; the length of a string is the number of symbols that it contains.

An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 
'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

Given: A DNA string s of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in ss.
"""

def read_dataset(file_name):
    with open(file_name) as file:
        sequence = file.read()
    return sequence

def count_bases(sequence):
    adenine = 0
    cytosine = 0
    guanine = 0
    thymine = 0
    for nucleobase in sequence:
        if nucleobase == 'A':
            adenine += 1
        elif nucleobase == 'C':
            cytosine += 1
        elif nucleobase == 'G':
            guanine += 1
        elif nucleobase == 'T':
            thymine += 1
        else:
            continue
    return (adenine, cytosine, guanine, thymine)

if __name__ == '__main__':
    sequence = read_dataset('rosalind_dna.txt')
    result = count_bases(sequence)
    print('{} {} {} {}'.format(result[0],result[1],result[2],result[3]))
