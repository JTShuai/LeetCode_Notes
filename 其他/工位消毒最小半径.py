workstation = [1 ,3, 6, 8, 9, 10, 18, 28, 29, 35]
sterrilizers = [5, 10]

'''
遍历工位，比较每个工位位置和消毒器位置，
如果当前消毒器位置大于工位位置，得到两者之间距离，重复出现时，保留最大距离
如果当前消毒器位置小于工位位置，找到大于工位位置的消毒器（或者可能没有），取 min(当前消毒器与工位的距离, 上一消毒器与工位距离)
'''
workstation.sort()
sterrilizers.sort()
res = 1
cur_index = 0
for work_postion in workstation:

    while cur_index < len(sterrilizers) and sterrilizers[cur_index] < work_postion:
        cur_index += 1

    temp = float('inf')
    if cur_index == len(sterrilizers):
        temp = work_postion - sterrilizers[cur_index-1]
    else:
        # 遍历完毕找到了更大的
        if cur_index >=1:
            temp = min(abs(work_postion - sterrilizers[cur_index]), work_postion - sterrilizers[cur_index-1])
        else:
            # 如果一开始就比当前大
            temp = sterrilizers[cur_index] - work_postion

    res = max(res, temp)

print(res)

if __name__ == '__main__':
    x = [1,3,4,2]
    x.sort()
    print(x)