import os

# if __name__ != '__main__':
if __name__ == '__main__':
    A = os.path.join(os.path.dirname(__file__),
                     '..')  # 当前目录的上一级目录 C:/Users/zhb68/PycharmProjects/pythonPytest-1/sys_dir\..
    E = os.path.abspath(A)  # C:\Users\zhb68\PycharmProjects\pythonPytest-1
    B = os.path.dirname(os.path.realpath(__file__))  # C:\Users\zhb68\PycharmProjects\pythonPytest-1\sys_dir

    C = os.path.abspath(os.path.dirname(__file__))  # C:\Users\zhb68\PycharmProjects\pythonPytest-1\sys_dir

    D = os.path.basename(os.path.realpath(__file__))  # dir2_.py

    print(A, B, C, D, E)

    item = '.'
    if os.path.isdir(item):
        print("isdir: ", item)
    item = os.path.join(item, 'dir2_.py')
    if os.path.isfile(item):
        print("isfile: ", item)
    item = os.path.abspath(os.path.join(item, 'dir2_.py'))
    if os.path.isabs(item):
        print("isabs: ", item)

    if os.path.islink(item):  # linux os
        print("islink: ", item)
    if os.path.ismount(item):  # linux os
        print("ismount: ", item)

    print('____________')
    print(globals())
    print(__file__)  # 是一个全局变量，表示当前文件，与__name__很象
    print(dir(__builtins__))
