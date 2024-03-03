# 01部分背包问题
# 完全背包问题不能使用贪心策略
# 时间复杂度 : O(nlogn)
# 隶属于： 贪心策略

def p_sort(item):
    return item[0] / item[1]
def partial_backage(lis, C):
    lis.sort(key=p_sort, reverse=True)
    i, ans = 0, 0
    l = len(lis)
    while C > 0 and i < l:
        if lis[i][1] <= C:
            ans += lis[i][0]
            C -= lis[i][1]
        else:
            ans += lis[i][0]/ lis[i][1] * C
            C = 0
        i += 1
    return ans

print(partial_backage([[60, 600], [10, 250], [36, 200], [16, 100], [45, 300]], 800))