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