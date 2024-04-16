from collections import defaultdict
n, k = map(int, input().split())

numbers = list(map(int,input().split()))
def f(k, numbers):
    window = defaultdict(int)
    for i in range(k+1):
        if len(numbers)-1 < i:
            break
        if numbers[i] in window and window[numbers[i]] == True:
            print('YES')
            return
        window[numbers[i]] = True
    for i in range(k+1, len(numbers)):
        window[numbers[i - k - 1]] = False
        if numbers[i] in window and window[numbers[i]] == True:
            print('YES')
            return
        window[numbers[i]] = True
    print('NO')
    return
f(k,numbers)