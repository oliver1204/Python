# 二进制
# 复制的快捷键: ctrl + d (duplicate 复制)
print(2 ** 0) # 1
print(2 ** 1)
print(2 ** 2)
print(2 ** 3)
print(2 ** 4)
print(2 ** 5)
print(2 ** 6)
print(2 ** 7)
print('-' * 20)
print(10 ** 0)
print(10 ** 1)
print(10 ** 2)

print('=' * 50)


# 思考 : 普通人如何学习复利思维?
# 点 -> 线 -> 面 -> 体 -> 灵活使用
# 1. 一年中每一天都进步 0.1% (千分之一), 请问一年之后, 你进步了多少?
day_up = 1.001 ** 365
print(f'{day_up:.2f}')
# 2. 一年中每一天都退步 0.1% (千分之一), 请问一年之后, 你还剩余多少?
day_down = 0.999 ** 365
print(f'{day_down:.2f}')