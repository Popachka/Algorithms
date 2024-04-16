N = int(input())
seg_n = []
for i in range(N):
    test_size = int(input())
    arr = list(map(int, input().split()))
    
    cur_size = 1
    segment_len = []
    min = 10**9
    for num in arr:
        if min > num:
            min = num
        if min < cur_size:
            cur_size -= 1
            segment_len.append(cur_size)
            cur_size = 1
        if num <= cur_size or min == cur_size:
            segment_len.append(cur_size)
            cur_size = 1
            min = 10**9
            continue
        cur_size += 1
    if cur_size > 1:
        segment_len.append(cur_size - 1)
    seg_n.append(segment_len)
for arr in seg_n:
    print(len(arr))
    print(*arr)

