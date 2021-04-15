# 字符串

# 单行字符串: 使用 单引号 和 双引号 都可以
a = 'Hello World!'
a = "Hello World!"

print(type(a))  # <class 'str'>

# 多行字符串: 作者复用了 多行注释的写法 ''' '''
a = '''
床前明月光, 疑是地上霜.
举头望明月, 低头写BUG.
-- 命运轨迹
'''
print(a)


# 转义符 \: 去掉字符串中 特殊字符的特殊含义
word = "He said:\"I'm fine!\""
# \" 可以把" 的定界符特征去掉, 变为普通的字符". 就不会冲突了
print(word)

word = "使用\\\" 可以显示普通的\""

print(word)  # 使用\" 可以显示普通的"
