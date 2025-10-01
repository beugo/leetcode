def birthday(s, d, m):
    """
    Problem: Count the number of contiguous segments of length m in the list s
    such that the sum of each segment equals d.
    
    Example:
    s = [1, 2, 1, 3, 2], d = 3, m = 2
    Valid segments: [1, 2], [2, 1] → Output = 2
    
    Approach:
    - Use a sliding window of size m across the list.
    - Keep track of the current window sum.
    - For each step, update the window sum in O(1) by adding the new element
      and removing the oldest element.
    - Count how many times the sum equals d.
    
    Complexity:
    - O(n) time (single pass with window updates).
    - O(1) extra space.
    """

    count = 0

    # initial window sum
    window_sum = sum(s[:m])
    if window_sum == d:
        count += 1

    # slide the window
    for i in range(m, len(s)):
        window_sum += s[i] - s[i - m]
        if window_sum == d:
            count += 1

    return count
