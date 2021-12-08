# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os.path
from time import sleep, ctime

import sys

from day01.print_index_grammar__prosample import *

import collections

import requests  # 导入requests包

import day01.threading_study

import json


def print_hi(names):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {names}')  # Press Ctrl+F8 to toggle the breakpoint.


class SubResolve(Resolve):
    grade = ""

    def __init__(self, _name, _age, _money, _grade):
        Resolve.__init__(self, _name, _age, _money)
        self.grade = _grade

    def speaker(self):
        Resolve.speaker(self)
        print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))


gate_dog = 1100


def main():
    fish = 1
    while True:
        total, enough = fish, True
        for _ in range(5):
            if (total - 1) % 5 == 0:
                total = (total - 1) // 5 * 4
            else:
                enough = False
                break
        if enough:
            print(f'总共有{fish}条鱼')
            break
        fish += 1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm\n')

    # print_index_day01()

    print_list_set_dict()

    gate_dog = 110000111
    print(gate_dog)
    resolve = SubResolve("xiaoming", 20, 2000, 122)

    resolve.speaker()

    super(SubResolve, resolve)

    main()
    # url = 'https://www.baidu.com/'
    # strhtml = requests.get(url)  # Get方式获取网页数据
    # print(strhtml.text)

    # 创建新线程
    # thread1 = day01.threading_study.FirstThread(1, "Thread-1", 1)
    # thread2 = day01.threading_study.FirstThread(2, "Thread-2", 2)
    #
    # thread1.start()
    # thread2.start()
    # thread1.join()
    # thread2.join()

    datas = {
        'no': 1,
        'name': 'Runoob',
        'url': 'http://www.runoob.com'
    }
    json_data = json.dumps(datas)
    print("Python 原始数据：", repr(datas))
    print("JSON 对象：", json_data)

    # 将 JSON 对象转换为 Python 字典
    data2 = json.loads(json_data)
    print("data2['name']: ", data2['name'])
    print("data2['url']: ", data2['url'])
