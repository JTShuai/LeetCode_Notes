'''
题目描述:
给你一个由 不同 整数组成的数组 nums ，和一个目标整数 target 。
请你从 nums 中找出并返回总和为 target 的元素组合的个数。

题目数据保证答案符合 32 位整数范围。
'''

'''
解题思路:
组合问题需考虑元素之间的顺序，需将target放在外循环，将nums放在内循环。

'''
from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0

        dp = [0]*(target + 1)
        dp[0] = 1
        for i in range(1, target+1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i-num]

        return dp[target]