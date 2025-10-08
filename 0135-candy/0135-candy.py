class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        out = [1] * n

        for i in range(1, n):            
            if ratings[i - 1] < ratings[i]:
                out[i] = out[i - 1] + 1
                
        for i in range(n - 2, -1, -1):
            if ratings[i + 1] < ratings[i]:
                out[i] = max(out[i], out[i + 1] + 1)

        return sum(out)
