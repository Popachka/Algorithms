n = int(input())
row = []
ans = 0
for i in range(n):
    a = int(input())
    ost_4 = a % 4 
    int_4 = a // 4
    if (ost_4 == 0 and int_4 == 0):
        row.append('NoChange')
        ans += 0
    elif (ost_4 == 3):
        if (int_4 == 0):
            row.append('1tab1backspace')
            ans += 2
        else:
            row.append(f'{int_4 + 1}tab1backspace')
            ans += 1 + int_4+1
    elif (ost_4 == 2):
        if (int_4 == 0):
            row.append('2space')
            ans += 2
        else:
            row.append(f'{int_4}tab2backspace')
            ans += int_4 + 2
    elif (ost_4 == 1):
        if (int_4 == 0):
            row.append('1space')
            ans += 1
        else:
            row.append(f'{int_4}tab1space')
            ans += int_4 + 1
    else:
        row.append(f'{int_4}tab')
        ans += int_4
    print('tagr  ', int_4, 'ost ', ost_4)
    print(row)

print(ans)
