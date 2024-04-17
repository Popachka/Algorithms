import math


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        def condition(speed) -> bool:
            return sum((pile - 1) / speed + 1 for pile in piles) <= h
        lo, hi = 1, max(piles)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if condition(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo


# Ввод данных для контеста
h = int(input())  # Ввод значения переменной h
piles = list(map(int, input().split()))  # Ввод значений элементов списка piles

# Создание объекта класса Solution
solution = Solution()

# Запуск метода minEatingSpeed и вывод результата
print(solution.minEatingSpeed(piles, h))
