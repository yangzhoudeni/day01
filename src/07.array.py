# 复合数据类型: 数组

# python把数组 细分成 4 种
'''
* list:  就是js的数组  []   
* tuple : 元组  ()  只能看不能改
* set : 集合  {}  唯一性,去重
* dict : 字典 {'键':'值'}  最高查询速度
'''

# list 列表: 就是js的array

skills = ['jQuery', 'ajax', 'axios', 'xhr', 'vue', 'vuex']

print(skills)
print(type(skills))  # <class 'list'>

# 长度: 通用函数 len()
print(len(skills))

# 增
skills.append('REACT')  # 同js的push()
print(skills)

# 插入到指定位置
skills.insert(1, 'ANGULAR')  # 同js的 skills.splice(1,0,'ANGULAR')
print(skills)

# 删
skills.pop()  # 删除结尾元素;  对应js的pop()
print(skills)

skills.pop(1)  # 删除指定序号元素;  对应js的 splice(i,1)
print(skills)

# 改
skills[0] = '命运'
print(skills)

# 查
print(skills[0])
print(skills[-1])
print(skills[2:])
print(skills[2:5])  # 含头不含尾
