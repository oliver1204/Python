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