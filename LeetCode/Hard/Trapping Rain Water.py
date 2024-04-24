class Solution:
    def trap(self, height: list[int]) -> int:
        lo, hi = 0, len(height) - 1
        MaxL = height[lo]
        MaxHi = height[hi]
        ans = 0
        while lo < hi:
            if MaxL <= MaxHi:
                lo += 1
                print(lo)
                tmp = max(0, MaxL - height[lo])
                MaxL = max(MaxL, height[lo])
            else:
                hi -= 1
                tmp = max(0, MaxHi - height[hi])
                MaxHi = max(MaxHi, height[hi])
            ans += tmp
        return ans
