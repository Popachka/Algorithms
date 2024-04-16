test = 'AAABBCCEE'
def pack(s,cnt):
    if cnt > 1:
        return s + str(cnt)
    return s
last = test[0]
ans = []
lastpos = 0
for i in range(1,len(test)):
    if last != test[i]:
        ans.append(pack(last, i - lastpos))
        lastpos = i
        last = test[i]
ans.append(pack(test[lastpos], len(test) - lastpos))
print(''.join(ans))