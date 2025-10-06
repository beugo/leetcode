class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        def prefix_products(arr):
            total = 1
            out = []
            for num in arr:
                out.append(total)
                total *= num
            return out

        left = prefix_products(nums)
        right = prefix_products(nums[::-1])[::-1]

        return [l * r for l, r in zip(left, right)]
        
        return output