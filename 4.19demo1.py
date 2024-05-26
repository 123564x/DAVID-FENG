s="helloworld"
s1 = s[0:5:2]
print(s1)
# 省略开始位置
print(s[:5:1])
# 省略结束位置
print(s[0:7:1])
# 省略步长
print(s[0:6:1])
# 省略开始位置、结束位置、步长
print(s[::])


s = "helloworld"
s1 = s[0:5:2]
print(s1)
print(s[:5:1])
print(s[0:7:1])
print(s[0:6:])
print(s[::])


s = "helloworld"
print(s[::-1])
print(s[-1:-11:-1])
print('-' * 40)
print(s[0:10:-1])
print('-' * 40)
print(s[4:-11:-1])
