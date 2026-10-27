# 定义一个元组类型
# tuple 元素不可变
tuple1 = (1, 2, 3, 4, 5)
print(tuple1, type(tuple1))
# tuple1[0] = 6
# print(tuple1, type(tuple1))
# 细节 (元组中仅有单个元素, 需要在元素之后添加逗号, 不能省略)
tuple2 = (1 )
print(tuple2, type(tuple2))

tuple3 = (1, )
print(tuple3, type(tuple3))