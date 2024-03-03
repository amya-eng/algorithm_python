# 最大子数组问题
# 时间复杂度： O(n)
# 隶属于动态规划问题

# D[i]: 以i开头的最大子数组和
# rec[i]: 记录以i开头的最大子数组结尾位置

def max_subarray(str1):
    len1 = len(str1)
    D = [i for i in range(len1)]
    rec = [i for i in range(len1)]
    D[len1 - 1] = str1[len1 - 1]
    rec[len1 - 1] = 12
    for i in range(len1 - 2, 0, -1):
        if D[i + 1] > 0:
            D[i] = D[i + 1] + str1[i]
            rec[i] = rec[i + 1]
        else:
            D[i] = str1[i]
            rec[i] = i
    index = 0
    for i in range(len1):
        if D[i] > D[index]:
            index = i
    print('最大子数组：str[%d...%d] = %d' % (index, rec[index], D[index]))

str1 = [1, -2, 4, 5, -2, 8, 3, -2, 6, 3, 7, -1]
max_subarray(str1)
