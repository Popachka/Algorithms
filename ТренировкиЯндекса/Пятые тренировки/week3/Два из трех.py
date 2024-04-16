n = int(input())
arr1 = list(map(int,input().split()))
ans = set()
n = int(input())
arr2 = list(map(int,input().split()))
n = int(input())
arr3 = list(map(int,input().split()))

res1 = set(arr1) - (set(arr1) - set(arr2))
res2 = set(arr1) - (set(arr1) - set(arr3))
res3 = set(arr2) - (set(arr2) - set(arr3))

res = res1 | res2 | res3
print(*sorted(res))