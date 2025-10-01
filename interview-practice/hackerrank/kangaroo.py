def kangaroo(x1, v1, x2, v2):
    """
    Problem: Two kangaroos start at positions x1 and x2 on a number line and 
    jump forward at constant rates v1 and v2. Determine if they will ever land 
    on the same location after the same number of jumps.

    Example:
    x1 = 0, v1 = 3, x2 = 4, v2 = 2
    → Both land at 12 after 4 jumps → Output: "YES"

    Approach:
    - If they start at the same spot, answer is "YES".
    - If velocities are equal but starting positions differ, they'll never meet.
    - Otherwise, check if the faster kangaroo starts behind the slower one and
      the relative gap is divisible by their velocity difference.
    - If so, they meet; otherwise, they don’t.
    """

    # Same start point
    if x1 == x2:
        return "YES"

    # If speeds equal but starts differ, they'll never meet
    if v1 == v2:
        return "NO"

    # Identify who is behind and the relative speed closing the gap
    if v1 > v2:
        diff = x2 - x1         # gap from kangaroo1 (behind) to kangaroo2 (ahead)
        dv = v1 - v2           # gap shrinks per jump
    else:
        diff = x1 - x2
        dv = v2 - v1

    # If the faster one isn't behind, they can't meet
    if diff < 0:
        return "NO"

    # Shrink the gap jump-by-jump without updating absolute positions
    while diff > 0:
        diff -= dv

    return "YES" if diff == 0 else "NO"
