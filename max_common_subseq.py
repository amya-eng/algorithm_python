# 最长公共子序列问题
# 时间复杂度：O(mn)
# 隶属于 动态规划问题
# 存在最优子结构和重叠子问题
# C[i, j]表示x(1...i)与y(1...j)的最长公共子序列长度


def max_common_subseq(x, y):
    lx = len(x)
    ly = len(y)
    C = [[0 for i in range(ly + 1)] for j in range(lx + 1)]
    rec = [[0 for i in range(ly + 1)] for j in range(lx + 1)]
    for i in range(1, lx + 1):
        rec[i][0] = 'U'
    for j in range(1, ly + 1):
        rec[0][j] = 'L'
    for i in range(1, lx + 1):
        for j in range(1, ly + 1):
            if x[i - 1] != y[j - 1]:
                C[i][j] = max(C[i][j - 1], C[i - 1][j])
                if C[i][j] == C[i - 1][j]:
                    rec[i][j] = 'U'
                else:
                    rec[i][j] = 'L'
            else:
                C[i][j] = C[i - 1][j - 1] + 1
                rec[i][j] = 'LU'
    print(C[-1][-1])
    def print_seq(rec, s, t, i, j):
        if i == 0 and j == 0:
            return
        if rec[i][j] == 'LU':
            print_seq(rec, s, t, i - 1, j - 1)
            print(s[i - 1], end=" ")
        elif rec[i][j] == 'L':
            print_seq(rec, s, t, i, j - 1)
        else:
            print_seq(rec, s, t, i - 1, j)
    print_seq(rec, x, y, lx, ly)


max_common_subseq("ABCBDAB", "BDCABA")