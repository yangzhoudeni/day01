'''
tuple: 元组类型
特点: 把数组的 增删改 操作去掉, 只剩下查功能 -- 只能看不能摸
总结: 安全
用途: 作为函数的返回值存在
'''

# 从 [] -> ()
a = ('vue', 'ajax', 'axios')

print(a)
print(type(a))  # <class 'tuple'>

# 元组不支持修改
# a[0] = 'mike'

print(a[0])
print(a[-1])

# 注意事项: 由于元组使用()进行声明
# 元组中至少一个 逗号,
b = ('mike',)
print(b)
print(type(b))
