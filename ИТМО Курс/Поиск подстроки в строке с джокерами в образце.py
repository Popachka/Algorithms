n = int(input())
ans = []

def f(q,p):
    ans = []
    for start in range(len(q) - len(p) + 1):
        substr = q[start:len(p) + start]
        index_list = []
        for i in range(len(substr)):
            if substr[i] == p[i] or p[i] == '?':
                index_list.append(start)
            else:
                index_list = []
                break
        if len(index_list) != 0:
            for num in index_list:
                ans.append(num)
    return len(set(ans)), set(ans)
for i in range(n):
    q = str(input())
    p = str(input())
    ans.append(f(q,p))
for a, i_list in ans:
    print(a)
    print(*i_list)