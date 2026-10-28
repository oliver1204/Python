# 计算最终成绩等级

# 请输入数字分数,系统将响应A, B, C, D 或 F 等级.
score = eval(input("Enter score: "))
# 多分支判断
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")