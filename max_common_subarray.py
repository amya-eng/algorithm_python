# 最长公共子串问题
# 隶属于： 动态规划
# 时间复杂度：O(mn)
#

def max_common_subarray(x, y):
    lx = len(x)
    ly = len(y)
    C = [[0 for i in range(ly + 1)] for j in range(lx + 1)]            # out of index 最可能出现的错误之一，还有一个是串上i-1,j-1
    l, p = 0, 0                         # l : 最长公共子串的长度， p: 最长公共子串的结尾
    for i in range(1, lx + 1):
        for j in range(1, ly + 1):
            if x[i - 1] == y[j - 1]:
                C[i][j] = C[i - 1][j - 1] + 1
            else:
                C[i][j] = 0
            if C[i][j] > l:
                l = C[i][j]
                p = i
    if l == 0:
        return None
    for k in range(p - l + 1, p + 1):
        print(x[k - 1], end=" ")

max_common_subarray('ABCADBB', 'BCEDBB')

