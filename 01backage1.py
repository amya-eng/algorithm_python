# 带备忘录不递归
def knapsackSR(lis, c) -> int:
    n = len(lis)
    dp = [[0 for i in range(c + 1)] for j in range(n + 1)]
    rec = [[0 for i in range(c + 1)] for j in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, c + 1):
            if lis[i - 1][1] <= j:
                s = lis[i - 1][0] + dp[i - 1][j - lis[i - 1][1]]
                if s > dp[i - 1][j]:
                    rec[i][j] = 1
                    dp[i][j] = s
                else:
                    rec[i][j] = 0
                    dp[i][j] = dp[i - 1][j]
    print('max_price:')                # 打印最大价值
    print(dp[-1][-1])

    for i in range(len(lis)):                                      # 打印商品列表
        print('%d: [%d %d]' % (i + 1, lis[i][0], lis[i][1]), end=" ")

    print('selected:')                                                     # 以下打印选中的商品标号
    i = n
    j = c
    while i:
        if rec[i][j] == 1:
            print(i, end=" ")
            j -= lis[i - 1][1]
        i -= 1


lis = [[24, 10], [2, 3], [9, 4], [10, 5], [9, 4]]              # [p, v]
knapsackSR(lis, 13)
