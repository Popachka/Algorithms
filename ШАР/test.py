import numpy as np

# Функция для поиска дня первого выброса
def find_outlier_day(N, K, metric_values):
    # Проходимся по дням, начиная с K-го
    for day in range(K, N):
        # Вычисляем 90-процентный квантиль для значений до текущего дня включительно
        threshold = np.percentile(metric_values[:day], 90)
        # Если текущее значение больше квантиля, то это выброс
        if metric_values[day] > threshold:
            return day + 1  # Номер дня, индексация с 1
    return -1  # Если выброс не найден

# Чтение ввода
N = int(input())
K = int(input())
metric_values = list(map(int, input().split()))

# Поиск дня первого выброса
result = find_outlier_day(N, K, metric_values)
print(result)
