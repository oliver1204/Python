# 其他语言的hello world 
'''
public static void main() {
    system.out.print("hello world")
}
'''
# Python 语言的hello world 
print('hello world')

# input() 函数是一个阻塞函数, 回车才代表输入的结束
msg = input('请输入你的内容: ')
print(f'{msg = }, {type(msg) = }')

# 需求 : 让用户输入两个整型数值, 实现数学上的加法运算
n1, n2 = eval(input('请输入两个整型数值: ')) # 10, 20
result = n1 + n2
print(f'{result = }')