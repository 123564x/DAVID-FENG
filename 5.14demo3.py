# 使用小括号
t = ('hello', [10, 20, 30], 'python', 'world')
print(t)

# 使用内置函数tuple()创建元组
t = tuple('helloworld')
print(t)

t = tuple([10, 20, 30, 40])
print(t)

print('10在元组中是否存在:', (10 in t))
print('10在元组是不存在:', (10 not in t))
print('最大值:', max(t))
print('最小值:', min(t))
print('len:', len(t))
print('t.index:', t.index(10))  # 10元素的位置
print('t.count:', t.count(10))  # 10元素在这个元组中的个数

# 如果元组只有一个元素
t = (10)
print(t, type(t))

# 如果元组只有一个元素，逗号不能省略
y = (10,)
print(y, type(y))

#元组的删除
# del t
# print(t)