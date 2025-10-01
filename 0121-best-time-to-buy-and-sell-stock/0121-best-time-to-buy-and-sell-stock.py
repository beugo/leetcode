class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_price = prices[0]
        best = 0
        for p in prices[1:]:
            if p < min_price:
                min_price = p
            elif p - min_price > best:
                best = p - min_price
        return best