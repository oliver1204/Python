# 综合案例 : 面向对象中的四大特性 (封装, 继承, 多态, 抽象)
# 导入 Abstract Base Class 抽象基类 abstractmethod 抽象方法的装饰器
from abc import ABC, abstractmethod
# Food 类
class Food(object):
    # 构造方法
    def __init__(self, name):
        self.name = name
# 子类
class Bone(Food):
    def __init__(self):
        super().__init__('骨头')
class Fish(Food):
    def __init__(self):
        super().__init__('鱼')
class Worm(Food):
    def __init__(self):
        super().__init__('虫子')
# Animal 类
class Animal(ABC):
# 构造方法 Animal()
    def __init__(self, name):
        self.name = name
# getter 方法
@property
def name(self):
# 逻辑判断
    if self.__name:
        return self.__name # __变量 这就是私有属性
    else:
        return '没有名字'
    # setter 方法
    @name.setter
    def name(self, name):
        # 逻辑判断
        if isinstance(name, str):
            self.__name = name.title()
        else:
            self.__name = None # 空对象
        # 吃的行为
        # 父类中的 eat() 行为本质上是一个抽象行为, 需要让子类必须重写该行为
        @abstractmethod
        def eat(self, food: Food):... # 这是一个抽象方法, 没有实现了. 要求子类必须重写父类的该行为


# 子类 `继承` 父类
class Dog(Animal):
    def __init__(self, name):
    # 调用父类的构造方法
    # super(Dog, self).__init__(name)
        super().__init__(name)
    # 子类要重写父类的 eat() 行为
    def eat(self, food: Food):
        print(f'{self.name}正在吃{food.name}.')
    # 特有行为
    def bomb_blockhouse(self):
        print(f'{self.name}正在疯狂的炸碉堡...')

class Cat(Animal):
    def __init__(self, name):
     super().__init__(name)
    def eat(self, food: Food):
        print(f'{self.name}正在吃{food.name}.')
    # 特有行为
    def mymoe(self):
        print(f'{self.name}正在疯狂卖萌...')

class Bird(Animal):
    def __init__(self, name: str):
        super().__init__(name)
    def eat(self, food: Food):

        print(f'{self.name}正在吃{food.name}.')
    # 特有行为
    def pole_dance(self):
        print(f'{self.name}正在疯狂跳钢管舞...')
    # 定义一个 Person 类
class Person(object):
    # 构造方法
    def __init__(self, name):
        self.name = name
    # 喂动物吃东西的行为
    def feed(self, animal: Animal, food: Food): # 多态: 父类引用可以接收子类对象
        print(f'{self.name}正在喂{animal.name}吃东西...')
        # 使用 animal 对象调用 eat() 行为
        animal.eat(food)
        print(f'{animal.name}吃饱了. 准备给 {self.name} 表演一个!!!')
        # 准备调用 animal 对象的特有行为
        if isinstance(animal, Dog):
            animal.bomb_blockhouse()
        elif isinstance(animal, Cat):
            animal.mymoe()
        elif isinstance(animal, Bird):
            animal.pole_dance()
# 测试
p = Person('孙悟空')
dog = Dog('哮天犬')
cat = Cat('加菲猫')
bird = Bird('鹦鹉')
bone = Bone()
fish = Fish()
worm = Worm()
p.feed(cat, fish)