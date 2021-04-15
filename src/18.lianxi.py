# 练习1: 计算 1~100之间所有数字的总和  5050
sum = 0

for i in range(1, 101):
    sum += i

print(sum)

# 练习2: 计算1~100 之间所有 偶数之和
sum = 0

for i in range(1, 101):
    if i % 2 == 0:
        sum += i

print(sum)

# 练习3: 计算 1~100 之间, 同时被 3 和 2 整除的数字  之和
sum = 0

for i in range(1, 101):
    if i % 2 == 0 and i % 3 == 0:
        sum += i

print(sum)
