# 三种导入方式
# import makefood
# from makefood import make_icecream, make_drink
import makefood as m
# main 函数
if __name__ == '__main__':
    # 使用模块
    # makefood.make_icecream('草莓酱', '葡萄干', '巧克力碎片')
    # makefood.make_drink('大杯', 'black coffee')
    # make_icecream('草莓酱', '葡萄干', '巧克力碎片')
    # make_drink('大杯', 'black coffee')
    m.make_icecream('草莓酱', '葡萄干','巧克力碎片')
    m.make_drink('大杯', 'black coffee')
print('hello world!')