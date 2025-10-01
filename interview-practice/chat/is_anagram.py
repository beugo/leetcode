def is_anagram(s, t):
    """
    Problem: Determine if two strings s and t are anagrams.
    Two strings are anagrams if they contain the same characters
    in the same frequency, regardless of order.

    Example:
    s = "anagram", t = "nagaram" → True
    s = "rat", t = "car" → False

    Approach:
    - If lengths differ, they cannot be anagrams.
    - Use a fixed-size count array of length 26 (for lowercase a–z).
    - Increment counts for characters in s, decrement for characters in t.
    - If all counts return to zero, then s and t are anagrams.

    Complexity:
    - Time: O(n), where n = length of s (and t).
    - Space: O(1), since the count array is fixed size (26).
    """

    if len(s) != len(t):
        return False

    counts = [0] * 26  # one slot per letter

    for ch in s:
        counts[ord(ch) - ord('a')] += 1

    for ch in t:
        counts[ord(ch) - ord('a')] -= 1

    return all(c == 0 for c in counts)
