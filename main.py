# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from time import sleep, ctime

import sys
from day01.print_index_grammar__prosample import print_sample


def print_hi(names):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {names}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    print_sample()

    # input("\n\n 按下 enter exit")

    x = 'hello world '
    sys.stderr.write(x)
