class Solution:
    def search(self, nums: list[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1

        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[lo]:
                if target < nums[lo] or target > nums[mid]:
                    lo = mid + 1
                else:
                    hi = mid
            else:
                if target < nums[mid] or target > nums[hi]:
                    hi = mid
                else:
                    lo = mid + 1
        return lo if nums[lo] == target else -1