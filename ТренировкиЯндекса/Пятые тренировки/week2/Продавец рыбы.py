N, K = map(int,input().split())

list_N = list(map(int,input().split()))
income = 0
for _ in range(K):
    list_N.append(-10**9)
print(list_N)
for i in range(len(list_N) - K - 1):
    buy = list_N[i]
    print('buy ', buy)
    for j in range(i+1, i+1+K):
        sell = list_N[j]
        print('sell ', sell)
        if sell - buy > income:
            income = sell - buy
            print('income ', income)

print('income ', income)