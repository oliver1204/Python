- [与AI相关的Python](#与ai相关的python)
  - [基本类型与基本运算](#基本类型与基本运算)
    - [1.1 认识变量类型和变量地址](#11-认识变量类型和变量地址)
      - [输出结果](#输出结果)
    - [1.2 余数 (%) 和整除(//)](#12-余数--和整除)
      - [输出结果](#输出结果-1)
    - [1.3 乘⽅(\*\*)](#13-乘)
      - [输出结果](#输出结果-2)
      - [思考 : 普通人如何学习复利思维?](#思考--普通人如何学习复利思维)
      - [输出结果](#输出结果-3)
    - [1.4 位运算操作](#14-位运算操作)
      - [输出结果](#输出结果-4)
      - [其他换位方法](#其他换位方法)
      - [输出结果](#输出结果-5)
    - [1.5 整数与浮点数的特性](#15-整数与浮点数的特性)
      - [在其他语言中](#在其他语言中)
      - [python 中的数没有限制](#python-中的数没有限制)
    - [1.6 字符串](#16-字符串)
      - [输出结果](#输出结果-6)
    - [1.7 输⼊与输出](#17-输与输出)
  - [2. 容器类型与对应操作⾏为](#2-容器类型与对应操作为)
    - [2.1 列表](#21-列表)
      - [输出结果](#输出结果-7)
      - [列表切片](#列表切片)
      - [输出结果](#输出结果-8)
      - [列表.sort() 与 sorted() 区别](#列表sort-与-sorted-区别)
      - [输出结果](#输出结果-9)
    - [2.2 元组类型](#22-元组类型)
      - [元组的功能 -- tuple类型不允许修改](#元组的功能----tuple类型不允许修改)
      - [输出结果](#输出结果-10)
    - [2.3 字典类型](#23-字典类型)
      - [输出结果](#输出结果-11)
      - [输出结果](#输出结果-12)
    - [2.4 集合](#24-集合)
      - [输出结果](#输出结果-13)
  - [3. 分⽀结构](#3-分结构)
    - [3.1 单分⽀](#31-单分)
      - [输出结果](#输出结果-14)
    - [3.2 双分⽀](#32-双分)
      - [简化](#简化)
      - [输出结果](#输出结果-15)
    - [3.3 多分⽀](#33-多分)
    - [3.4 match匹配语句](#34-match匹配语句)
    - [4.1  for循环](#41--for循环)
      - [range ()函数](#range-函数)
      - [输出结果](#输出结果-16)
      - [输出结果](#输出结果-17)
      - [输出结果](#输出结果-18)
      - [输出结果](#输出结果-19)
    - [4.2 while循环](#42-while循环)
      - [认识哨兵值](#认识哨兵值)
      - [输出结果](#输出结果-20)
      - [哨兵值](#哨兵值)
      - [输出结果](#输出结果-21)
  - [5. 函数定义](#5-函数定义)
      - [输出结果](#输出结果-22)
      - [输出结果](#输出结果-23)
      - [输出结果](#输出结果-24)
      - [输出结果](#输出结果-25)
      - [输出结果](#输出结果-26)
  - [6. ⾯向对象](#6-向对象)
      - [抽象类的介绍](#抽象类的介绍)
      - [多态练习](#多态练习)
      - [输出结果](#输出结果-27)
  - [7. ⽂件操作](#7-件操作)
      - [文本文件路径](#文本文件路径)
      - [非文件文件复制](#非文件文件复制)
      - [登录日志综合案例](#登录日志综合案例)
  - [8. 异常处理](#8-异常处理)
    - [8.1 ⼀个除数为 0 的错误](#81-个除数为-0-的错误)
      - [输出结果](#输出结果-28)
    - [8.2 撰写异常处理程序 try - except - else - finally](#82-撰写异常处理程序-try---except---else---finally)
      - [输出结果](#输出结果-29)
    - [8.3 ⾃定义异常与丢出异常](#83-定义异常与丢出异常)
      - [输出结果](#输出结果-30)
  - [9. 模块化编程](#9-模块化编程)
    - [9.1 math 模块](#91-math-模块)
      - [输出结果](#输出结果-31)
    - [9.2 random 模块](#92-random-模块)
      - [输出结果](#输出结果-32)
    - [9.3 ⽇期时间模块](#93-期时间模块)
      - [输出结果](#输出结果-33)
    - [9.4 ⾃定义模块](#94-定义模块)
      - [输出结果](#输出结果-34)
      - [输出结果](#输出结果-35)
    - [9.5 第三⽅模块](#95-第三模块)
    - [9.5.1 ⽹络爬⾍](#951-络爬)
    - [9.5.2 ⾃动化](#952-动化)
    - [9.5.3 数据分析及可视化](#953-数据分析及可视化)
    - [9.5.4 WEB开发](#954-web开发)
    - [9.5.5 机器学习](#955-机器学习)
    - [9.5.6 其他常⽤](#956-其他常)

# 与AI相关的Python
## 基本类型与基本运算
### 1.1 认识变量类型和变量地址
* Python可以使⽤ id() 函数获得变量的地址
* 相同内容的变量会有相同的地址

```python
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
```
#### 输出结果

```python
295961168, 4295961168
id(num1) = 4295961168, id(num2) = 4295961168
id(num1) = 4295961168, id(num2) = 4295961168
type(num1) = <class 'int'>, type(num2) = <class 'int'>
==================================================
type(n1) = <class 'float'>, type(n2) = <class 'float'>
id(n1) = 4296922096, id(n2) = 4296922096
==================================================
type(s1) = <class 'str'>, type(s2) = <class 'str'>
id(s1) = 4297363696, id(s2) = 4297363696
```

### 1.2 余数 (%) 和整除(//)
使用 divmod() 函数一次获得商和余数
divmod(x, y) 商余函数，同时输出商和余数，
divmod(10, 3) = (3, 1)

```python
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
```

#### 输出结果

```python
quotient1 = 3.3333333333333335, quotient2 = 3
remaining = 1
q = 3, r = 1
```
### 1.3 乘⽅(**)
```python
# 二进制
# 复制 ctrl + d (duplicate 复制)

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
```

#### 输出结果
```python
1 2 4 8 16 32 64 128
--------------------
1  10  100
```
#### 思考 : 普通人如何学习复利思维?
```python
# 点 -> 线 -> 面 -> 体 -> 灵活使用
# 1. 一年中每一天都进步 0.1% (千分之一), 请问一年之后, 你进步了多少?
day_up = 1.001 ** 365
day_up = 1.001 ** 730 # 第二年
print(f'{day_up:.2f}')
# 2. 一年中每一天都退步 0.1% (千分之一), 请问一年之后, 你还剩余多少?

day_down = 0.999 ** 365
print(f'{day_down:.2f}')
```
#### 输出结果
```python
1.44
.07
0.69
```

### 1.4 位运算操作

```python
# 需求 : 交换 x, y 的值
x = 10
y = 20

# 方式一 : 临时变量
# temp = x
# x = y
# y = temp

# 方式二 : + - - (自增运算符 ++ 自减运算符 --)
# js有，前自增 ++1 以及后自增++。 但是python没有，只有一种自增方式
# x = x + y # x = 30
# y = x - y # y = 10
# x = x - y # x = 20

# 方式三 : Python 语言特有的交换语法, 其它语言没有该语法
# x, y = y, x

# 方式四 : Python的交换语法，在底层是位运算 - 异或操作 
# (异或操作的口诀: 相同为0, 不同为1)
x = x ^ y
y = x ^ y
x = x ^ y
print(f'{x = }, {y = }')

# 具体实现思路如下：
# 在python 中 三个单引号是多行注释
''' 一个字节表示数据
十进制   二进制
10      0000 1010
20      0001 0100
'''
#  x = x ^ y  异或操作结果是 30 
''' 一个字节表示数据
10    0000 1010
20    0001 0100
-----------------
      0001  1110 x=30
'''
#  y = x ^ y 异或操作结果是 10
''' 一个字节表示数据
30    0001 1110
20    0001 0100
-----------------
      0000  1010 y=10
'''
# x = x ^ y 异或操作结果是 20
''' 一个字节表示数据
30   0001  1110
10   0000  1010
-----------------
     0001  0100  x=20

'''
```

#### 输出结果

```python
x = 20, y = 10

```
#### 其他换位方法

```python

# << 左移: 每移动一位, 相当于 * 2
n = 10
n = n << 1 # 相当于 10 * 2 = 20
print(f'{n = }')

# >> 右移: 每移动一位, 相当于 // 2
m = 10
m = m >> 1 # 相当于 10 // 2 = 20
print(f'{m = }')

# & 按位与: 全 1 为 1
a = 10
b = 7
'''
10 0000 1010
7  0000 0111
-----------------
   0000 0010 结果为: 2
'''
c = a & b
print(f'{c = }')
# | 按位或 : 有 1 就 1
'''
10 0000 1010
7  0000 0111
-----------------
   0000 1111 结果为: 15
'''
d = a | b
print(f'{d = }')

```
#### 输出结果

```python
n = 20
m = 5
c = 2
d = 15
```


### 1.5 整数与浮点数的特性

#### 在其他语言中
int 整型, 占用 4 个字节空间, 总有 4 * 8 = 32 个比特位. 31个比特位可以存储数据. 正数： 2147483648（2^31） 负值： -2147483647

unsigned int, unsigned long 无符号类型, 只能存储正数, 不能存储负数. 4294967296（2^32）, 18446744073709551616

long 长整型, 占用 8 个字节空间, 最大值为 9223372036854775808
float 单精度浮点型 4个字节, double 双精度浮点型 8 个字节

#### python 中的数没有限制
整数的英文是 integer, 在计算机程序语言中一般用 int 表示. 整数大小必须在某一区间, 否则会有溢位(overflow), 造成数据不正确. Python3已经将整数存储空间的大小限制拿掉了, 所有没有 long 了, 也就是说 int 可以是任意大小的数值.

浮点数的英文是 float, 既然整数大小没有限制, 浮点数大小当然也没有限制.



### 1.6 字符串
python 的字符串有三类
  1. 单引号 ' '
  2. 双引号 " "
  3. 三引号 '''  ''' """  """，多用于多行注释的时候使用

```python

s = '''
介绍信
尊敬的xxx, 我向您
推荐该学员...
...
...
非常优秀!!
此致/敬礼
'''
print(s)
```

当给三引号赋予变量后就变成了字符串，否则就是注释。

```python
# raw string 原生字符串 (取消所有转义)
# 文件路径
# filepath = 'D:\TuLing\2421\视频\专为AI设计的Python课程' 这种写法在\T的时候就出错了
filepath = 'D:\\TuLing\\2421\\视频\\专为AI设计的Python课程' 
  
filename = r'D:\TuLing\2421\视频\专为AI设计的Python课程'

print(f'{filepath = }')
print(f'{filename = }')

print('===' * 20)

# binary string
# 二进制数据
s = 'hello world' 
print('===s', s, type(s))
b = b'hello world' # 相当于将字符串类型数据转换为了字节数据
print('===b', b, type(b))
```
#### 输出结果

```python
===s hello world <class 'str'>
===b b'hello world' <class 'bytes'>

```
   
### 1.7 输⼊与输出
input()函数与print()函数功能相反, 这个函数会从屏幕读取用户从键盘输入的数据. 特别注意所有输入的数据不论是字符串或是数值数据返回到value时一律是字符串数据, 如果要执行数学运算需要用int()函数转换为整数.

eval() 函数 : evaluate
eval(<字符串>)函数是Python语言中一个十分重要的函数，它能够以Python表达式的方式解析并执行字符串，将返回结果输出.

`思考:` 输入多个数字, 为什么只能用逗号分隔? 为什么使用空格分隔会报错呢?

```python

# 其他语言的hello world 

# public static void main() {
#    system.out.print("hello world")
#}
#'''
# Python 语言的hello world 
print('hello world')

# input() 函数是一个阻塞函数, 回车才代表输入的结束
msg = input('请输入你的内容: ')
print(f'{msg = }, {type(msg) = }')

# 需求 : 让用户输入两个整型数值, 实现数学上的加法运算
n1, n2 = eval(input('请输入两个整型数值: ')) # 10, 20
result = n1 + n2
print(f'{result = }')

```

## 2. 容器类型与对应操作⾏为
### 2.1 列表
```python
# 定义一个列表对象
# 方式一：
# alist = []
# 方式二： 
alist = list()
print(f'{alist = }, {type(alist) = }')

# CRUD 增删改查
alist.append(1)
alist.append(2)
alist.append(3)
print(alist)
alist.insert(0, 9)
print(alist)
element = alist.pop() # 弹出
print(alist, element)
# 指定下标弹出元素
element = alist.pop(0)
print(alist, element)
# 指定元素删除
alist.remove(2)
print(alist)
# 修改
alist[0] = 666
print(alist)
```
#### 输出结果

```python
alist = [], type(alist) = <class 'list'>
===在后面添加 [1, 2, 3]
===在指定位置添加 [9, 1, 2, 3]
===将末尾删除，并返回 [9, 1, 2] 3
===删除指定的index，并返回 [1, 2] 9
===指定元素删除某个元素 [1]
===修改 [666]
```

#### 列表切片
```python
# [start : stop : step] 下标 : start=0, stop=10 (不包含) step = 1
alist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# blist = alist[0:5:1]
blist = alist[:5:]
print(blist)
str = 'hello world'
substr = str[0:5:1]
print(substr)
```

#### 输出结果

```python
[1, 2, 3, 4, 5]
hello
```

#### 列表.sort() 与 sorted() 区别

```python
# 存取有序
alist = list([5, 7, 3, 2, 8, 9, 1, 4, 6])
print(alist)
# 元素有序 (升序)
alist.sort()
print('=== sort', alist)
alist.reverse() # 降序
print('=== reverse',alist)
print('-' * 20)
blist = list([5, 7, 3, 2, 8, 9, 1, 4, 6])
blist.sort(reverse=True)
print('===blist.sort(reverse=True) ',blist)
print('-' * 20)
# 内置函数 sorted() 不是在原列表上进行排序的, 而是复制了一个新排列再实现排序. 所以操作完毕后一定要接收返回的结果
clist = list([5, 7, 3, 2, 8, 9, 1, 4, 6])
dlist = sorted(clist, reverse=True)
print(clist, id(clist))
print('====sorted(clist, reverse=True)', dlist, id(dlist))
```

#### 输出结果

```python
=== sort [1, 2, 3, 4, 5, 6, 7, 8, 9]
=== reverse [9, 8, 7, 6, 5, 4, 3, 2, 1]
--------------------
===blist.sort(reverse=True)  [9, 8, 7, 6, 5, 4, 3, 2, 1]
--------------------
[5, 7, 3, 2, 8, 9, 1, 4, 6] 4346788288
====sorted(clist, reverse=True) [9, 8, 7, 6, 5, 4, 3, 2, 1] 4346788928
```
dlist 和 clist 地址是不一样的，所以内置的sort 方法是复制了一个全新的数组。

而数组本身的sort方法，[].sort 是对数组本身操作的，id 是同一个。


### 2.2 元组类型

#### 元组的功能 -- tuple类型不允许修改
1. 可以更安全地保 护数据
   程序设计中有些数据可能永远不会改变, 将它存储在元组(tuple)内, 可以安全地保护, 例如: 图像处理时对象的长,宽或每一像素的色彩数据, 很多是元组数据类型.
2. 加快程序执行速度元组 (tuple) 结构比列表 (list) 简单, 占用较少的系统资源, 程序执行时速度比较快.了解了上述元组的优点后, 未来设计程序时, 如果确定数据可以不更改, 就尽量使用元组数据类型
```python
# 定义一个元组类型
# tuple 元素不可变
tuple1 = (1, 2, 3, 4, 5)
print(tuple1, type(tuple1))
# tuple1[0] = 6
# print(tuple1, type(tuple1))
# 细节 (元组中仅有单个元素, 需要在元素之后添加逗号, 不能省略)
tuple2 = (1 )
print(tuple2, type(tuple2))
```
#### 输出结果

```python
(1, 2, 3, 4, 5) <class 'tuple'>
1 <class 'int'>
(1,) <class 'tuple'>
```
!!! 细节 (元组中仅有单个元素, 需要在元素之后添加逗号, 不能省略)

### 2.3 字典类型
python 中也有内置的map函数，但是它不同于java 或 js的含义，
```python
nums_str = ["1", "2", "3", "4"]
nums_int = list(map(int, nums_str))
print(nums_int)
```
#### 输出结果

```python
[1, 2, 3, 4]
```

```python
#字典类型 : key-value 键值对, 通过 key 实现操作, key 要保证唯一性
# Python : dict() {key: value}

adict = {'张三': 100,'李四': 98,'王五': 88,'赵六': 60}
print(adict)
adict['张三'] = 90
print(adict)
score = adict['张三']
print(f'{score = }')
# keys 键集, values 值集, items 键值对集合
print(adict.keys())
print(adict.values())
```

Python 中的字典顺序是按照定义时的顺序存储的。
#### 输出结果

```python
adict = {'张三': 100,'李四': 98,'王五': 88,'赵六': 60}
{'张三': 90,'李四': 98,'王五': 88,'赵六': 60}
score = 90
dict_keys(['张三', '李四', '王五', '赵六'])
dict_values([90, 98, 88, 60])
```
大型程序设计中, 字典用久了会产生相当多的元素, 也许是几千个或几十万个或更多.
### 2.4 集合

| 说明     | Python 符号  | 函数名                 |
| -------- | ------------ | ---------------------- |
| 交集     | `a & b`      | `intersection`         |
| 并集     | `a \| b`     | `union`                |
| 差集     | `a - b`      | `difference`           |
| 对称差集 | `a ^ b`      | `symmetric_difference` |
| 等于     | `a == b`     | —                      |
| 不等于   | `a != b`     | —                      |
| 是成员   | `a in b`     | —                      |
| 不是成员 | `a not in b` | —                      |

```python
# 集合 set() / {e1, e2, e3 ...}
aset = {11, 22, 33, 44, 55, 44, 33, 22, 11}
print(aset)
```
#### 输出结果

```python
{33, 22, 55, 11, 44}
```

```python
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

```


## 3. 分⽀结构
### 3.1 单分⽀
课堂案例 : 小明的语文, 数学, 英语成绩, 判断三门功课是否全部及格.
```python
# 接收三科成绩
chinese, math, english = eval(input('请输入小明的语文,数学,英语成绩: '))
# 判断
if chinese >= 60 and math >= 60 and english >= 60:
    print('全部及格!')
print('程序继续向下执行...')
```
#### 输出结果

```python
程序继续向下执行...
```
### 3.2 双分⽀
```python
# 实现奇偶数的判断
n = int(input('请输入一个整型数值: '))
# 判断
if n % 2 == 0:
# 偶数
    print(f'{n}是一个偶数.')
else:
# 奇数
    print(f'{n}是一个奇数5.')
```
#### 简化
```python
# 获取两个整型数值的较大值
n1, n2 = eval(input('请输入两个整型数值: '))
# 判断, 条件成立返回左边的值
bigger = n1 if n1 > n2 else n2
print(f'{bigger = }'
```
#### 输出结果

```python
请输入一个整型数值: 12
12是一个偶数.
请输入两个整型数值: 3, 7
bigger = 7
```
### 3.3 多分⽀
练习 1 : 请输入数字分数, 系统将响应A, B, C, D 或 F 等级.
```python
 请输入数字分数,系统将响应A, B, C, D 或 F 等级.
score = eval(input("Enter score: "))
# 多分支判断
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

```
### 3.4 match匹配语句
```python
score = eval(input("Enter score: "))
level = score // 10 # 算出来的是十位数, // 是除法，不是注释
match level:
    case 10 | 9:
        print("A")
    case 8:
        print("B")
    case 7:
        print("C")
    case 6:
        print("D")
    case _:  # 兜底条件
        print("F")
```

### 4.1  for循环
可迭代对象 (iterable object) 可以是列表, 元组, 字典, 集合或 range(), 在信息科学中迭代 (iteration) 可以解释为重复执行语句.
#### range ()函数
range() 必须要指定 stop 参数数值， range(start, stop, step), 如果只有一个参数，则参数代表 stop
```python
# for 循环 : 执行指定次数的循环
# 需求 : 我爱北京天安门
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

```
#### 输出结果

```python
我爱北京天安门
我爱北京天安门
我爱北京天安门
我爱北京天安门
我爱北京天安门
我爱北京天安门
我爱北京天安门
我爱北京天安门
我爱北京天安门
我爱北京天安门
11 22 33 44 55

hello world!
```

生成式 (generator) 是一种使用迭代方式产生 Python 数据的方式, 可以产生表, 字典, 集合等.这是结合循环与条件表达式精简程序代码的方法, 如果会使用此概念设计程序, 表示你的 Python功力已跳出初学阶段, 如果你有其他程序语言经验, 表示你已经逐渐跳出其他程序语言的枷锁, 逐步脱变成真正的 Python 程序设计师.

需求 1 : 生成 10 个 0 的列表对象
```python
alist = [0] * 10
print(alist)

```
#### 输出结果

```python
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
```

需求 2 : 生成 1~10 之间的所有偶数序列
```python
# for i in range(2, 11, 2):
#     print(i)
# 列表生成器
blist = [i for i in range(2, 11, 2)]
print(blist)
```
#### 输出结果

```python
[2, 4, 6, 8, 10]
```
需求 3 : 列出 20 之内的所有勾股数 [3, 4, 5] [5, 12, 13] ...
勾股定义 : a² + b² = c²
运用循环个的方式写：
```python
for a in range(1, 20, 1):
  for b in range(a, 20, 1):
    for c in range(b, 20, 1):
# 判断
      if a ** 2 + b ** 2 == c ** 2:
          print(a, b, c)
```
列表生成器是对循环写法的一种简化
```python
clist = [(a, b ,c) for a in range(1, 20, 1) for b in range(a, 20, 1)  for c in range(b, 20, 1) if a ** 2 + b ** 2 == c ** 2]
print(clist)
```
#### 输出结果

```python
[(3, 4, 5), (5, 12, 13), (6, 8, 10), (8, 15, 17), (9, 12, 15)]
```
### 4.2 while循环
* 这也是一个循环, 基本上循环会一直执行, 直到条件运算为 False 才会离开循环, 所以设计 while 循环时一定要设计一个条件可以离开循环, 相当于让循环结束.
* 程序设计时, 如果忘了设计可以离开循环的条件, 程序会造成无限循环状态.
* 一般 while 循环使用的是条件控制循环, 在符合特定条件下执行, for 循环则是一种计数循环, 会重复执行特定次数.
#### 认识哨兵值
* 在程序设计时, 我们可以在 while 循环中设定一个输入数值当做循环执行结束的值, 这个值称哨兵值 (sentinel value)
  
需求 1 : 有一筐鸡蛋, 至少有两个, 两个两个数, 多一个, 三个三个数, 多一个, 四个四个数, 还是多一个, 请问, 至少有几个?
```python
count = 2
# 死循环
while True:
# 判断
    if count % 2 == 1 and count % 3 == 1 and count % 4 == 1:
        print(f'{count = }')
        break
    count += 1

```
#### 输出结果

```python
count = 13
```
#### 哨兵值
```python
print('人机复读机对话!')
# 哨兵值
active = True
while active:
    dialog = input() # 用户输入对话 (没有提示词)
if dialog == 'quit': # 退出
    active = False # 将哨兵值修改为 `假`
print(dialog)
```
#### 输出结果

```python
人机复读机对话!
hello
hello
how old are you
how old are you
怎么老是你呀
怎么老是你呀
quit
quit
```

## 5. 函数定义
```python
# 定义一个函数
# 1. 返回值类型 void, int, float, double, list, dict ...
# 2. 函数名 (见名知意)
# 3. 参数列表 (数据往往是需要指定类型)
# def greeting(name, age):
# pass # 让语法检测先通过
def greeting(name: str, age: int) -> str:
    name = name.title() # 名字的首字母大写
    # age 修改
    age = 18
    return f'Hello {name}, you are {age} years old. you are very handsome.'
# 调用函数
msg = greeting('jack', 18)
print(f'{msg = }')
```
#### 输出结果

```python
msg = 'Hello Jack, you are 18 years old. you are very handsome.'
```
回传多个数据的应用 (实质是回传tuple)

```python
# 定义函数 : 返回多个结果
def math_operation(x: int, y: int) -> tuple:
  add = x + y
  minus = x - y
  multiply = x * y
  divide = x / y
  return add, minus, multiply, divide
result = math_operation(5, 2)
print(f'{result = }, {type(result) = }')
```
#### 输出结果

```python
result = (7, 3, 10, 2.5), type(result) = <class 'tuple'>
```
在设计Python的函数时, 有时候可能会碰上不知道会有多少个参数会传递到这个函数, 此时可以用下列方式设计.
函数返回的数据可以不指定类型，返回的就是元组类型tuple， 类型tuple类型不可以一改变数据类型
```python
# 定义函数 : 参数是不定长参数
def math_operation(*args) -> int:
    # args 本质是元组类型
    res = 0
    for arg in args:
        res += arg
    return res
r = math_operation(1,2,3,4,5)
print(f'{r = }')
```
#### 输出结果

```python
r = 15
```
我们可以设计含任意数量关键词参数的函数, 方法是在函数内使用 **kwarg(kwargs是程序设计师可以自行命名的参数, 可以想成 key word argumengs) 这是关键词参数将会变成任意数量的字典元素, 其中自变量是键, 对应的值是字典的值

```python
python = 90 chinese = 100 math = 98 english = 60
python = 90 chinese = 100 math = 98 english = 60
r = {'name': 'Jack', 'score': 348} r1 = {'name': 'Jack', 'score': 348}

```
#### 输出结果

```python
python = 90 chinese = 100 math = 98 english = 60
python = 90 chinese = 100 math = 98 english = 60
r = {'name': 'Jack', 'score': 348} r1 = {'name': 'Jack', 'score': 348}
```

匿名函数最大特色是可以有许多的参数, 但是只能有一个程序表达式, 然后可以将执行结果回传
```python
# 匿名函数 lambda 表达式
def square(x):
    return x*x
r1 = square(5)
print(r1)

# 这个就是匿名函数
lambda x: x*x
# filter(func, iterable) 过滤函数 Python

alist = [i for i in range(1, 101, 1)]
# r = filter(lambda x: x % 3 == 0, alist)
r = list(filter(lambda x: x % 3 == 0, alist))
print(r)
```
#### 输出结果

```python
25
[3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99]
```

## 6. ⾯向对象
设计两个共性的 动物类 与 食物类
动物类子类有: 狗类,猫类,鸟类都继承自动物类. 有名称属性, 和吃的行为.
食物类子类有 : 骨头, 鱼, 虫子
最后设计一个Person类,拥有喂动物的行为.

`思考 :`
1. 当父类的某些方法, 需要声明, 但是又不确定如何实现时, 怎么办?
2. 不需要实例化父类对象, 父类主要作用是设计和制定规范, 让其它类来继承并实现, 怎么办?
3. 解决方案 -> 抽象类
#### 抽象类的介绍
1. 默认情况下, Python不提供抽象类, Python附带一个模块, 该模块为定义抽象基类提供了基础, 该模块名称为 ABC
2. 当我们需要抽象基类时, 让类继承 ABC (abc模块的ABC类), 使用 @abstractmethod 声明抽象方法 (@abstractmethod 用于声明抽象方法的装饰器, 在abc模块中), 那么这个类就是抽象类
3. 抽象类的价值更多作用是在于设计, 是设计者设计好后, 让子类继承并实现抽象类的抽象方法
#### 多态练习
综合案例 : 本案例综合了面向对象中的四大特性 (封装, 继承, 多态, 抽象)
```python
# 导入 Abstract Base Class 抽象基类 abstractmethod 抽象方法的装饰器
from abc import ABC, abstractmethod
# Food 类
class Food(object):
    # 构造方法
    def __init__(self, name):
        self.name = name
# 子类
class Bone(Food):
    def __init__(self):
        super().__init__('骨头')
class Fish(Food):
    def __init__(self):
        super().__init__('鱼')
class Worm(Food):
    def __init__(self):
        super().__init__('虫子')
# Animal 类
class Animal(ABC):
# 构造方法 Animal()
    def __init__(self, name):
        self.name = name
# getter 方法
@property
def name(self):
# 逻辑判断
    if self.__name:
        return self.__name # __变量 这就是私有属性
    else:
        return '没有名字'
    # setter 方法
    @name.setter
    def name(self, name):
        # 逻辑判断
        if isinstance(name, str):
            self.__name = name.title()
        else:
            self.__name = None # 空对象
        # 吃的行为
        # 父类中的 eat() 行为本质上是一个抽象行为, 需要让子类必须重写该行为
        @abstractmethod
        def eat(self, food: Food):... # 这是一个抽象方法, 没有实现了. 要求子类必须重写父类的该行为


# 子类 `继承` 父类
class Dog(Animal):
    def __init__(self, name):
    # 调用父类的构造方法
    # super(Dog, self).__init__(name)
        super().__init__(name)
    # 子类要重写父类的 eat() 行为
    def eat(self, food: Food):
        print(f'{self.name}正在吃{food.name}.')
    # 特有行为
    def bomb_blockhouse(self):
        print(f'{self.name}正在疯狂的炸碉堡...')

class Cat(Animal):
    def __init__(self, name):
     super().__init__(name)
    def eat(self, food: Food):
        print(f'{self.name}正在吃{food.name}.')
    # 特有行为
    def mymoe(self):
        print(f'{self.name}正在疯狂卖萌...')

class Bird(Animal):
    def __init__(self, name: str):
        super().__init__(name)
    def eat(self, food: Food):

        print(f'{self.name}正在吃{food.name}.')
    # 特有行为
    def pole_dance(self):
        print(f'{self.name}正在疯狂跳钢管舞...')
    # 定义一个 Person 类
class Person(object):
    # 构造方法
    def __init__(self, name):
        self.name = name
    # 喂动物吃东西的行为
    def feed(self, animal: Animal, food: Food): # 多态: 父类引用可以接收子类对象
        print(f'{self.name}正在喂{animal.name}吃东西...')
        # 使用 animal 对象调用 eat() 行为
        animal.eat(food)
        print(f'{animal.name}吃饱了. 准备给 {self.name} 表演一个!!!')
        # 准备调用 animal 对象的特有行为
        if isinstance(animal, Dog):
            animal.bomb_blockhouse()
        elif isinstance(animal, Cat):
            animal.mymoe()
        elif isinstance(animal, Bird):
            animal.pole_dance()
# 测试
p = Person('孙悟空')
dog = Dog('哮天犬')
cat = Cat('加菲猫')
bird = Bird('鹦鹉')
bone = Bone()
fish = Fish()
worm = Worm()
p.feed(cat, fish)
```
#### 输出结果

```python
孙悟空正在喂加菲猫吃东西...
加菲猫正在吃鱼.
加菲猫吃饱了. 准备给 孙悟空 表演一个!!!
加菲猫正在疯狂卖萌...
```
## 7. ⽂件操作
文件的类型 : 按文件中数据的组织形式, 文件分为以下两大类
1.文本文件: 存储的是普通字符文件, 默认为 unicode字符集, 可以使用记事本程序打开.
2.二进制文件: 把数据内容用，字节 进行存储, 无法用记事本打开, 必须使用专门的软件打开.
举例: mp3音频文件, jpg图片, doc文档等.
with语句可以自动管理上下文资源, 不论什么原因跳出with块,都能确保文件正确的关闭, 以此来达到释放资源的目的.

#### 文本文件路径
```python
source_path = r'D:\test.txt'
destination_path = r'D:\copy.txt'

# 文件文件复制
# mode='rt' read text mode='wt' write text
with open(source_path, mode='rt', encoding='utf-8') as reader:
    content = reader.read() # 读取文件中的所有数据
    with open(destination_path, 
```

#### 非文件文件复制

```python
# 非文件文件复制# 非文本文件路径
source_path = r'D:\桌面logo.jpg'
destination_path = r'D:\logo.jpg'
# 非文件文件复制
# mode='rb' read binary mode='wb' write binary
with open(source_path, mode='rb') as reader:
    content = reader.read() # 读取文件中的所有数据
    with open(destination_path, mode='wb') as writer:
        writer.write(content)   
```

#### 登录日志综合案例
1. 实现登录验证, 如果用户名是列表中的元素 ['Smith', 'Tom', 'Jack'], 密码'888' 则登录成功, 否则失败
2. 不管登录是否成功, 都需要在文件中记录登录的信息
3. 登录成功, 可以看到相应的操作菜单提示, 请实现相应的功能
```python
import time
# 登录日志综合案例
FILENAME = 'log.txt' # 相对路径
# 写入数据到日志文件中
def record_log(user, status):
# append 拼接模式
    with open(FILENAME, mode='a+', encoding='utf-8') as f:
        chinese_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        log = f'登录用户: {user}, {status}, 登录时间: {chinese_time}'
        f.write(log + '\n')
def read_log():
    with open(FILENAME, mode='rt', encoding='utf-8') as f:
        for line in f.readlines():
            # strip() 功能 : 去除字符串对象收尾的空格和换行
            line = line.strip()
            print(line)
# 展示界面
def show_menu():
    menu = '''
        **********************
        1. 当前登录用
        户
        2. 查看登录日志
        3. 退出系统
    '''
    print(menu)
# 接收用户的输入
user = input('亲, 请输入你的用户名: ')
pwd = input('亲, 请输入您的登录密码: ')
# 判断
if user in ('Jack', 'Rose', 'Peter') and pwd == '888':
# 当前用户是注册用户, 可以登录
    record_log(user, '登录成功')
    # 保证界面不退出
    while True:
        # 展示界面
        show_menu()
        # 提供用户输入选择
        choice = input('亲, 请输入您的操作码: ')
        if choice == '1':
            print('当前用户: ', user)
        elif choice == '2':
            read_log()
        elif choice == '3':
            record_log(user,'退出系统')
            print(f'感谢您的使用 , 期待下次再见!')
            break
        else:
            print('您的输入有误, 请重新选择!!!')
else:
    # 登录失败
    print('登录失败! 您的用户名或密码错误.')
    record_log(user, '登录失败')
```
## 8. 异常处理
有时也可以将程序错误 (error) 称作程序异常 (exception)

相信每一位写程序的人一定会常常碰上程序错误,过去碰上这类情况程序将终止执行, 同时出现错误信息, 错误信息内容通常是显示Traceback, 然后列出异常报告

Python可以让我们捕捉异常和撰写异常处理程序, 当异常被捕捉时会去执行异常处理程序, 然后程序可以继续执行.
### 8.1 ⼀个除数为 0 的错误
```python
# 异常 : 如果不处理异常, 程序就会提前终止
def division(x, y):
    return x / y
    
print(division(2, 3))
# 这条语句会发生程序的异常.
# ZeroDivisionError: division by zero
print(division(4, 0))
# 分析 : 以下的输出语言可以被执行吗?
print(division(4, 1))
```
#### 输出结果

```python

```
### 8.2 撰写异常处理程序 try - except - else - finally
Python 的关键词 finally 功能是和 try 配合使用
, 在try 之后可以有 except 或 else, 这个 finally 关键词必
须放在 except 和 else 之后, 同时不论是否有异常发生一定会执行这个 finally 内的程序代码.
```python
# 异常 : 如果不处理异常, 程序就会提前终止
def division(x, y):
    # 需要将可能发生异常的逻辑代码放到 try 语句中
    try:
        # 这里有很多的逻辑执行语句...
        v = x / y
    except ZeroDivisionError as e:
        print(e)
        return '除数不能为0!'
    except TypeError as e:
        print(e)
        return '数据类型错误, 需要使用整型数据.'
    except BaseException as e: # 兜底处理
        print(e)
        return '发生了异常!'
    else:
        # 如果 try 语句中执行一切正常, 则 else 语句会被执行.
        # 如果发生了异常, else 语句就不会被执行
        return v
    finally:
        # 这里的代码是用于释放资源 (文件资源, 连接池资源, 数据库资源...)
        # 无论是否发生了异常, finally 语句快都会在 return 之前被执行    
        print('finally 语句块被执行...')

        
print(division(2, 3))
print(division(4, 0))
print(division(4, '2'))
print(division(4, 1))
```
#### 输出结果

```python
finally 语句块被执行...
0.6666666666666666
division by zero
finally 语句块被执行...
除数不能为0!
unsupported operand type(s) for /: 'int' and 'str'
finally 语句块被执行...
数据类型错误, 需要使用整型数据.
finally 语句块被执行...
4.0
```
### 8.3 ⾃定义异常与丢出异常
前面介绍的异常皆是Python直译器发现异常时, 自行丢出异常对象, 如果我们不处理程序就终止执行, 如果我们使用 try-except 处理程序可以在异常中继续执行.

我们自己将它定义为异常然后丢出异常信息, 程序停止正常往下执行, 同时让程序跳到自己设计的except 去执行.
```python
# 自定义异常类
class AgeException(BaseException):
    # 构造方法
    def __init__(self, msg):
        super().__init__(msg)
# 自定义函数
def check_age(age):
    if age < 18:
        # 抛出自定义异常对象
        raise AgeException('你未成年, 不能购买烟酒, 不能去98嗨~~')
    else:
        print('恭喜你成年了, 来, 跟我一起high~~~')
# 测试
try:
    age = int(input('亲, 请输入您的年龄: '))
    # 调用自定义函数
    check_age(age)
except AgeException as e:
    print(e)
    
print('继续执行后续代码...')
```
#### 输出结果

```python
亲, 请输入您的年龄: 32
恭喜你成年了, 来, 跟我一起high~~~
继续执行后续代码...
```
## 9. 模块化编程
在真正做项目时, 我们会使用别人已经开发好的模块, 这样就不必从零开发项目了, 还可以加快开发速度,这些模块可能是Python官方提供的, 也可能是第三方开发的.Python官方提供的模块,就叫做 内置模块.

Python可以说是一个模块化编程的高级语言.
### 9.1 math 模块
在math模块中包含数学运算相关的函数, 例如指数, 对数, 平方根和三角函数等.
```python
# 导入模块
import math
# 20实际最美的数学公式 : 欧拉 e的iπ + 1 = 0
# math 模块
print(math.pi)
print(math.tau)
print(math.e)
# 阶乘 (递归函数)
r = math.factorial(5)
print(r)
# 欧几里得 (初高中几何 -> 源自于 <几何原本>)
# 最大公约数
print(math.gcd(40, 104))
# 最小公倍数
print(math.lcm(40, 104))
```
#### 输出结果

```python
3.141592653589793
6.283185307179586
2.718281828459045
120
8
520
```
### 9.2 random 模块
所谓的随机数是指平均散布在某区间的数字, 随机数其实用途很广, 最常见的应用是设计游戏时可以控制输出结果, 赌场的老虎机器就是靠它赚钱. 我们将介绍random模块中最有用的几个方法, 同时也会分析赌场赚钱的原因.
| 函数名称     | 说明  | 
| -------- | ------------ | 
| randint(x, y)     | 产生x(含)到y(含)的随机整数   | 
| random( )     | 产生0(含)到1(不含)的随机浮点数     | 
| uniform(x, y)     | 产生x(含)到y(不含)的随机浮点数      | 
| choice(列表) | 可以在列表中随机回传一个元素      | 
| shume(列表)     | 可以在列表中随机回传一个元素    | 
| sample(列表,数量)   | 随机回传第2个参数数量的列表元素     | 
| seed(x)   | X是种子值，未来每次可以产生相同的随机数     |


```python
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
```
#### 输出结果

```python
0.33560066760968
a
['c', 'b']
['a', 'g', 'b', 'i', 'j', 'e', 'd', 'f', 'c', 'h']
```
### 9.3 ⽇期时间模块
| strftime( )参数     | 意义  | 
| -------- | ------------ | 
| %Y    | 含世纪的年份，例如:'2020’   | 
| %y    | 不含世纪的年份，例如:'20' 代表 '2020’     | 
| %B     | 用完整英文代表月份，例如:'January’代表1月    | 
| %b     | 用缩写英文代表月份，例如:'Jan’代表1月      | 
| %m    | 用数字代表月份，“01’~'12’   | 
| %j   | 该年的第几天，'001’~'366    | 
| %d   | 该月的第几天，'01’~'31’     |
｜%A    ｜用完整英文代表星期几，例如:'Sunday’代表星期日｜
｜%a   ｜用缩写英文代表星期几，例如:'Sun’代表星期日｜
｜%w    ｜用数字代表星期几，'0’星期日~'6’星期六｜
｜%H     ｜24 小时制，'00’~'23｜
｜%I   ｜12 小时制，'01’~'12｜
｜%M   ｜分，'00’~'59’｜
｜%S   ｜秒，'00’~'59’｜
｜%P   ｜'AM’或'PM｜
```python
# 第一个 datetime 表示的是模块的名称
# 第二个 datetime 表示的是类名
from datetime import datetime, timedelta # 微小的时间间隔
today = datetime.today()
print(f'{today = }')
now = datetime.now()
print(f'{now = }')
# 将日期时间对象按照指定的模式转换为字符串格式时间数据
# f -> format 格式化
now_str = now.strftime('%Y-%m-%d %H:%M:%S')
print(now_str, type(now_str))
# 将字符串类型的数据转换为时间日期类型的数据
# p -> parse 解析
date_str = '2008年08月08日 00:10:50'
d = datetime.strptime(date_str, '%Y年%m月%d日 %H:%M:%S')
print(f'{d = }, {type(d)}')
# timedelta 微小的时间间隔
# 需求 : 从现在向后推, 100 之后是哪一天 ?
# now + 100 # datetime + int
future = now + timedelta(days=100)
print(f'{future = }')
```
#### 输出结果

```python
today = datetime.datetime(2026, 10, 28, 17, 22, 19, 537320)
now = datetime.datetime(2026, 10, 28, 17, 22, 19, 537522)
2026-10-28 17:22:19 <class 'str'>
d = datetime.datetime(2008, 8, 8, 0, 10, 50), <class 'datetime.datetime'>
future = datetime.datetime(2027, 2, 5, 17, 22, 19, 537522)
```
### 9.4 ⾃定义模块
`思考 :` 什么要自定义模块?
答 : 在实际开发中, Python提供的标准库模块不能满足开发需求, 程序员需要一些个性化的模块, 就可以进行自定义模块的实现.
`说明：`模块导入 - 基本语法
[from 模块名] import (函数 | 类 | 变量 | *) [as 别名]
1. [ ] 是可选项
2. 可以根据需求, 选择合适的形式进行导入
`思考 :` 为什么需要包?
在一个实际的项目, 可能需要很多个模块, 当模块文件越来越多, 如果我们将所有的模块文件都放在同一个文件夹, 就会带来很多问题, 不利于管理和调用, 怎么办?

`说明：`
1. 这里写了六个模块文件, 实际上可能有很多的模块文件.
2. 把所有的模块文件, 都放到一个目录下, 必然造成管理的混乱.
3. 怎么办? -> 包
```python
today = datetime.datetime(2026, 10, 28, 17, 22, 19, 537320)
now = datetime.datetime(2026, 10, 28, 17, 22, 19, 537522)
2026-10-28 17:22:19 <class 'str'>
d = datetime.datetime(2008, 8, 8, 0, 10, 50), <class 'datetime.datetime'>
future = datetime.datetime(2027, 2, 5, 17, 22, 19, 537522)
```
#### 输出结果

```python
这个冰淇淋的配料如下: 
         草莓酱
         葡萄干
         巧克力碎片
您点的饮料如下: 
         大杯
         Black Coffee
```

```python
# import makefood
# from makefood import make_icecream, make_drink
import makefood as m
# main 函数
if __name__ == '__main__':
    # 使用模块
    # makefood.make_icecream('草莓酱', '葡萄干', '巧克力碎片')
    # makefood.make_drink('大杯', 'black coffee')
    # make_icecream('草莓酱', '葡萄干', '巧克力碎片')
    # make_drink('大杯', 'black coffee')
    m.make_icecream('草莓酱', '葡萄干','巧克力碎片')
    m.make_drink('大杯', 'black coffee')
    print('hello world!')
```
#### 输出结果

```python
这个冰淇淋的配料如下:
    草莓酱
    葡萄干
    巧克力碎片
您点的饮料如下:
    大杯
    Black Coffee
hello world!
```

### 9.5 第三⽅模块
看见更大的 Python 世界 -> https://pypi.org/
pip有哪些命令可以使用，可以使用 pip help 命令来查看：

### 9.5.1 ⽹络爬⾍
* requests-对HTTP协议进行高度封装，支持非常丰富的链接访问功能。
* PySpider-一个国人编写的强大的网络爬虫系统并带有强大的WebUI。
* bs4-beautifulsoup4库，用于解析和处理HTML和XML。
* Scrapy-很强大的爬虫框架，用于抓取网站并从其页面中提取结构化数据。可用于从数据挖掘到监控和自动化测试的各种用途
* Crawley-高速爬取对应网站的内容，支持关系和非关系数据库，数据可以导出为JSON、XML等
* Portia-可视化爬取网页内容
* cola-分布式爬虫框架
* newspaper-提取新闻、文章以及内容分析
* lxml-lxml是python的一个解析库，这个库支持HTML和xml的解析，支持XPath的解析方式
### 9.5.2 ⾃动化
* XlsxWriter-操作Excel工作表的文字，数字，公式，图表等
* win32com-有关Windows系统操作、Office（Word、Excel等）文件读写等的综合应用库
* pymysql-操作MySQL数据库
* pymongo-把数据写入MongoDB
* smtplib-发送电子邮件模块selenium-一个调用浏览器的driver，通过这个库可以直接调用浏览器完成某些操作，比如输入验证码，常用来进行浏览器的自动化工作。
* pdfminer-一个可以从PDF文档中提取各类信息的第三方库。与其他PDF相关的工具不同，它能够完全获取并分析 P D F 的文本数据
* PyPDF2-一个能够分割、合并和转换PDF页面的库。
* openpyxl- 一个处理Microsoft Excel文档的Python第三方库，它支持读写Excel的xls、xlsx、xlsm、xltx、xltm。
* python-docx-一个处理Microsoft Word文档的Python第三方库，它支持读取、查询以及修改doc、docx等格式文件，并能够对Word常见样式进行编程设置。
### 9.5.3 数据分析及可视化
* matplotlib-Matplotlib 是一个 Python 2D 绘图库，可以生成各种可用于出版品质的硬拷贝格式和跨平台交互式环境数据。Matplotlib 可用于 Python 脚本，Python 和 IPython shell（例如 MATLAB或 Mathematica），Web 应用程序服务器和各种图形用户界面工具包。”
* numpy-NumPy 是使用 Python 进行科学计算所需的基础包。用来存储和处理大型矩阵，如矩阵运算、矢量处理、N维数据变换等。
* pyecharts-用于生成 Echarts 图表的类库
* pandas-一个强大的分析结构化数据的工具集，基于numpy扩展而来，提供了一批标准的数据模型和大量便捷处理数据的函数和方法。
* Scipy: 基于Python的matlab实现，旨在实现matlab的所有功能，在numpy库的基础上增加了众多的数学、科学以及工程计算中常用的库函数。
* Plotly-Plotly提供的图形库可以进行在线WEB交互，并提供具有出版品质的图形，支持线图、散点图、区域图、条形图、误差条、框图、直方图、热图、子图、多轴、极坐标图、气泡图、玫瑰图、热力图、漏斗图等众多图形
* wordcloud-词云生成器
* jieba-中文分词模块
### 9.5.4 WEB开发
* Django-一个开放源代码的Web应用框架，由Python写成。 是Python生态中最流行的开源Web应用框架，Django采用模型、模板和视图的编写模式，称为MTV模式。
* Pyramid是一个通用、开源的Python Web应用程序开发框架。它主要的目的是让* Python开发者更简单的创建Web应用，相比Django，Pyramid是一个相对小巧、快速、灵活的开源Python Web框架。
* Tornado-一种 Web 服务器软件的开源版本。Tornado和现在的主流Web服务器框架（包括大多数Python的框架）有着明显的区别：它是非阻塞式服务器，而且速度相当快
* Flask是轻量级Web应用框架，相比Django和Pyramid，它也被称为微框架。使用Flask开发Web应用十分方便，甚至几行代码即可建立一个小型网站。Flask核心十分简单，并不直接包含诸如数据库访问等的抽象访问层，而是通过扩展模块形式来支持。

### 9.5.5 机器学习
* NLTK-一个自然语言处理的第三方库，NLP领域中常用，可建立词袋模型（单词计数），支持词频分析（单词出现次数）、模式识别、关联分析、情感分析（词频分析+度量指标）、可视化+matploylib做分析图）等
* TensorFlow-谷歌的第二代机器学习系统，是一个使用数据流图进行数值计算的开源软件库。
* Keras -是一个高级神经网络 API，用 Python 编写，能够在 TensorFlow，CNTK 或 Theano 之上运行。它旨在实现快速实验，能够以最小的延迟把想法变成结果，这是进行研究的关键。”
* Caffe-一个深度学习框架，主要用于计算机视觉，它对图像识别的分类具有很好
的应用效果
* theano-深度学习库。它与Numpy紧密集成，支持GPU计算、单元测试和自我验证，为执行深度学习中大规模神经网络算法的运算而设计，擅长处理多维数组。
* Scikit-learn-是一个简单且高效的数据挖掘和数据分析工具，它基于NumPy、SciPy和matplotlib构建。Scikit-learn的基本功能主要包括6个部分：分类，回归，聚类，数据降维，模型选择和数据预处理。Scikit-learn也被称为sklearn。

### 9.5.6 其他常⽤
* IPython-一个基于Python 的交互式shell，比默认的Python shell 好用得多，支持变量自动补全、自动缩进、交互式帮助、魔法命令、系统命令等，内置了许多很有用的功能和函数
* PTVS-Visual Studio 的 Python 工具pydub-支持多种格式声音文件，可进行多种信号处理、信号生成、音效注册、静音处理等
* TimeSide-能够进行音频分析、成像、转码、流媒体和标签处理的Python框架
* dnspython-DNS工具包pygame-专为电子游戏设计的一个模块
* PyQt5-pyqt5是Qt5应用框架的Python第三方库，编写Python脚本的应用界面
* PIL(Pillow)-PIL库是Python语言在图像处理方面的重要第三方库，支持图像存储、显示和处理，它能够处理几乎所有图片格式，可以完成对图像的缩放、剪裁、叠加以及向图像添加线条、图像和文字等操作
* OpenCV-图像和视频工作库
* Py2exe: 将python脚本转换为windows上可以独立运行的可执行程序。
* WeRoBot 是一个微信公众号开发框架，也称为的微信机器人框架。WeRoBot可以解
析微信服务器发来的消息，并将消息转换成成Message或者Event类型。

