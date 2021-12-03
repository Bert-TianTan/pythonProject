# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from time import sleep, ctime

import sys


def print_hi(names):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {names}')  # Press Ctrl+F8 to toggle the breakpoint.


name = "tian123456789"
age = 100

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    # print("name = %s, age = %d".format(name, age))
    # print(name)
    print(name[1:6:2])  # 每隔一个就打印一个
    print(name[1:6:6])
    print(name[2:])
    print(name * 0)
    print(name * 1)
    print('hello\ntian')
    print(r'hello\ntian')  # 在字符串前面添加一个 r，表示原始字符串，不会发生转义

    # input("\n\n 按下 enter exit")

    x = 'hello world '
    sys.stderr.write(x)

































































































