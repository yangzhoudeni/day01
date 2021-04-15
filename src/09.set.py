'''
set 集合

特征: 内部元素不重复, 但是去重不保证顺序
'''

a = {'mike', 'lucy', 'lucy', 'mike', 'lily', 'lily'}

print(a)
print(type(a))

# 用途: 通过强制转换类型的方式, 把 数组类型去重

arr = [1, 2, 3, 4, 4, 3, 2, 1]

arr_unique = set(arr)
print(arr_unique)
