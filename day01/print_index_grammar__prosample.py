
# 主要是测试字符串的操作


name = "tian123456789"
age = 100


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

    print("======= print_sample end =================")
