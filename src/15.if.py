'''
流程控制语句: 
* 条件分支: if
* 循环: for
'''

# 作者: 简化理念--懒
'''
if (条件){ 代码... }
'''

married = True
# 省略了 () 和 {}
# 必须遵循的规范:  由于没有了{}限定代码范围;  要求严格的缩进, 来代表包含关系
if married:
    print('已婚')

# 双分支语句:  if 和 else 是同级别, 所以必须在一个缩进
if married:
    print("已婚")
else:
    print('未婚')


score = input('请输入文华的得分(0-100):')
# input()的返回值 肯定是字符串类型
score = int(score)

if score >= 90:
    print('优秀')
elif(score >= 60 and score < 90):
    # else if -> elif
    print('良好')
else:
    print('不及格')
