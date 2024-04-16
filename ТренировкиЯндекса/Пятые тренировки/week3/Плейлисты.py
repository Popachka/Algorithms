n = int(input())

k = int(input())
fav_tracks0 = set(map(str,input().split()))
if n == 1:
    print(len(fav_tracks0))
    print(*sorted(fav_tracks0))
    exit()
for i in range(n-1):
    k = int(input())
    fav_tracks = set(map(str,input().split()))
    res = fav_tracks0 - (fav_tracks0 - fav_tracks)
    fav_tracks0 = res
print(len(res))
print(*sorted(res))
