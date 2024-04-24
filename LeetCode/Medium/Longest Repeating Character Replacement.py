class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        count = {}
        ans = 0
        maxf = 0
        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)
            maxf = max(maxf, count[s[right]])
            while (right - i + 1) - maxf > k:
                count[s[i]] -= 1
                i += 1
            ans = max(ans, right - i + 1)
        return ans
