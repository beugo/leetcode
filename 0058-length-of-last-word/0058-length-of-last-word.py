class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        trimmed = s.strip().split(" ")
        return len(trimmed[-1])