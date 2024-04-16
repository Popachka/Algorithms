def main():
    m = 8
    x = [[0 for _ in range(m)] for _ in range(m)]
    p = 0

    n = int(input())  # ввод числа клеток

    # ввод координат клеток и заполнение массива единицами
    for k in range(n):
        i, j = map(int, input().split())
        x[i - 1][j - 1] = 1

    p = 4 * n

    # просмотр массива по горизонтали
    for i in range(m):
        for j in range(m - 1):
            if x[i][j] == 1 and x[i][j + 1] == 1:
                p -= 2

    # просмотр массива по вертикали
    for j in range(m):
        for i in range(m - 1):
            if x[i][j] == 1 and x[i + 1][j] == 1:
                p -= 2

    print(p)  # вывод результата

if __name__ == "__main__":
    main()
