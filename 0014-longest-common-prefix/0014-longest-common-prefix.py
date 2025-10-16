class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs or "" in strs:
            return ""
        
        prefix = ""
        for group in zip(*strs):
            if len(set(group)) == 1:
                prefix += group[0]
            else:
                break
        return prefix