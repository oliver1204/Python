# 文本文件路径
source_path = r'/Users/liuziran/Desktop/ecosa/innovation/0.1.html'
destination_path = r'/Users/liuziran/Desktop/ecosa/innovation/0.1.html'

# 文件文件复制
# mode='rt' read text mode='wt' write text
with open(source_path, mode='rt', encoding='utf-8') as reader:
    content = reader.read() # 读取文件中的所有数据
    with open(destination_path, mode='wt', encoding='utf-8') as writer:
        writer.write(content)


# 非文件文件复制# 非文本文件路径
source_path = r'/Users/liuziran/Desktop/ecosa/innovation/0.1.html'
destination_path = r'/Users/liuziran/Desktop/ecosa/innovation/0.1.html'
# 非文件文件复制
# mode='rb' read binary mode='wb' write binary
with open(source_path, mode='rb') as reader:
    content = reader.read() # 读取文件中的所有数据
    with open(destination_path, mode='wb') as writer:
        writer.write(content)   


import time
# 登录日志综合案例
FILENAME = 'log.txt' # 相对路径
# 写入数据到日志文件中
def record_log(user, status):
# append 拼接模式
    with open(FILENAME, mode='a+', encoding='utf-8') as f:
        chinese_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        log = f'登录用户: {user}, {status}, 登录时间: {chinese_time}'
        f.write(log + '\n')
def read_log():
    with open(FILENAME, mode='rt', encoding='utf-8') as f:
        for line in f.readlines():
            # strip() 功能 : 去除字符串对象收尾的空格和换行
            line = line.strip()
            print(line)
# 展示界面
def show_menu():
    menu = '''
        **********************
        1. 当前登录用
        户
        2. 查看登录日志
        3. 退出系统
    '''
    print(menu)
# 接收用户的输入
user = input('亲, 请输入你的用户名: ')
pwd = input('亲, 请输入您的登录密码: ')
# 判断
if user in ('Jack', 'Rose', 'Peter') and pwd == '888':
# 当前用户是注册用户, 可以登录
    record_log(user, '登录成功')
    # 保证界面不退出
    while True:
        # 展示界面
        show_menu()
        # 提供用户输入选择
        choice = input('亲, 请输入您的操作码: ')
        if choice == '1':
            print('当前用户: ', user)
        elif choice == '2':
            read_log()
        elif choice == '3':
            record_log(user,'退出系统')
            print(f'感谢您的使用 , 期待下次再见!')
            break
        else:
            print('您的输入有误, 请重新选择!!!')
else:
    # 登录失败
    print('登录失败! 您的用户名或密码错误.')
    record_log(user, '登录失败')