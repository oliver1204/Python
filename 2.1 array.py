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


# 列表切片
# [start : stop : step] 下标 : start=0, stop=10 (不包含) step = 1
alist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# blist = alist[0:5:1]
blist = alist[:5:]
print(blist)
str = 'hello world'
substr = str[0:5:1]
print(substr)

# 列表.sort() 与 sorted() 区别
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
