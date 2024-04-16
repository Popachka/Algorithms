N = int(input())
fortuna = list(map(int,input().split()))
a, b, k = map(int, input().split())
max_fortuna = max(fortuna)
max = 0
def is_integer(x):
    return x % 1 == 0

for i in range(a, b+1, k):
    if is_integer(i / k):
        divine = (i // k) - 1
    else:
        divine = (i // k)
    mod = divine % N
    left = fortuna[-mod]
    right = fortuna[mod]
    if left > max:
        max = left
    if right > max:
        max = right
    if max_fortuna == max:
        break
print(max)