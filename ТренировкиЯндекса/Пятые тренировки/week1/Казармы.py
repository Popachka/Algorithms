def calc(t,myunits,barhp,enemyprod):
    rounds = 0
    enemyunits = 0
    while barhp >= t:
        if enemyunits >= myunits:
            return 10**9
        barhp -= myunits - enemyunits
        enemyunits = 0
        if barhp > 0:
            enemyunits += enemyprod
        rounds += 1
    while barhp > 0:
        if myunits <= 0:
            return 10**9
        if barhp >= myunits:
            barhp -= myunits
        else:
            enemyunits -= myunits - barhp
            barhp = 0
        myunits -= enemyunits
        if barhp > 0:
            enemyunits += enemyprod
        rounds += 1
    while enemyunits > 0:
        if myunits <= 0:
            return 10**9
        enemyunits -= myunits
        if enemyunits > 0:
            myunits -= enemyunits
        rounds += 1
x = int(input())
y = int(input())
p = int(input())
ans = 10**9
for t in range(0, y + 2):
    ans = min(ans, calc(t,x,y,p))
if ans != 10**9:
    print(ans)
else:
    print(-1)