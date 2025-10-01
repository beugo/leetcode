from math import inf

def msa(nums, target):
    """
    Problem: Given an array of positive integers nums and a target sum,
    find the minimal length of a contiguous subarray of which the sum ≥ target.
    If no such subarray exists, return 0.
    (This is the "Minimum Size Subarray Sum" problem.)

    Example:
    nums = [2, 3, 1, 2, 4, 3], target = 7
    → Smallest subarray = [4, 3] → length = 2

    Approach:
    - Use a sliding window:
        - Expand the right pointer, adding to the running sum.
        - While the current sum ≥ target, update min_len and shrink from the left.
    - If no valid window is found, return 0.

    Complexity:
    - Time: O(n) (each element added/removed once).
    - Space: O(1).
    """

    min_len = inf
    curr_sum = 0
    left = 0

    for right in range(len(nums)):
        curr_sum += nums[right]

        while curr_sum >= target:
            min_len = min(min_len, right - left + 1)
            curr_sum -= nums[left]
            left += 1

    return 0 if min_len == inf else min_len
