class Solution:
    def canJump(self, nums: List[int]) -> bool:
        steps_left = 0
        for n in nums:
            if steps_left < 0:
                return False
            elif n > steps_left:
                steps_left = n
            steps_left -= 1
            
        return True