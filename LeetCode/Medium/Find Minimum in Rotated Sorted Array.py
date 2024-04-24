class Solution:
    def findMin(self, nums: list[int]) -> int:
        def condition(mid, y):
            return mid > y
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if condition(nums[mid], nums[hi]):
                lo = mid + 1
            else:
                hi = mid

        return nums[lo]