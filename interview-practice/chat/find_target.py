def find_target(arr, target):
    """
    Problem: Given an array of integers and a target sum, return the indices of
    the two numbers that add up to the target. Assume exactly one solution exists.

    Example:
    arr = [2, 7, 11, 15], target = 9
    → 2 + 7 = 9 → Output = [0, 1]

    Approach:
    - Use a hash map (dictionary) to store numbers we've seen and their indices.
    - For each number:
        - Compute its complement (target - num).
        - If the complement is already in the dictionary, we found a pair.
        - Otherwise, add the current number and index to the dictionary.
    - Return the indices once a match is found.

    Complexity:
    - Time: O(n), single pass through arr.
    - Space: O(n), storing up to all elements in dictionary.
    """

    complements = {}
    for i, num in enumerate(arr):
        complement = target - num
        if complement in complements:
            return [complements[complement], i]
        complements[num] = i
