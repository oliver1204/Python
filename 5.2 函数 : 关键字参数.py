# 定义函数 : 关键字参数
def store_info(name: str, **kwargs) -> dict:
    # keyword arguments 关键字参数, 本质是一个字典类型
    """
    功能 : 存储对应姓名的学生信息
    :param name: 学生姓名
    :param kwargs: python: 编程成绩 chinese: 语文成绩 math: 数学成绩 english: 英语成绩
    :return: 返回一个封装完毕的字典数据 {name: 姓名, score: 总成绩}
    """
    name = name.title() # 名字首字母大写
    python = kwargs['python']
    chinese = kwargs['chinese']
    math = kwargs['math']
    english = kwargs['english']
    # 将四科成绩实现累加
    score = python + chinese + math + english
    return {'name': name, 'score': score}
# 调用
r = store_info('jack', python=90, math=98, chinese=100, english=60)
print(f'{r = }')