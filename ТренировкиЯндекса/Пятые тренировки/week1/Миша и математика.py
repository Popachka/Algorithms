n = int(input())
a =  list(map(int, input().split()))
res = chr(43) * (n - 1)
if not sum(a)%2:
    for i, v in enumerate(a):
        if v % 2 == 1:
            break
    i = max(0, i-1)
    res = res[:i] + chr(120) + res[i+1:]
print(res)