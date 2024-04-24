class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        lo, hi = 0, len(numbers) - 1
        while lo <= hi:
            tmp = numbers[lo] + numbers[hi]
            if tmp == target:
                return [lo+1,hi+1]
            elif tmp > target:
                hi -= 1
            else:
                lo += 1