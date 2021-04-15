# 冒泡排序

arr = [12, 78, 445, 556, 23, 56, 89, 67]

# 利用冒泡排序 把数组 从小到大排列

# 两两比较, 比较的次数是 总数量 - 1
count = len(arr)-1

for j in range(count):
    for i in range(count):
        # 两两比较  大的 向后移动
        if arr[i] > arr[i+1]:
            # 互换位置 a,b = b,a;  python具备的写法
            arr[i], arr[i+1] = arr[i+1], arr[i]

print(arr)
