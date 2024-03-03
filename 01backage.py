def knapsackSR(lis, i, j, v) -> int:                 # 背包容量限制
    if v < 0:
        return float("-inf")
    if i > j:
        return 0
    return max(knapsackSR(lis, i + 1, j, v), knapsackSR(lis, i + 1, j , v - lis[i - 1][1]) + lis[i - 1][0])

lis = [[9, 4], [10, 5], [9, 4], [2, 3], [24, 10]]             # [p, v]
pmax = knapsackSR(lis, 1, 5, 13)
print(pmax)