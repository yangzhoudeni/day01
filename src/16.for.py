# for循环
# python没有传统的for循环:  for(let i=0; i<xx; i++){}

# python只提供 遍历数组写法

skills = ['vuex', 'vue', 'axios', 'ajax', 'json']

for item in skills:
    print(item)

# key?
# range(): 快速生成含有指定数量个数字的数组. 序号从0开始
for i in range(10):
    print(i)

print(list(range(10)))

skills = ['vuex', 'vue', 'axios', 'ajax', 'json']
#            0      1       2           3     4
# 序号的取法
for index in range(len(skills)):
    # arr[下标]: 利用下标读取对应的值
    print('index:', index, '  item:', skills[index])
