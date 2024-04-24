class Solution:
    def maxArea(self, height: list[int]) -> int:
        lo, hi = 0, len(height) - 1
        ans = -1
        while lo <= hi:
            height_min = min(height[lo], height[hi])
            axis = hi - lo
            S = axis * height_min
            ans = max(S, ans)
            if height[lo] > height[hi]:
                hi -= 1
            else:
                lo += 1
        return ans
