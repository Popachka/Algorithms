import json

name_json = input()
# Чтение файла ввода
with open(f'C:\MyFiles\PyCode\Alg\ШАР\{name_json}', 'r', encoding='utf-8') as f:
    input_data = json.load(f)


def crit_10(string: str):
    """_summary_

    Args:
        string (str): _description_

    Returns:
        _type_: _description_
    """
    vowels = set('aeiou')
    not_uniq = set()
    count = 0
    for char in string:
        char = char.lower()
        if char in vowels and char not in not_uniq:
            count += 1
            not_uniq.add(char)
    return count


def select_crit(strings: list, crit: str):
    """_summary_

    Args:
        strings (list): _description_
        crit (str): _description_

    Returns:
        _type_: _description_
    """
    select_part = []
    if crit == '10':
        for part in strings:
            if crit_10(part) >= 2:
                select_part.append(part)
    elif crit == '20':
        for part in strings:
            if len(part) % 2 == 0:
                select_part.append(part)
    else:
        select_part.extend(strings)
    return select_part


output_data = {}
for key, criteriy in input_data.items():
    parts = input().strip().split('_')
    select_parts = select_crit(parts, criteriy)
    select_parts.sort(reverse=True)  # Сортировка в обратном алфавитном порядке
    output_data[key] = select_parts
# Вывод нового json
with open('output.json', 'w', encoding='utf-8') as f:
    json.dump(output_data, f, ensure_ascii=False, indent=4)

