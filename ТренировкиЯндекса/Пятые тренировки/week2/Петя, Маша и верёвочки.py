N = int(input())
list_N = list(map(int,input().split()))

ans = 0
max_n = max(list_N)
sum_n = sum(list_N) - max_n

    

if (max_n == sum_n):
    ans = max_n+sum_n
else:
    ans = max_n - sum_n
    if (ans < 0):
        ans = sum_n + max_n
print(ans)