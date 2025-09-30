def is_anagram(s, t):
    if len(s) != len(t):
        return False
    
    counts = [0] * 26  # one slot per letter
    
    for ch in s:
        counts[ord(ch) - ord('a')] += 1
    
    for ch in t:
        counts[ord(ch) - ord('a')] -= 1
    
    # if all counts are zero, it's an anagram
    return all(c == 0 for c in counts)