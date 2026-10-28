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

# 不指定类型，返回的就是元组类型tuple， 类型tuple类型不可以一改变数据类型
def math_operation(x: int, y: int) -> tuple:
  add = x + y
  minus = x - y
  multiply = x * y
  divide = x / y
  return add, minus, multiply, divide

result = math_operation(5, 2)
print(f'{result = }, {type(result) = }')



