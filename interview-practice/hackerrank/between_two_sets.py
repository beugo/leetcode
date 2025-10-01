def getTotalX(a, b):
    """
    Problem: Find the number of integers that are "between" two sets.

    Rules:
    - Every integer x considered must be divisible by all elements in array a.
    - Every integer x considered must also divide all elements in array b.
    - Return the count of such integers.

    Example:
    a = [2, 4], b = [16, 32, 96]
    Valid numbers are {4, 8, 16}, so output = 3.

    Approach:
    - The candidates must lie between max(a) and min(b).
    - Step through multiples of max(a).
    - For each candidate, check both divisibility conditions.
    """

    total = 0
    start = max(a)
    end = min(b)

    for i in range(start, end + 1, start):  # only multiples of max(a)
        if all(i % num == 0 for num in a):      # divisible by all in a
            if all(num % i == 0 for num in b):  # divides all in b
                total += 1

    return total
