#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

The reverse complement of a DNA string s is the string s^c formed by reversing the symbols 
of s, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

Given: A DNA string s of length at most 1000 bp.

Return: The reverse complement s^c of s.
"""

def read_dataset(file_name):
    with open(file_name) as file:
        strand = file.read()
    return strand

def reverse_complement(dna_strand):
    base_pair = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    return [base_pair[nucleobase] for nucleobase in reversed(dna_strand)]

    """
    complement = []
    for nucleobase in dna_strand[::-1]:
        complement.append(base_pair[nucleobase])
    return complement
    """

    """
    complement = []
    for nucleobase in dna_strand[::-1]:
        if nucleobase == 'T':
            complement.append('A')
        elif nucleobase == 'A':
            complement.append('T')
        elif nucleobase == 'G':
            complement.append('C')
        elif nucleobase == 'C':
            complement.append('G')
        else:
            continue
    return complement
    """

if __name__ == '__main__':
    dna_strand = read_dataset('rosalind_revc.txt').strip()
    dna_strand_complement = reverse_complement(dna_strand)
    print("".join(dna_strand_complement))
