'''
continue
break
'''

for i in range(20):

    if i == 8:
        # 跳出当前次循环, 开始下一次
        continue

    if i == 11:
        # 终止整个循环
        break

    print(i)
