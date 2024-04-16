from collections import defaultdict
str1 = str(input())
str2 = str(input())

def is_anagramma(str1, str2):

    if len(str1) != len(str2):
        print('NO')
        return

    count_str1 = defaultdict(int)
    count_str2 = defaultdict(int)
    
    for char in str1:
        count_str1[char] += 1
    for char in str2:
        count_str2[char] +=  1

    if count_str1 == count_str2:
        print('YES')
    else:
        print('NO')

is_anagramma(str1, str2)