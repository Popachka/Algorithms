from collections import defaultdict
keys = input().split()
main_dict = defaultdict(bool)

for key in keys:
    main_dict[key] = True

lines_str = list(map(str, input().split()))
ans = []
for str in lines_str:
    suffix_found = False
    for i in range(len(str)):
        suffix = str[:i+1]
        if suffix in main_dict:
            ans.append(suffix)
            suffix_found = True
            break
    if not suffix_found:
        ans.append(str)
print(*ans)