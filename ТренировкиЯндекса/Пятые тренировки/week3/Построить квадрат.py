def find_squares(N, points):
    points = list(points)
    
    found_square = False
    
    for i in range(N):
        for j in range(i + 1, N):
            A = points[i] 
            B = points[j] 

            # Рассчитываем вектор между точками A и B
            V = (B[0] - A[0], B[1] - A[1])  
            # Находим координаты двух возможных вершин квадрата
            C = (A[0] + V[1], A[1] - V[0])
            D = (B[0] + V[1], B[1] - V[0])
            E = (A[0] - V[1], A[1] + V[0])
            F = (B[0] - V[1], B[1] + V[0])

            # Проверяем, есть ли найденные вершины квадрата в исходном множестве точек
            if C in points and D in points and E in points and F in points:
                found_square = True
                break
        
        if found_square:
            break

    if not found_square:
        # Если квадрат не был найден, добавляем только две дополнительные точки
        additional_points_ans = []
        min_point = 100
        for i in range(N):
            for j in range(i + 1, N):
                additional_points = []
                A = points[i]
                B = points[j]
                # Рассчитываем вектор между точками
                V = (B[0] - A[0], B[1] - A[1])
                # Находим координаты двух возможных вершин квадрата
                C = (A[0] + V[1], A[1] - V[0])
                D = (A[0] - V[1], A[1] + V[0])
                # Проверяем, есть ли эти вершины в исходном множестве точек
                if C not in points:
                    additional_points.append(C)
                if D not in points:
                    additional_points.append(D)
                if  len(additional_points) < min_point:
                    additional_points_ans = [*additional_points]
                    min_point = len(additional_points)
        return additional_points_ans

    return set()


N = int(input()) # кол-во точек
coords_list = set()

for i in range(N):
    x, y = map(int, input().split())
    coords_list.add((x, y))

additional_points = find_squares(N, coords_list)
print(len(additional_points))
for point in additional_points:
    print(point[0], point[1])
