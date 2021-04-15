'''
while: 负责不固定次数的循环

while 条件:
  xxxx
'''

# 制作 猜数字游戏:
import random
# 0-1000之间 随机获取数字
target = random.randint(0, 1000)

count = 0

while True:
    count += 1

    num = input('请猜测一个数字(0-1000):')
    num = int(num)

    if num == target:
        print('恭喜您, 猜对了, 共猜了%s次' % count)
        break
    if num < target:
        print('猜小了')
    if num > target:
        print('猜大了')
