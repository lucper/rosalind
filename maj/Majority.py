#!/usr/bin/env python
"""
Return majority element: element that occurs > N/2 times in array, for array of size N.
"""

import fileinput

def occ(arr, item):
    return sum(1 for val in arr if val == item)

def majority(arr):
    if len(arr) == 1:
        return *arr, 1
    else:
        mid = len(arr) // 2
        lmaj, locc = majority(arr[:mid])
        rmaj, rocc = majority(arr[mid:])
        if lmaj and rmaj:
            if lmaj == rmaj:
                return lmaj, locc + rocc
            elif lmaj != rmaj:
                rocc += occ(arr[:mid], rmaj)
                locc += occ(arr[mid:], lmaj)
                if rocc > locc:
                    return rmaj, rocc
                elif rocc < locc:
                    return lmaj, locc
        elif not lmaj and rmaj:
            rocc += occ(arr[:mid], rmaj)
            if rocc > mid:
                return rmaj, rocc
        elif not rmaj and lmaj:
            locc += occ(arr[mid:], lmaj)
            if locc > mid:
                return lmaj, locc
        return None, -1

if __name__ == '__main__':
    with fileinput.input() as fin:
        next(fin) # skip 1st line
        results = [majority(line.split()) for line in fin]
        print(" ".join(str(m) if o > 0 else str(o) for m, o in results))
