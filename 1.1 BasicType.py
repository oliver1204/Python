# id() 内置函数查看地址

# 数据类型 变量名 = 变量值
# Python 语⾔的变量类型是⾃动推导, 类似 js 中的 var, const, let

# 1. 整型常量特点
num1 = 10
num2 = 10

# %s 字符串 %d 整型 %f 浮点型 字符串.format()
# f-string
print(f'{id(num1)}, {id(num2)}')
# 思考 : 以上两个变量是⼀样的吗? 
# 答：都是4366576208, 4366576208，所以是一样的

# 为了更清楚的知道ID所对应的值，采用下面的写法
print(f'id(num1) = {id(num1)}, id(num2) = {id(num2)}')
# id(num1) = 4309330512, id(num2) = 4309330512

# 上面的写法可以简化为：
print(f'{id(num1) = }, {id(num2) = }')

print(f'{type(num1) = }, {type(num2) = }')

print('=' * 50) # 字符串相乘就是重复的含义

# 2. 浮点型常量特点
n1 = 10.5
n2 = 10.5
print(f'{type(n1) = }, {type(n2) = }')
print(f'{id(n1) = }, {id(n2) = }')
print('=' * 50)

# 3. 字符串常量的特点
s1 = 'hello world' # Python 语⾔的字符串都是⼀样的. 没有所谓 `字符类型` char, 所以单引号和双引号都是可以的。
s2 = "hello world"
print(f'{type(s1) = }, {type(s2) = }')
print(f'{id(s1) = }, {id(s2) = }')