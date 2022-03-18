# 基础乘法
print(7 * 8)

# 基础乘方 2^3 = 8
print(2**3)

# numpy中的乘法
import numpy as np
a = np.array([1,2,3])
b = np.array([10, 10, 10])
print("a:", a)
print("b:", b)
print("a * b =", a * b)
# numpy array所有的方法/变量属性
print(dir(a))


# 引入一个文件（不推荐的方法）
from module_a import *  # 引入numpy中所有的方法/属性
print("外积")
print(array_prod(a, b))  # 外积
from module_b import *  # 引入numpy中所有的方法/属性
print("内积（外积方法被覆盖）")
print(array_prod(a, b))  # 内积


# 正确的引入方法
import module_a as ma
import module_b as mb
print("外积")
print(ma.array_prod(a, b))  # 外积
print("内积（外积方法不会被覆盖）")
print(mb.array_prod(a, b))  # 内积


# 作为数据容器的迭代解构器
a = (1, 2, 3)
b = ['a', 'b', 'c']
print(*a)  # *的作用是按照顺序迭代数据结构（list/tuple/set/dict）
# 1. zip可以将两个同样程度的list/tuple这样的数据结构
# 按照位置依次组合在一起（想象拉链的结合方式）
c = list(zip(a, b))
print(c)
# 任务，已知c求得a，b（逆运算）
print(*c)
a, b = tuple(zip(*c))
b = list(b)
print("a={}; b={};".format(a, b))
# 2. 作为函数(function)的动态参数传递方法
def sum_nums(a, b, c):
    return a+b+c
# 可以用作按照位置顺序的参数输入
sum_nums(*[1,2,3])


d1 = {'a': 1,
     'b': 2,
     'c': 3}
print(sum_nums(*d1)) # 注意，一般我们默认dict不一定保留顺序，虽然Python中key的顺序一般不会改变
print(sum_nums(**d1))
# 按照函数名传递参数

d2 = {'a': 1, 'b': 2, 'c': 3, 'e':100} # sum_nums中不存在的‘e’参数，报错！
print(sum_nums(**d2))


# 函数本身可以定义数量不定的参数
# 下面函数完成记录运算时间的任务
import time
def timer(my_func, *args, **kwargs):
    t0 = time.time()
    for i in range(int(1e6)):
        my_func(*args, **kwargs)
    t1 = time.time()
    print("计算100万次{}函数用时为:{:.4f}秒".format(my_func.__name__, t1-t0) )
def power_nums(a, b, c):
    return a**b**c  # a^(b^(c))
timer(power_nums, **d1)


# 修时器/语法糖的用法（补充内容，本视频不要求）
def my_decorator(my_func):
    def timer(*args, **kwargs):
        t0 = time.time()
        for i in range(int(1e6)):
            my_func(*args, **kwargs)
        t1 = time.time()
        print("计算100万次{}函数用时为:{:.4f}秒".format(my_func.__name__, t1-t0) )
    return timer
@my_decorator
def power_nums(a, b, c):
    return a**b**c
power_nums(**{'a': 2, 'b': 3, 'c': 5})



# 规则：positional arguments必须在keyword argument之前
# 实际项目中如何应用动态传递参数？（例子）
# pandas: dataframe plot (https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html)