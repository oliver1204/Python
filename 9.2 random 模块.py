import random
# 执行范围的随机整数
r1 = random.randint(1, 10)
print(f'{r1 = }')
# 0.0 ~ 1.0 浮点值
print(random.random())
print(random.choice(['a', 'b', 'c']))
print(random.sample(['a', 'b', 'c'], 2))
alist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
random.shuffle(alist) # 洗牌, 随机置换
print(alist)