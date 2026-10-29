# 异常 : 如果不处理异常, 程序就会提前终止
def division(x, y):
    return x / y
    
print(division(2, 3))
# 这条语句会发生程序的异常, 导致程序提前终止,  第三句无法正常秩序
# ZeroDivisionError: division by zero
print(division(4, 0))
# 分析 : 以下的输出语言可以被执行吗?
print(division(4, 1))