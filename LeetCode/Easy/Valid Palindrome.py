class Solution:
    def isPalindrome(self, s: str) -> bool:
        lo, hi = 0, len(s) - 1
        s = s.lower()
        while lo < hi:
            while lo < hi and not s[lo].isalnum(): lo+=1
            while lo < hi and not s[hi].isalnum(): hi-=1

            if s[lo] != s[hi]: return False
            lo +=1
            hi -= 1
        return True