n = int(input())
berries = []
negative_berries = []
for i in range(n):
    a, b = map(int, input().split())
    if (a-b >= 0):
        berries.append((a, b, i + 1, a - b))
    else:
        negative_berries.append((a, b, i + 1, a - b))
berries.sort(key=lambda x: (-x[1]), reverse=True)
negative_berries.sort(key=lambda x: (x[0]), reverse=True)
berries = berries + negative_berries
print(berries)
current_height = 0
max_height = 0
order = []
max_negative = 0
positive_max = 0

for berry in berries:
    a, b, index, diff = berry
    current_height += a
    if current_height > max_height:
        max_height = current_height
    current_height -= b
    order.append(index)

print(max_height)
print(*order)
