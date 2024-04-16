from collections import defaultdict, Counter
def intersect(nums1, nums2):
    arr1 = Counter(nums1)
    arr2 = Counter(nums2)
    n1 = len(nums1)
    n2 = len(nums2)
    ans = []
    if n1 < n2:
        for key,cnt in arr1.items():
            if key in arr2:
                count_append = min(cnt, arr2[key])
                ans += [key] * count_append
    else:
        for key, cnt in arr2.items():
            if key in arr1:
                count_append = min(cnt, arr1[key])
                ans += [key] * count_append
    return ans
nums1 = [1,2,2,1]
nums2 = [2,2,3]

print(intersect(nums1,nums2))