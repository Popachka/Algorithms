K = int(input())
left = 10**9
right = 0
top = 0
bottom = 10**9
for _ in range(K):
    x, y = map(int,input().split())
    
    if x <= left:
        left = x
    if x >= right:
        right = x
    if y >= top:
        top = y
    if y <= bottom:
        bottom = y
print(left,bottom,right,top)