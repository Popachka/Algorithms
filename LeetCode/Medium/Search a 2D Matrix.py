class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if matrix[i][-1] < target:
                continue
            else:
                lo, hi = 0, len(matrix[i]) - 1
                while lo <= hi:
                    mid = (lo + hi) // 2
                    if matrix[i][mid] == target:
                        return True
                    elif matrix[i][mid] > target:
                        hi = mid - 1
                    else:
                        lo = mid + 1
        return False
