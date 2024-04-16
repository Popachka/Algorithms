n = int(input())

def tetrahedral_number(n):
    # Функция, вычисляющая n-ое тетраэдрическое число
    return (n * (n + 1) * (n + 2)) // 6

def max_ships(n):
    # Функция, которая находит максимальное количество кораблей, которое можно разместить
    # на поле размером 1 x n, используя тетраэдрические числа
    k = 1
    while tetrahedral_number(k) < n:
        k += 1
    return k
print(max_ships(n) - 1)