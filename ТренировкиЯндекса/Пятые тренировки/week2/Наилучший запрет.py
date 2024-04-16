import copy

n, m = map(int, input().split())

game = []
ans = []
for i in range(n):
    row = list(map(int, input().split()))
    game.append(row)

def print_game(game):
    for i in game:
        print('\t'.join(map(str, i)))

def find_max(arr):
    max_row_val = 0
    max_row_index = None
    max_row_col = None
    cnt = 0
    for row in arr:
        max_tmp = max(row)
        if max_tmp > max_row_val:
            max_row_val = max_tmp
            max_row_index = cnt
            max_row_col = row.index(max_tmp)
        cnt += 1
    return [max_row_val, max_row_index, max_row_col]

game_0 = copy.deepcopy(game)

# Первый Максимум
first_max = find_max(game)
# Исключаем строку с first_max
ans.append(first_max[1] + 1)
for i in range(m):
    game[first_max[1]][i] = -1
game_1 = copy.deepcopy(game)

# Второй максимум
second_max = find_max(game)
# Исключаем столбец с second_max
ans.append(second_max[2] + 1)
for i in range(n):
    game[i][second_max[2]] = -1
game_2 = copy.deepcopy(game)

# Третий максимум
third_max = find_max(game)
# Сравним если вычеркнуть первый макс как столбец
for i in range(n):
    game_0[i][first_max[2]] = -1
tmp_max = find_max(game_0)
for i in range(m):
    game_0[tmp_max[1]][i] = -1

third_max_vs_col_first_max = find_max(game_0)
if third_max[0] > third_max_vs_col_first_max[0]:
    ans[0] = tmp_max[1] + 1
    ans[1] = first_max[2] + 1 
print(*ans)
