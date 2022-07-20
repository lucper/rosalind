#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.

Given a DNA string t corresponding to a coding strand, its transcribed RNA string u is 
formed by replacing all occurrences of 'T' in t with 'U' in u.

Given: A DNA string t having length at most 1000 nt.

Return: The transcribed RNA string of t.
"""

def read_dataset(file_name):
    with open(file_name) as file:
        sequence = file.read().strip()
    return sequence

def transcribe_dna(strand):
    """
    return strand.replace("T","U")
    """
    rna_strand = strand[:]
    for nuclebase_index in range(0,len(rna_strand)):
        if rna_strand[nuclebase_index] == 'T':
            rna_strand[nuclebase_index] = 'U'
    return rna_strand

if __name__ == '__main__':
    """
    strand = read_dataset('rosalind_rna.txt')
    print(transcribe_dna(strand))
    """
    strand = list(read_dataset('rosalind_rna.txt'))
    result = transcribe_dna(strand)
    print("".join(result))
