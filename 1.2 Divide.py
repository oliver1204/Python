# 余数 (%) 和整除(//)
# 使用 divmod() 函数一次获得商和余数

# 商 (没有小数点)
quotient1 = 10 / 3 # / 浮点除
quotient2 = 10 // 3 # // 整除
print(f'{quotient1 = }, {quotient2 = }')

# 余数
remaining = 10 % 3
print(f'{remaining = }')

# 内置函数 divmod(x, y)
# 逗号表达式
q, r = divmod(10, 3) # 商, 余数
print(f'{q = }, {r = }')