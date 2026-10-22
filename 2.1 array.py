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
print('===在后面添加', alist)
alist.insert(0, 9)
print('===在指定位置添加',alist)
element = alist.pop() # 弹出
print('===将末尾删除，并返回', alist, element)
# 指定下标弹出元素
element = alist.pop(0)
print('===删除指定的index，并返回',  alist, element)
# 指定元素删除
alist.remove(2)
print('===指定元素删除某个元素',  alist)
# 修改
alist[0] = 666
print('===修改', alist)