#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getRemovableIndices' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING str1
#  2. STRING str2
#

def getRemovableIndices(str1, str2):
    i = j = 0
    removable_positions = []
    while i < len(str1) and j < len(str2):
        if str1[i] == str2[j]:
            i += 1
            j += 1
        else:
            # try skipping str1[i]
            if str1[i+1:] == str2[j:]:
                removable_positions.append(i)
            i += 1  # skip ahead
            j += 1  # only advance str2 if you want to continue
            break
    
    # If everything matched until the end, last char of str1 is removable
    if j == len(str2):
        removable_positions.append(len(str1) - 1)

    return removable_positions or [-1]
        
        

if __name__ == '__main__':
    str1 = input()

    str2 = input()

    result = getRemovableIndices(str1, str2)

    print('\n'.join(map(str, result)))
