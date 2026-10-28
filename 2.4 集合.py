# 集合 set() / {e1, e2, e3 ...}
aset = {11, 22, 33, 44, 55, 44, 33, 22, 11}
print(aset)

a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}

# 交集 & intersection
# r1 = a & b 符号法
r1 = a.intersection(b) # 函数名法
print('交集 & ===', r1)
# 并集 | union
# r2 = a | b
r2 = a.union(b)  # 函数名法
print('并集 | ===', r2)
# 差集 - difference
r3 = a - b
r4 = b - a
print('差集 a - b ===',r3)
print('差集 b - a ===',r4)
# 对称差集 ^ symmetric_difference
r5 = a^b
# r5 = a.symmetric_difference(b)
print('对称差集 symmetric_difference===',r5)

# 等于 == 与不等于 !=
#元素属于集合, Python 的关键词 in 可以测试元素是否属于集合
#元素不属于集合, Python的关键词 not in 可以测试元素是否不属于集合

