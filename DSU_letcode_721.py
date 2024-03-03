class DSU:
    def __init__(self, N):
        self.root = [i for i in range(N)]
        self.depth = [1 for i in range(N)]

    def find(self, x):                                # 找root
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self.root[x])           # 路径压缩
        return self.root[x]

    def union(self, a, b):
        x = self.find(a)
        y = self.find(b)
        xh = self.depth[a]
        yh = self.depth[b]
        if x == y:
            return
        if xh >= yh:                                 # 按秩合并
            self.root[y] = x
            self.depth[x] = max(xh, yh + 1)
        else:
            self.root[x] = y

def is_upper(str1, str2):
    s1, s2 = len(str1), len(str2)
    for i in range(s1):
        if i > s2:                   # 如果str1 比str2 长
            return False
        if str1[i] < str2[i]:
            return True
        elif str1[i] > str2[i]:
            return False
        else:
            continue
    if s1 <= s2:                       # 如果str1 比str2 短 或两字符串完全相同
        return False

def accountsMerge(accounts):
    n = len(accounts)
    dsu = DSU(n)
    for i in range(n):
        for j in range(i + 1, n):
            flg = False
            if accounts[i][0] == accounts[j][0]:
                for item in accounts[i][1:]:
                    if item in accounts[j][1:]:
                        flg = True
            if flg:
                dsu.union(i, j)
    i = 0
    l = n
    des = 0
    while i < l:
        if i != dsu.root[i] - des:
            root = dsu.root[i] - des
            for item in accounts[i][1:]:
                if item not in accounts[root][1:]:
                    accounts[root].append(item)
            del accounts[i]
            del dsu.root[i]
            des += 1
            i -= 1
            l -= 1
        i += 1

    for item in accounts:
        s = len(item[1:])
        j = 1
        while j < s:
            k = j + 1
            while k < s + 1:
                if is_upper(item[k], item[j]):
                    item[j], item[k] = item[k], item[j]
                if item[j] == item[k]:
                    del item[k]
                    k -= 1
                    s -= 1
                k += 1
            j += 1
    return accounts

account = accountsMerge([["David","David0@m.co","David4@m.co","David3@m.co"],["David","David5@m.co","David5@m.co","David0@m.co"],["David","David1@m.co","David4@m.co","David0@m.co"],["David","David0@m.co","David1@m.co","David3@m.co"],["David","David4@m.co","David1@m.co","David3@m.co"]])
print(account)

