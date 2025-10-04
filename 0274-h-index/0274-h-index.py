class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        h = n
        for count in citations:
            if count < h:
                h -= 1
        
        return h