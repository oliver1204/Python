# for 循环 : 执行指定次数的循环
# 需求 : 我爱北京天安门
# range() 必须要指定 stop 参数数值
# range(start, stop, step), 如果只有一个参数，则参数代表 stop
for _ in range(10): # [0~9] 序列中的下标
    print('我爱北京天安门')
# 循环使用场景 : 序列
alist = [11, 22, 33, 44, 55]
for i in alist:
    print(i)
# 字符串序列
str = 'hello world!'
for i in str:
    print(i)

print('=' * 50)

# 需求 1 : 生成 10 个 0 的列表对象
alist = [0] * 10
print(alist)

# 需求 2 : 生成 1~10 之间的所有偶数序列
for i in range(2, 11, 2):
    print(i)
blist = [i for i in range(2, 11, 2)]
print(blist)

# 需求 3 : 列出 20 之内的所有勾股数 [3, 4, 5] [5, 12, 13] ...
# 勾股定义 : a² + b² = c²
# for a in range(1, 20, 1):
#   for b in range(a, 20, 1):
#     for c in range(b, 20, 1):
# # 判断
#       if a ** 2 + b ** 2 == c ** 2:
#           print(a, b, c)

clist = [(a, b ,c) for a in range(1, 20, 1) for b in range(a, 20, 1)  for c in range(b, 20, 1) if a ** 2 + b ** 2 == c ** 2]
print(clist)