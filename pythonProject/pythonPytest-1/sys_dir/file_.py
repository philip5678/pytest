import glob
import os

# print(path := os.path.abspath('.'))
# print(cwd := os.getcwd())
# print(path := os.path.abspath('..'))


#
# print(path + r'\file_.py')
# print(path:=os.path.join(path, 'file_.py'))
# print(path:=os.path.join(cwd, 'file_.py'))


# cwd = os.getcwd()
# # create a full path name.Os.path.join automatically inserts forward slashes (“/”) into the path name when needed.
# desktop = os.path.join(cwd, "")
# print(desktop)
#
# print(files := os.listdir(desktop))
#
# for f in files:
#     print(os.path.join(desktop, f))

path = '.'
# The immediate file path

directory_contents = os.listdir(path)
print(directory_contents)
print("----")
# Filter for directories
for item in directory_contents:
    if os.path.isdir(item):
        print(item)
print("----")
directories = glob.glob("*/")
print(directories)
directories = glob.glob("*i?_.py")
directories = glob.glob("*i??_.py")
print(directories)
print("----")
for item in directory_contents:
    if os.path.isfile(item):
        print(item)


# def count_py_files_in_repos(dirname):
#     # count = 0
#     if os.path.exists(path := os.path.join(dirname, '.git')):
#         print(path)
#         count = 0
#         # root, dirs, files=os.walk(dirname)  #X
#         # print(os.walk(dirname))
#         for root, dirs, files in os.walk(dirname):
#             print(root, dirs, files)
#             count += len([f for f in files if f.endswith('.py')])
#         print('{} has {} Python files'.format(dirname, count))
#         for name in os.listdir(dirname):
#             path = os.path.join(dirname, name)
#             if os.path.isdir(path):
#                 count_py_files_in_repos(path)
#     else:
#         count = 0
#     return count
#
#
# count_py_files_in_repos(r'C:\Users\zhb68\PycharmProjects')

# https://www.kite.com/python/answers/how-to-list-immediate-subdirectories-in-python
# https://blog.csdn.net/JohinieLi/article/details/76660733
# https://blog.csdn.net/qq_41979513/article/details/90780868

#
# print('---------------------------------------------')
# for root, dirs, files in os.walk(".", topdown=False):
#     for name in files:
#         print(name)
#     print("----")
#     for name in dirs:
#         print(name)
#
# print('---------------------------------------------')
#
#
# def file_name(file_dir):
#     L = []
#     for dirpath, dirnames, filenames in os.walk(file_dir):
#         # print(filenames)
#         for file in filenames:
#             if os.path.splitext(file)[1] == '.py':
#                 # file_ = os.path.join(dirpath, file)
#                 # print(os.path.split(os.path.join(os.getcwd() + file_)))
#                 # print(os.path.realpath(dir_ := os.path.dirname(file_)))
#                 # print(file_ := os.path.basename(file_))
#                 L.append(os.path.join(dirpath, file))
#     return L

# print(file_name('.'))

# https://docs.python.org/3.8/library/os.path.html#os.path.splitext

# 打开文件
# print('---------------------------------------------')
# path = r'C:\Users\zhb68\PycharmProjects'
# dirs = os.listdir(path)
# print(dirs)
# print('---------------------------------------------')
# # 输出所有文件和文件夹
# for file in dirs:
#     print(os.path.join(os.getcwd(), file))
