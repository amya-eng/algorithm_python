# 编辑距离问题
# 时间复杂度： O(mn)
# 隶属于：动态规划问题
# dp[i][j]: 从s(1...i)变成t(1...j)的最短编辑距离
def min_edit_distense(str1, str2) -> int:
    l1 = len(str1)
    l2 = len(str2)
    dp = [[0 for i in range(l2 + 1)] for j in range(l1 + 1)]
    rec = [[0 for i in range(l2 + 1)] for j in range(l1 + 1)]
    for i in range(l1 + 1):
        dp[i][0] = i
        rec[i][0] = 'U'
    for j in range(l2 + 1):
        dp[0][j] = j
        rec[0][j] = 'L'
    for i in range(1, l1 + 1):
        for j in range(1, l2 + 1):
            c = 0
            if str1[i - 1] != str2[j - 1]:
                c = 1
            replace = dp[i - 1][j - 1] + c
            insert = dp[i][j - 1] + 1
            delete = dp[i - 1][j] + 1
            m = min(replace, insert, delete)
            if m == replace:
                dp[i][j] = replace
                rec[i][j] = 'LU'
            elif m == insert:
                dp[i][j] = insert
                rec[i][j] = 'L'
            else:
                dp[i][j] = delete
                rec[i][j] = 'U'
    print(dp[-1][-1])

    def print_seq(rec, i, j, s, t):
        if i == 0 and j == 0:
            return
        if rec[i][j] == 'LU':
            print_seq(rec, i - 1, j - 1, s, t)
            if s[i - 1] == t[j - 1]:                                  # 索引rec/dp时比索引字符串时多1
                print('无需操作')
            else:
                print('用t[%d](%c)替换s[%d](%c)' % (j, t[j - 1], i, s[i - 1]))
        elif rec[i][j] == 'L':
            print_seq(rec, i, j - 1, s, t)
            print('插入t[%d](%c)' % (j, t[j - 1]))
        else:
            print_seq(rec, i - 1, j, s, t)
            print('删除s[%d](%c)' % (i, s[i - 1]))

    print_seq(rec, l1, l2, str1, str2)


min_edit_distense("ABCBDAB", "BDCABA")
