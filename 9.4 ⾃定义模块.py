# 在自定义模块中定义一些功能
# 制作冰淇淋
def make_icecream(*toppings):
    print('这个冰淇淋的配料如下: ')
    for topping in toppings:
        print('\t', topping)
# 制作饮料
def make_drink(size, drink):
    print('您点的饮料如下: ')
    print('\t', size.title())
    print('\t', drink.title())
# 模块测试
if __name__ == '__main__':
    make_icecream('草莓酱' , '葡萄干', '巧克力碎片')
    make_drink('大杯', 'black coffee')


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