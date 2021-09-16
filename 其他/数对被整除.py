averageScore = 5
n = 5
scores = [1, 10, 5, 4, 3, 2, 7, 6, 8, -1]

'''
能被averageScore整除的两数之和，则 a%averageScore + b%averageScore = averageScore

要让输出的和前面的最大：
1。 先将scores排序
2。 然后得到每个数的余数
3。 优先找大数的余数配对
'''

def task2(scores):
    scores.sort()

    res = []

    # 字典保存每个余数对应的数字
    resi_map = {}

    # 保存每个余数有多少个对应数字
    resi_len = {}

    # 两数之和
    pair_sum = []
    pairs = {}

    while scores:
        cur_max = scores.pop()
        resi = cur_max % averageScore
        if resi in resi_map:
            resi_map[resi].append(cur_max)
            resi_len[resi] +=1
        else:
            resi_map[resi] = [cur_max]
            resi_len[resi] = 1

    # 遍历完毕后检查能否组合，再开始配对
    if 0 in resi_len:
        if resi_len[0]%2 != 0:
            return 0

    for resi in resi_map.keys():
        if resi != 0:
            if (averageScore - resi) not in resi_len:
                return 0
            if resi_len[averageScore - resi] != resi_len[resi]:
                return 0

        # 开始配对,利用res维护一个最大和数对
        while resi_map[resi]:
            first = resi_map[resi].pop(0)
            if resi !=0:
                second = resi_map[averageScore - resi].pop(0)
            else:
                second = resi_map[resi].pop(0)

            if second > first:
                first, second = second, first

            two_sum = first+second


            if two_sum not in pairs:
                pair_sum.append(two_sum)
                pairs[two_sum] = [[first, second]]
            else:
                pairs[two_sum].append([first, second])

    # 每个数都配对完毕后开始汇总在res中
    pair_sum.sort()
    while pair_sum:
        max_sum = pair_sum.pop()
        max_sum_pairs = pairs[max_sum]

        if len(max_sum_pairs)>1:
            max_sum_pairs.sort(key=lambda x:x[0],reverse=True)
            for cur_pair in max_sum_pairs:
                res.extend( cur_pair )
        else:
            res.extend(max_sum_pairs[0])
    return res


if __name__ == '__main__':
    # a = []
    b = [1,2,3]
    # a.extend(b)
    # print(a)
    out = ''
    for num in b[:-1]:
        out += str(num) + ' '

    print(out + f'{b[-1]}')




