class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        p = 2
        for i in range(2, n):
            if nums[i] != nums[p - 2]:
                nums[p] = nums[i]
                p += 1
        return p