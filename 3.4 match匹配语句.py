score = eval(input("Enter score: "))
level = score // 10 # 算出来的是十位数, // 是除法，不是注释
match level:
    case 10 | 9:
        print("A")
    case 8:
        print("B")
    case 7:
        print("C")
    case 6:
        print("D")
    case _:  # 兜底条件
        print("F")