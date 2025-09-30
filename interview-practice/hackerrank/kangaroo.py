def kangaroo(x1, v1, x2, v2):
    # Same start point
    if x1 == x2:
        return "YES"

    # If speeds equal but starts differ, they'll never meet
    if v1 == v2:
        return "NO"

    # Identify who is behind and the relative speed closing the gap
    if v1 > v2:
        diff = x2 - x1         # gap from kangaroo1 (behind) to kangaroo2 (ahead)
        dv = v1 - v2           # how much the gap shrinks per jump
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