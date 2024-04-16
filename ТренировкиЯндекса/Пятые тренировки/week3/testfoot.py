# Открываем оба файла для сравнения
file1_path = "Alg\ТренировкиЯндекса\Пятые тренировки\week3\output.txt"
file2_path = "Alg\ТренировкиЯндекса\Пятые тренировки\week3\\real_output.txt"

with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
    # Считываем строки обоих файлов
    lines_file1 = file1.readlines()
    lines_file2 = file2.readlines()

    # Определяем максимальное количество строк, чтобы обработать оба файла полностью
    max_lines = max(len(lines_file1), len(lines_file2))

    # Проходимся построчно и сравниваем строки
    for i in range(max_lines):
        # Если в одном из файлов закончились строки, а в другом ещё есть, выводим сообщение об этом
        if i >= len(lines_file1):
            print(f"Файл '{file1_path}' закончился, а в файле '{file2_path}' ещё есть строки:")
            print(lines_file2[i], end="")
        elif i >= len(lines_file2):
            print(f"Файл '{file2_path}' закончился, а в файле '{file1_path}' ещё есть строки:")
            print(lines_file1[i], end="")
        # Если строки в файлах не равны, выводим их
        elif lines_file1[i] != lines_file2[i]:
            print(f"Строка {i+1}:")
            print(f"В файле '{file1_path}': {lines_file1[i]}", end="")
            print(f"В файле '{file2_path}': {lines_file2[i]}", end="")
