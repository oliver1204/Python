# 在自定义模块中定义一些功能
# 制作冰淇淋
def make_icecream(*toppings):
    print('这个冰淇淋的配料如下: ')
    for topping in toppings:
        print('\t', topping) # '\t' 制表符

# 制作饮料
def make_drink(size, drink):
    print('您点的饮料如下: ')
    print('\t', size.title())
    print('\t', drink.title())

# 模块测试, 应该放在主函数里面，这样其他引入模块在使用该模块的时候不会执行测试模块
# 如果没有 if __name__ == '__main__': 任何引用模块都会触发此模块执行
if __name__ == '__main__':
    make_icecream('草莓酱' , '葡萄干', '巧克力碎片')
    make_drink('大杯', 'black coffee')


# 错的模块测试代码
# make_icecream('草莓酱' , '葡萄干', '巧克力碎片')
# make_drink('大杯', 'black coffee')