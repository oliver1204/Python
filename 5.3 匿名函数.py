# 正常函数的
def square(x):
    return x*x
r1 = square(5)
print(r1)
# 匿名函数 lambda 表达式
# 这个就是匿名函数
lambda x: x*x

# filter(func, iterable) 过滤函数 Python

alist = [i for i in range(1, 101, 1)]
# r = filter(lambda x: x % 3 == 0, alist)
r = list(filter(lambda x: x % 3 == 0, alist))
print(r)

# lambda x: x % 3 == 0 就是匿名函数
