def getRemovableIndices(str1, str2):
    """
    Problem: Find all indices in str1 such that removing the character at that
    index makes str1 equal to str2. If no such index exists, return [-1].

    Example:
    str1 = "abc", str2 = "ab"
    → Removable index = [2] (removing 'c')

    Approach:
    - Compare characters of str1 and str2 from left to right.
    - On the first mismatch, try skipping the character at str1[i].
    - If the remainder matches, record i as removable.
    - Additionally, if str1 matches str2 up to the end, then the last
      character of str1 is also removable.
    - Return all such indices, or [-1] if none exist.
    """

    i = j = 0
    removable_positions = []

    while i < len(str1) and j < len(str2):
        if str1[i] == str2[j]:
            i += 1
            j += 1
        else:
            # try skipping str1[i]
            if str1[i+1:] == str2[j:]:
                removable_positions.append(i)
            i += 1
            j += 1
            break

    # If everything matched until the end, last char of str1 is removable
    if j == len(str2):
        removable_positions.append(len(str1) - 1)

    return removable_positions or [-1]
