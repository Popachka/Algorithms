n = int(input())
ans = []

def f(s):
    if s == s[::-1]:
        ans = len(s)
        return ans
    for i in range(1,len(s)):
        tmp = s[:-i]
        rev_tmp = tmp[::-1]
        if tmp == rev_tmp:
            ans = len(tmp)
            return ans
        
def dynamic_f(s):
    n = len(s)
    if n == 0:
        return 0
    dp = [[False] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = True
    max_length = 1
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i+1] = True
            max_length  = 2
    for length in range(3, n + 1):
        for start in range(n - length + 1):
            end = start + length - 1
            if s[start] == s[end] and dp[start+1][end-1]:
                dp[start][end] = True
                max_length = max(max_length, length)
    return max_length





for i in range(n):
    s = str(input())
    ans.append(dynamic_f(s))

for length in ans:
    print(length)
    