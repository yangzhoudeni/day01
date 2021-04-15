# 下标取值

word = 'ABCDEFGHIJKLMN'
#       0123456789

print(word[0])  # 从左向右 0
print(word[-1])  # 从右向左 -1 开始
print(word[2:])  # 从序号2开始到结尾
print(word[2:5])  # 从序号2 ~ 4 : 含头不含尾, [2:5] 不含5

# 通用的求长度函数:len()
print(len(word))

# 字符串相关方法
word = 'nice TO meet YOU'

print(word.upper())
print(word.title())
print(word.capitalize())
print(word.lower())
