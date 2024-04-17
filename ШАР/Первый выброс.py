def find_outlier_day(N, K, metrics):
    for i in range(K, N):
        previous_days = sorted(metrics[i-K:i])  # Значения за предыдущие дни
        threshold = previous_days[int(K * 0.9)]  # Пороговое значение (90%)
        if metrics[i] > threshold:
            return i + 1  # Номер дня, считая от 1
    return -1  # Если выбросов нет

# Чтение ввода
N = int(input())
K = int(input())
metrics = list(map(int, input().split()))

outlier_day = find_outlier_day(N, K, metrics)
print(outlier_day)
