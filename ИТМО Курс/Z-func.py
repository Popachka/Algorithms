def z_func(s, n):
    z = [0] * n
    for i in range(1, n):
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
    return z

def count_good_substrings(s, t):
    ss = t + '$' + s
    z = z_func(ss, len(ss))
    
    cnt = 0
    for i in range(len(t) + 1, len(z)):
        if z[i] >= len(t):
            cnt = 1
    
    return cnt

n = int(input())
sum = 0
for _ in range(n):
    s = input().strip()
    t = input().strip()
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            string = s[i:j]
            sum += 1
            result = count_good_substrings(string, t)
            sum -= result
    print(sum)
