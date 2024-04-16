from collections import defaultdict
n = int(input())
ans = []

def f(s):
    ans = 0
    prefix = defaultdict(int)
    suffix = defaultdict(int)
    for i in range(len(s)):
        tmp_prefix = s[:i] 
        tmp_suffix = s[i:] 
        prefix[tmp_prefix] += 1
        suffix[tmp_suffix] += 1

    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if prefix[s[i:j]] > 0 and suffix[s[i:j]] > 0:
                continue
            ans += prefix[s[i:j]] + suffix[s[i:j]]
    if ans > 0:
        ans -= 1
    return ans 



for i in range(n):
    s = str(input())
    ans.append(f(s))
for a in ans:
    print(a)