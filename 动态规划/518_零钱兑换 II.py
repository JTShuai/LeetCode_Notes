'''
题目描述:
给你一个整数数组 coins 表示不同面额的硬币，另给一个整数 amount 表示总金额。

请你计算并返回可以凑成总金额的硬币组合数。如果任何硬币组合都无法凑出总金额，返回 0 。

假设每一种面额的硬币有无限个。 

题目数据保证结果符合 32 位带符号整数。
'''

'''
解题思路:
动态规划，背包问题
dp[i][j]: 前 i 个硬币 凑成面额为 j 的组合方式总数

转移方程:
    # 总数等于 考虑当前硬币的组合方式 + 不考虑当前硬币的组合方式
    dp[i][j] = dp[i-1][j] + dp[i][j-coin[i]]
'''
from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[1]+[0]*(amount) for _ in range(n+1)]

        for i in range(1,n+1):
            for j in range(1, amount+1):
                dp[i][j] = dp[i-1][j]
                if j >= coins[i-1]:
                    dp[i][j] += dp[i][j - coins[i-1]]

        return dp[n][amount]

    def change2(self, amount: int, coins: List[int]) -> int:
        # 压缩为一维数组
        n = len(coins)
        dp = [0] * (amount+1)
        dp[0] = 1

        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] += dp[i-coin]

        return dp[amount]



if __name__ == '__main__':
    s = Solution()
    amount = 5
    coins = [1,2,5]
    print(s.change2(amount,coins))