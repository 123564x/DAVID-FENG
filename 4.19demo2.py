# s = "helloworld"
# print("e在s中存在吗？", 'e' in s)
# print("v在s中存在吗？", 'v' in s)
# print("e在s中不存在吗？", 'e' not in s)
# print("v在s中不存在吗？", 'v' not in s)
# # 内置函数的使用
# print('len():', len(s))
# print('max():', max(s))
# print('min():', min(s))
# print('s.index(o):', s.index('o'))
# print('s.count(l):', s.count("l"))
#
# # 直接使用【】创建列表
# lst = ['hello', 'world', 98, 100.5]
# print(lst)
#
# # 可以使用内置的函数list()创建列表
# lst2 = list('helloworld')
# lst3 = list(range(1, 10, 2))
# print(lst2)
# print(lst3)
# # 列表是序列中的一种，对序列的操作符，运算符，函数均可以使用
# print(lst + lst2 + lst3)
# print(lst * 3)
# print(len(lst))
# print(max(lst3))
# print(min(lst3))
#
# print(lst2.count('o'))
# print(lst2.index('o'))
# # 列表的删除操作
# lst4 = [10, 20, 30]
# print(lst4)
# # 删除列表
# del lst4
# # print(lst4)  # NameError: name 'lst4' is not defined. Did you mean: 'lst'?

lst = ['hello', 'world', 'python', 'php']
# 使用遍历循环for遍历列表元素
# for item in lst:
#     print(item)
#
# # 使用for循环，range()函数，len()函数，根据索引进行遍历
# for i in range(0, len(lst)):
#     print(i, '-->', lst[i])

# 第三种遍历方式 enumerate()函数
for index, item in enumerate(lst):
    print(index, item)  # index是序号，不是索引
# 手动修改序号的起始值
for index, item in enumerate(lst, start=2):
    print(index, item)
for index, item in enumerate(lst, 1):
    print(index, item)
