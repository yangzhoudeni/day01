# 模板字符串:  变量放到字符串中进行显示

name = '东东'
age = 36

# 输出 xxx今年xx岁
# js中: `${name}今年${age}岁`

# 变量拼接到字符串中的写法共有两种方案:
# 方案1: 例如JS, 使用特定的包围来表示变量: 例如js的 ${}, php的 {}
# 方案2: 例如node.js的数据库语句: 采用?占位符  select * from xxx where name=? and age=?

# 此处, python采用占位符方案实现
word = '%s今年%s岁' % (name, age)
print(word)


name = 'iPhone12'
price = '9999'
year = '2021'

# 目标显示: xxxx年的xxx, 售价xxx元
word = '%s年的%s, 售价%s元' % (year, name, price)

print(word)

'''
详解占位符:
%s string 转化字符串显示, 原样显示
%d digit 只显示整数位, 没有四舍五入
%f float 浮点型, 6位小数
%.nf  保留n位小数, 带四舍五入
'''

a = 12.6456

print('%s %d %f %.2f' % (a, a, a, a))
