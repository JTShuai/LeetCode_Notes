'''
题目描述:
如果一个数列 至少有三个元素 ，并且任意两个相邻元素之差相同，则称该数列为等差数列。

例如，[1,3,5,7,9]、[7,7,7,7] 和 [3,-1,-5,-9] 都是等差数列。
给你一个整数数组 nums ，返回数组 nums 中所有为等差数组的 子数组 个数。
子数组 是数组中的一个连续序列。

示例 1：
输入：nums = [1,2,3,4]
输出：3
解释：nums 中有三个子等差数组：[1, 2, 3]、[2, 3, 4] 和 [1,2,3,4] 自身。

示例 2：
输入：nums = [1]
输出：0
 

提示：
1 <= nums.length <= 5000
-1000 <= nums[i] <= 1000
'''

'''
解题思路:
每个数组可以和前面的数字组建等差数列，也可以和后面的数字组成新的等差数列

dp[n] 表示从起始位置到当前位置的所有数字一共可以组成的等差数列个数（可以不包含当前数字）

一个数能与前面的数组成等差数列，则至少和他前面的两个数可以组成等差数列(长度为3)
则: dp[n] = dp[n-1] + self_num[n]
self_num[n] = self_num[n-1] + 1

self_num 表示 当前数字与前序的数字能组成的等差数列个数（必须包含当前数字）

'''

from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0

        dp = [0]*n
        self_num = [0]*n

        for i in range(2,n):
            if nums[i] + nums[i-2] == 2*nums[i-1]:
                self_num[i] = self_num[i-1] + 1

            dp[i] = dp[i-1] + self_num[i]

        return dp[-1]

    '''
    方法二: 最后返回 self_num 的 和
    '''
    def numberOfArithmeticSlices2(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0

        self_num = [0] * n
        cnt = 0

        for i in range(2, n):
            if nums[i] + nums[i - 2] == 2 * nums[i - 1]:
                self_num[i] = self_num[i - 1] + 1
                cnt += self_num[i]

        return cnt