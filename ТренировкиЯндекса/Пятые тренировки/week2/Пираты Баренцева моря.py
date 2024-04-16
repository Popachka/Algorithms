n = int(input())
ans = []
coors = [tuple(map(int,input().split())) for _ in range(n)]
def f(coors,n):
    d = []
    for col in range(1, n+1):
        sum = 0
        ships = [(x,y) for x,y in coors if y != col]
        afk_ships = [x for x,y in coors if y == col]
        moving_ships = set(range(1,n+1)) - set(afk_ships)
        for i, x in enumerate(moving_ships):
            sum += abs(x - ships[i][0]) + abs(col - ships[i][1])
        d.append(sum)
    return min(d)
coors.sort(key=lambda x: x[1])
ans.append(f(coors,n))
coors.sort(key=lambda x: x[0])
ans.append(f(coors,n))

print(min(ans))
