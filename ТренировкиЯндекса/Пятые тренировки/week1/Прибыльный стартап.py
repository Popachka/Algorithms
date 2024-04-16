n, k, d = map(int, input().split())
numbers = '0123456789'
flag = True

if k == 0:
    flag = False

ans = '-1'

while d != 0 and flag:
    found = False

    for x in numbers:
        tmp_str = f'{n}{x}'
        tmp = int(tmp_str)

        if tmp % k == 0:
            if x == '0':
                n_str = str(n)
                n_str += '0' * d
                ans = n_str
                found = True
                flag = False
                break
            n = tmp
            ans = str(n)
            found = True
            break

    if not found:
        ans = '-1'
        flag = False

    d -= 1

print(ans)
