class Solution:
    def reverseWords(self, s: str) -> str:
        words = [w for w in s.strip().split(" ") if w]
        return " ".join(reversed(words))