# 注意区分以下代码和浅拷贝的区别
s = [[0 for i in range(3)] for j in range(4)]
print(s)
s[1][0] = 3
print(s)

print()

# 浅拷贝
s1 = [[0] * 3] * 4
print(s1)
s1[1][0] = 3
print(s1)



