'''
python入门

内置数据类型：
Number：支持int、float、bool、complex
键值对 Dist(字典)
序列：String(字符串)、List(列表)、Tuple(元组)、Set(集合)
不可变类型：Number(值传递)、String、Tuple
可变类型：List、Set(无序不重复)、Dist

流程控制语句：
判断：if-elif-else，没有switch
循环：while_else，for in else
range(x,y,z)
range(len(a))

列表生成式

'''

# 数据类型

# python类型属于对象，变量没有类型，变量不用声明，变量只是对象的引用，变量使用前必须=(等号)赋初值
# 数据类型的转换，将数据类型作为函数名即可
# set(s) 转换为可变集合
# frozenset(s) 转换为不可变集合
# r'''str'''表示多行字符串
# u'''str'''表Unicode编码
# ur'''str'''表示Unicode编码的多行字符串

# x**y 返回x的y次幂

print("---------数据类型转换---------")
i = 1;
f = float(i);
print(i)
print(f)
print("---------------------------\n")

# 集合

# 1. list内置函数append()、pop()...
#    dict内置函数clear()、keys()、values()、items()...
#    dict键不可变，不能用list
# 2. 创建list用[]，创建tuple用()
#    创建set用{}或set()
#    创建dict用{:,:,:,:...}
# 3. 序列的迭代：(str可表示任意序列)
#    枚举enumerate(str)——取索引与值。
#    迭代器iter(str)——取值。通过next(iter)或for-in
#    dict的迭代另外可以用内置函数dict.keys()、dict.values()、dict.items()

# str*2 重复输出str两遍。str可表示任意序列
# str1+str2 组合str1和str2。str可表示任意序列

print("----------创建元祖----------")
t1 = (1, 2, 3, 4, 5, 6)  # 元祖
t2 = ()  # 空元祖
t3 = (20,)  # 含一个元素的元祖，需要在元素后添加逗号
print(t1)
print(t2)
print(t3)
print("---------------------------\n")

print("----------创建dict---------")
dict1 = {}
dict1['one'] = "1"
dict1[2] = "two"

dict2 = {'name': 'Google', 'code': 1, 'site': 'www.Google.com'}

dict3 = dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])  # dict(d) 创建一个字典。d必须是一个序列 (key,value)元组

print(dict1)
print(dict2)
print(dict3)
print("---------------------------\n")

print("---------list切片----------")
s = [1, 2, 3, 4, 5]
l1 = s[:2]  # list切片
l2 = s[-4:-1:2]  # 倒序切片，第3位为step
print(l1)
print(l2)
print("---------------------------\n")

print("--------字符切片取值--------")
s = 'abcdefghijklmn'[::2]  # 字符切片。从头到尾step为2切片
print(s.upper())  # 转为大写
print({x: y for x, y in enumerate(s)})
print("---------------------------\n")

print("--------删除list元素--------")
list = [1, 2, 3, 4, 5, 6, 7]
del list[2]
print(list)
list.remove(5)  # 输入参数为匹配值value
print(list)  # 输入参数为索引index
list.pop()
print(list)
print("---------------------------\n")

print("--------set集合运算---------")
a = set('abracadabra')
b = set('alacazam')
print(a)
print(a - b)  # a和b的差集
print(a | b)  # a和b的并集
print(a & b)  # a和b的交集
print(a ^ b)  # a和b中不同时存在的元素
print("---------------------------\n")

print("----------集合迭代----------")
l = ['a', 'b', 'c']
t = ('tuple 1', 'tuple 2', 'tuple 3', 'tuple 4')
for index, value in enumerate(t):  # 取索引与值，enumerate实际上是返回一个tuple的list
    print(index, '->', value)
print("---------------------------\n")

# 输出个位与百位相等的对称数
print("---------列表生成式---------")
print([x * 100 + y * 10 + z for x in range(1, 10) for y in range(10) for z in range(1, 10) if x == z])
# 生成列表。range(x,y,z) x起始位置，默认值0；y末尾位置；z表示step，默认值1
print("---------------------------\n")
