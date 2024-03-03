# 不相交集的实现
# Disjoint Set Union

class DSU:
    def __init__(self, N):
        self.root = [i for i in range(N)]
        self.depth = [1 for i in range(N)]

    def find(self, x):                                # 找root
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self, self.root[x])           # 路径压缩
        return self.root[x]

    def union(self, a, b):
        x = self.find(a)
        y = self.find(b)
        xh = self.depth(a)
        yh = self.depth(b)
        if x == y:
            return
        if xh >= yh:                                 # 按秩合并
            self.root[y] = x
            self.depth[x] = max(xh, yh + 1)
        else:
            self.root[x] = y




