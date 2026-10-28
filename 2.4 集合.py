# 集合 set() / {e1, e2, e3 ...}
aset = {11, 22, 33, 44, 55, 44, 33, 22, 11}
print(aset)

a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}

# 交集 &
# r1 = a & b 符号法
r1 = a.intersection(b) # 函数名法
print('交集 & ===', r1)
# 并集
# r2 = a | b
r2 = a.union(b)
print('并集 | ===', r2)
# 差集
r3 = a - b
r4 = b - a
print('差集 a - b ===',r3)
print('差集 b - a ===',r4)
# 对称差集
r5 = a.symmetric_difference(b)
print('对称差集 symmetric_difference===',r5)

