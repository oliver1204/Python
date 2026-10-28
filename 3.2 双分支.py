# 实现奇偶数的判断
n = int(input('请输入一个整型数值: '))
# 判断
if n % 2 == 0:
# 偶数
    print(f'{n}是一个偶数.')
else:
# 奇数
    print(f'{n}是一个奇数5.')

#简化

# 获取两个整型数值的较大值
n1, n2 = eval(input('请输入两个整型数值: '))
# 判断, 条件成立返3回左边的值
bigger = n1 if n1 > n2 else n2
print(f'{bigger = }')