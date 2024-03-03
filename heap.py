# 大根堆
def shiftup(lis, index):
    if index == 1:
        return lis
    while index != 1:
        if lis[index] > lis[index // 2]:
            lis[index], lis[index // 2] = lis[index // 2], lis[index]
        index = index // 2
    return lis


def shiftdown(lis, index):
    if index * 2 > len(lis):
        return lis
    while index * 2 + 1 < len(lis):
        t = index * 2 if lis[index * 2] > lis[index * 2 + 1] else index * 2 + 1
        if lis[t] > lis[index]:
            lis[t], lis[index] = lis[index], lis[t]
        index = t
    return lis
def insert(lis, value):
    lis.append(value)
    l = len(lis) - 1
    return shiftup(lis, l)

def delete(lis, index):
    l = len(lis) - 1
    lis[l], lis[index] = lis[index], lis[l]
    del lis[l]
    shiftup(lis, index)
    shiftdown(lis, index)
    return lis

def top(lis):
    x = lis[1]
    delete(lis, 1)
    return x


def create(lis):
    lis1 = [0]                        # heap第一个元素是占位符
    for i in lis:
        lis1 = insert(lis1, i)
    return lis1[1:]

def transfor(lis):              # 将一个数组转化为大根堆
    lis = [0] + lis
    index = (len(lis) - 1) // 2           # 全部转化为index表示方法
    while index != 0:
        lis = shiftdown(lis, index)
        index -= 1
    return lis[1:]

def heap_sort(array):
    array = transfor(array)
    array = [0] + array
    for j in range(len(array) - 1, 1, -1):
        array[1], array[j] = array[j], array[1]
        array[:j] = shiftdown(array[:j], 1)          # 前半段未排序，调整成堆
    return array[1:]

lis = [0, 8, 7, 6, 5, 4, 3, 2, 10]
lis = shiftup(lis, 8)            # 将下标为8的元素上推
print(lis)
lis = [0, 10, 9, 2, 7, 6, 5, 4, 3, 2, 1]
lis = shiftdown(lis, 3)              # 将下标为3的元素下滤
print(lis)
lis = insert(lis, 20)                # 末端插入一个元素，并维护堆
print(lis)
lis = delete(lis, 5)                 # 删除下标为5的元素并维护堆
print(lis)
print(top(lis))
print(lis)
lis = [3,4,5,6,1,7,8]
lis1 = create(lis)                        # 通过插入空堆来建堆
print(lis1)
lis = [3,4,5,6,1,7,8]                        # 通过调整数组来建堆
lis2 = transfor(lis)
print(lis2)
array = [3,5,2,5,4,2,1,9,7,4,9]
array = heap_sort(array)
print(array)

