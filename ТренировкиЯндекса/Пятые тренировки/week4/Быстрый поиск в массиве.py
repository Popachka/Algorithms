def binary(numbers, target):
    l = 0
    r = len(numbers)
    while l < r:
        mid = (l + r) // 2
        if numbers[mid] < target:
            l = mid + 1
        else:
            r = mid
    return l 
        
def binary_r(numbers, target):
    l = 0
    r = len(numbers)
    while l < r:
        mid = (l + r) // 2
        if numbers[mid] <= target:
            l = mid + 1
        else:
            r = mid
    return l 
                   
N = int(input())
numbers = list(map(int,input().split()))
numbers.sort()
ans = []

K = int(input())

for i in range(K):
    L, R = map(int,input().split())
    left_index = binary(numbers, L)
    right_index = binary_r(numbers, R)
    print(right_index - left_index)
