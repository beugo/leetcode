def solution(numbers):
    """
    Problem: Given a list of numbers, determine for each element (excluding the
    first and last) whether it is a local peak or valley.
    
    Rules:
    - A "peak" is when numbers[i] is greater than both neighbours.
    - A "valley" is when numbers[i] is smaller than both neighbours.
    - For each index i (1 .. len(numbers)-2), append:
        - 1 if numbers[i] is a peak or valley,
        - 0 otherwise.
    - Return the resulting list.

    Example:
    numbers = [1, 3, 2, 4, 5]
    → middle elements are 3, 2, 4
    - 3 is a peak (1 < 3 > 2) → 1
    - 2 is a valley (3 > 2 < 4) → 1
    - 4 is neither (2 < 4 < 5) → 0
    Output = [1, 1, 0]

    Approach:
    - Iterate from index 1 to len(numbers)-2.
    - Check peak/valley conditions with neighbours.
    - Append result to the output list.
    """
    return [
        1 if (numbers[i-1] < numbers[i] > numbers[i+1]) or (numbers[i-1] > numbers[i] < numbers[i+1]) else 0
        for i in range(1, len(numbers) - 1)
    ]
