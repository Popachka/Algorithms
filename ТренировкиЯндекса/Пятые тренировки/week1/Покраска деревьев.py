P, V = list(map(int,input().split()))
Q, M = list(map(int,input().split()))

Vasya_range_min, Vasya_range_max = P - V, P + V 
Mar_range_min, Mar_range_max = Q-M, Q+M
Vasya_count = Vasya_range_max - Vasya_range_min + 1
Mar_count = Mar_range_max - Mar_range_min + 1 
print(Vasya_count, Mar_count)
overlap_min = max(Vasya_range_min, Mar_range_min) 
overlap_max = min(Vasya_range_max, Mar_range_max) 
print(overlap_min, overlap_max)
overlap_count = max(0, overlap_max - overlap_min + 1)
print(overlap_count)
total_count = Vasya_count + Mar_count - overlap_count 
print(total_count)