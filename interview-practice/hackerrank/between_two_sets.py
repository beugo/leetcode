#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    total = 0
    start = max(a)
    end = min(b)

    numbers = []

    for i in range(start, end + 1, start):  # step by max(a)
        # check condition 1: every a[j] divides i
        if all(i % num == 0 for num in a):
            # check condition 2: i divides every b[k]
            if all(num % i == 0 for num in b):
                total += 1
                numbers.append(i)

    print(numbers)
    return total

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    print(str(total) + '\n')