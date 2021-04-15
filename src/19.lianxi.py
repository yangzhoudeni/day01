# 练习1: 打印 1990 ~ 2025 年之间所有的闰年组成的数组
# tips: 闰年 被400整除 或 不能被100整除但被4整除
years = []

for year in range(1990, 2026):
    if year % 400 == 0 or year % 100 != 0 and year % 4 == 0:
        years.append(year)

print(years)

# 练习2: 鸡兔同笼问题
# 笼子有若干鸡和兔子, 35个头 94只脚, 请问 鸡和兔子 各多少只?
# tips: 计算机速度快, 可以快速尝试所有组合 找到匹配的
for tu in range(36):
    #  0~35
    ji = 35 - tu
    if ji*2 + tu*4 == 94:
        print('鸡:%s, 兔:%s' % (ji, tu))


# 练习3: 百钱买百鸡
# 文华有100元, 媳妇让他买100只鸡 必须正好花光.
# 已知: 公鸡5元 母鸡3元 小鸡1元/3只.  帮文华找到所有购买方案
for gj in range(21):
    for mj in range(34):
        xj = 100 - gj - mj

        if gj*5 + mj*3 + xj/3 == 100:
            print('公鸡%s, 母鸡%s, 小鸡%s' % (gj, mj, xj))
