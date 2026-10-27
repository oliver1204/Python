nums_str = ["1", "2", "3", "4"]
nums_int = list(map(int, nums_str))
print(nums_int)

#字典类型 : key-value 键值对, 通过 key 实现操作, key 要保证唯一性
# Python : dict() {key: value}

adict = {'张三': 100,'李四': 98,'王五': 88,'赵六': 60}
print(adict)
adict['张三'] = 90
print(adict)
score = adict['张三']
print(f'{score = }')
# keys 键集, values 值集, items 键值对集合
print(adict.keys())
print(adict.values())