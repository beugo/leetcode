class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        back_of_1, back_of_2, back_of_final = m - 1, n - 1, m + n - 1

        while back_of_1 >= 0 and back_of_2 >= 0:
            if nums1[back_of_1] > nums2[back_of_2]:
                nums1[back_of_final] = nums1[back_of_1]
                back_of_1 -= 1
            else:
                nums1[back_of_final] = nums2[back_of_2]
                back_of_2 -= 1

            back_of_final -= 1
        
        while back_of_2 >= 0:
            nums1[back_of_final] = nums2[back_of_2]
            back_of_2 -= 1
            back_of_final -= 1