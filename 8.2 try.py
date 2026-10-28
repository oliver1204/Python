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