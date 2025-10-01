def rob(nums):
    """
    Problem: Given a list of non-negative integers representing the amount of
    money in each house along a street, determine the maximum amount of money
    that can be robbed without robbing two adjacent houses.
    (Classic "House Robber" dynamic programming problem.)

    Example:
    nums = [2, 7, 9, 3, 1]
    → Best choice: rob houses with 2, 9, and 1 → Output = 12

    Approach:
    - Use dynamic programming with rolling variables.
    - prev1: max robbed amount up to the previous house.
    - prev2: max robbed amount up to the house before that.
    - For each house:
        - Either skip it (keep prev1),
        - Or rob it (prev2 + current value).
    - Return prev1 as the maximum total at the end.

    Complexity:
    - Time: O(n), one pass through nums.
    - Space: O(1), only two state variables.
    """

    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    prev2, prev1 = 0, 0
    for x in nums:
        cur = max(prev1, prev2 + x)
        prev2, prev1 = prev1, cur
    return prev1
