'''
题目描述：
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
'''

'''
解题思路:
对于每一个位置 i 来说，其能接的水量取决于 左右的短板高度 与 当前高度 的差
cap = min(left_high, right_high) - h[i]
然后累加 每个位置的 cap 得到最后的结果

方法一：
动态规划
先正反遍历两边数组，得到 左边的最大值和右边的最大值
l[i]: 前 i 个整数的的最大值
r[i]: i 到 n 中整数的最大值
然后再遍历一次做累加运算

方法二:
左右指针
左右指针从两测出发，分别表示左边的最大值和右边的最大值，短的那个向中间移动
'''
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # 方法一
        if not height:
            return 0
        n = len(height)
        l = [0]*n
        r = [0]*n

        # 正序遍历得到左边高度
        for i in range(n):
            h = height[i]
            if i == 0:
                l[i] = h
                continue

            l[i] = max(h,l[i-1])

        # 逆序遍历得到右边高度
        for j in range(n-1,-1,-1):
            h = height[j]
            if j == n-1:
                r[j] = h
                continue
            r[j] = max(r[j+1],h)

        # 最后一次遍历得到所有积水
        ans = 0
        for i in range(1,n-1):
            h = height[i]
            l_h = l[i]
            r_h = r[i]
            ans += min(l_h,r_h) - h
        return ans

    def trap2(self, height: List[int]) -> int:
        # 方法二

        if not height:
            return 0

        n = len(height)
        ans = 0
        l = 0
        r = n-1
        max_l = height[0]
        max_r = height[-1]

        while l < r:
            if max_l < max_r:
                # 左边是短板，计算左边的
                ans += max_l - height[l]
                l += 1
                max_l = max(max_l, height[l])
            else:
                # 右边是短板，计算右边的
                ans += max_r - height[r]
                r -= 1
                max_r = max(max_r, height[r])

        return ans

