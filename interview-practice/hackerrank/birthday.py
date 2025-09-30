#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    count = 0
    
    # step 1: initial window sum
    window_sum = sum(s[:m])
    
    # step 2: check the first window
    if window_sum == d:
        count += 1
    
    # step 3: slide the window
    for i in range(m, len(s)):
        window_sum += s[i] - s[i - m]  # add new, remove old
        if window_sum == d:
            count += 1
    
    return count


    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    print(str(result) + '\n')

