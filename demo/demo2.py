import math

'''
demo进阶

函数
输入参数：声明设置默认参数、不定长参数、参数名指定输入参数(顺序可与声明不一致)

数据结构
模块
面对对象
'''

print("--------函数返回多值--------")


def move(x, y, step, angle=4):  # angle定义默认参数
    nx = x + step * math.sqrt(angle)  # sqrt返回浮点型
    ny = y + step * math.sqrt(angle)
    return nx, ny  # 多值返回是一个tuple


a, b = move(100, 100, 60, 1)
print(a, b)
t = move(100, 100, 60)
print(t)
print("---------------------------\n")

print("------函数输入参数可变------")


def summation(*args):  # 定义可变参数
    r = 0
    for i in args:
        r = r + i
    return r


print(summation(1, 2, 3))
print("---------------------------\n")


# 函数式编程：变量可以指向函数
# 高阶函数：能接受函数做参数的函数


def add(x, y, f):
    return f(x) + f(y)


print(add(15, -8, abs))  # 传入abs函数取绝对值
