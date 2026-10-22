# raw string 原生字符串 (取消所有转义)
# 文件路径
# filepath = 'D:\TuLing\2421\视频\专为AI设计的Python课程' 这种写法在\T的时候就出错了
filepath = 'D:\\TuLing\\2421\\视频\\专为AI设计的Python课程' 
  
filename = r'D:\TuLing\2421\视频\专为AI设计的Python课程'

print(f'{filepath = }')
print(f'{filename = }')

print('===' * 20)

# binary string
# 二进制数据
s = 'hello world' 
print('===s', s, type(s))
b = b'hello world' # 相当于将字符串类型数据转换为了字节数据
print('===b', b, type(b))