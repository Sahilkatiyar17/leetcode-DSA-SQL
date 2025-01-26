class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return 0
        l, h = 0, len(nums) - 1
        while l <= h:  # Fix the condition from l < h to l <= h
            mid = (l + h) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                h = mid - 1

        # l is the correct insert position after the loop
        return l
