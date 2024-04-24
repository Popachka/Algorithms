class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = {}, {}
        res, resLen = [-1, -1], float('inf')

        lo = 0

        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)

        for right in range(len(s)):
            char = s[right]
            window[char] = 1 + window.get(char, 0)

            if char in countT and window[char] == countT[char]:
                have += 1

            while have == need:
                length = right - lo + 1
                if length < resLen:
                    resLen = length
                    res = [lo, right]

                window[s[lo]] -= 1

                if s[lo] in countT and window[s[lo]] < countT[s[lo]]:
                    have -= 1

                lo += 1
        return s[res[0]:res[1]+1]
