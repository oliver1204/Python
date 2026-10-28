count = 2
# 死循环
while True:
# 判断
    if count % 2 == 1 and count % 3 == 1 and count % 4 == 1:
        print(f'{count = }')
        break
    count += 1

print('-' * 20)

print('人机复读机对话!')
# 哨兵值
active = True
while active:
    dialog = input() # 用户输入对话 (没有提示词)
if dialog == 'quit': # 退出
    active = False # 将哨兵值修改为 `假`
print(dialog)