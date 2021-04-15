'''
dict 字典类型, 全称: dictionary

特征: 具有最高的查询速度

解释 JS 的对象类型
'''
boss = {
    "键": "值",  # 键值对 结构
    'name': '文华',
    'age': 40,
    'gender': 1,
    'skills': ('vue', 'jQuery', 'Flutter', 'React')
}

print(boss)
print(type(boss))

# 增
# js中 boss.address = 'xxx'
boss['address'] = '北京市丰台区'
print(boss)

# 删
boss.pop('address')
print(boss)

# 改
boss['age'] = 18
print(boss)

# 查
print(boss['age'])
