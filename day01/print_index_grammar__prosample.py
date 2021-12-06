# 主要是测试字符串的操作

import random

# >>> 5 + 4  # 加法
# 9
# >>> 4.3 - 2 # 减法
# 2.3
# >>> 3 * 7  # 乘法
# 21
# >>> 2 / 4  # 除法，得到一个浮点数
# 0.5
# >>> 2 // 4 # 除法，得到一个整数
# 0
# >>> 17 % 3 # 取余
# 2
# >>> 2 ** 5 # 乘方
# 32

name = "tian123456789"
age = 100


def reverse_words(input_arrays):
    # 通过空格将字符串分隔符，把各个单词分隔为列表
    inputwords = input_arrays.split(" ")

    # 翻转字符串
    # 假设列表 list = [1,2,3,4],
    # list[0]=1, list[1]=2 ，而 -1 表示最后一个元素 list[-1]=4 ( 与 list[3]=4 一样)
    # inputWords[-1::-1] 有三个参数
    # 第一个参数 -1 表示最后一个元素
    # 第二个参数为空，表示移动到列表末尾
    # 第三个参数为步长，-1 表示逆向
    inputwords = inputwords[-1::- 1]

    print(inputwords)

    out_target = ' '.join(inputwords)

    return out_target


def print_sample():
    # print("name = %s, age = %d".format(name, age))
    # print(name)
    print("======= print_sample start =================")
    print(name[1:6:2])  # 每隔一个就打印一个
    print(name[1:6:6])
    print(name[2:])
    print(name * 0)
    print(name * 1)
    print('hello\ntian')
    print(r'hello\ntian')  # 在字符串前面添加一个 r，表示原始字符串，不会发生转义

    print(type(name))

    print(isinstance(name, str))

    print(5 ** 2)  # 5 的平方
    print(5 / 2)  # 2.5

    print(random.choice(range(9)))

    # 从 1-100 中选取一个奇数
    print("randrange(1,100, 2) : ", random.randrange(1, 100, 2))

    # 从 0-99 选取一个随机数
    print("randrange(100) : ", random.randrange(100))

    # 格式化
    site = {"name": "Jack", "age": "100"}
    print("名字：{name}, 年龄：{age}".format(**site))
    # 通过列表索引设置参数
    my_list = ['菜鸟教程', 'www.runoob.com']
    print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是必须的

    print("======= print_sample end =================")


def study_if_else():
    money = 100
    if money < 1:
        print("less than one")
        print("end")
    elif money < 5:
        print("less than 5")
    else:
        print("more than 5")
