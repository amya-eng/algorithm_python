class dsu:
    def __init__(self, N):
        self.root = [i for i in range(N)]
        self.depth = [1 for i in range(N)]
    def find(self, k):
        if k == self.root[k]:
            return k
        self.root[k] = self.find(self.root[k])
        return self.root[k]

    def union(self, a, b):
        x = self.find(a)
        y = self.find(b)
        xh = self.depth[a]
        yh = self.depth[b]
        if x == y:
            return
        if xh <= yh:
            self.root[x] = y
            self.depth[y] = max(xh + 1, yh)
        else:
            self.root[y] = x


def findCircleNum(isConnected) -> int:
    n = len(isConnected)
    dsu1 = dsu(n)
    for i in range(n):                  # 遍历二维数组的方式
        for j in range(n):
            if isConnected[i][j] == 1:
                dsu1.union(i, j)
    r = 0
    for k in range(n):
        if k == dsu1.root[k]:
            r += 1
    return r

r = findCircleNum([[1,1,0],[1,1,0],[0,0,1]])
print(r)

