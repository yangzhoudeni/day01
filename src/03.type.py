# 变量类型
'''
在 JS 中: 
* 基础变量类型: number(数字:整型+浮点)  string字符串  boolean布尔(true/false)
* 空类型: null(赋值过,清空了) 和 undefined(从未赋值)
* 复合类型: array数组   object对象
'''

# python中的基础数据类型:

# 整型: python把 js 的 number 类型细分为 整型int 和 浮点型float
a = 5
# type() 相当于js的 typeof()
print(type(a))  # <class 'int'>  int -> integer

# 浮点: 带小数点和科学计数法
a = 5.5
print(type(a))  # <class 'float'>

a = 5e2
print(type(a))  # <class 'float'>

# 布尔类型: 值为 大驼峰写法
a = True
print(type(a))  # <class 'bool'>

a = False
print(type(a))  # <class 'bool'>

# 空
a = None
print(type(a))  # <class 'NoneType'>
