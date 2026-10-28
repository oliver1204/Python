# 定义函数 : 参数是不定长参数
def math_operation(*args) -> int:
    # args 本质是元组类型
    res = 0
    for arg in args:
        res += arg
    return res
r = math_operation(1,2,3,4,5)
print(f'{r = }')