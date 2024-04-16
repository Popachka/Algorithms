n = int(input())
ans = []
for i in range(n):
    s = str(input())
    t = str(input())
    cnt = 0 
    sum = 0   
    for j in range(len(s)):
        for g in range(j+1, len(s)+1):
            sum +=1
            if t in s[j:g]:
                cnt += 1
    ans.append(sum - cnt)
for i in ans:
    print(i)