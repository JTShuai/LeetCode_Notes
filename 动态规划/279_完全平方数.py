'''
题目描述:

给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。
给你一个整数 n ，返回和为 n 的完全平方数的 最少数量 。

完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。
例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。


示例 1：
输入：n = 12
输出：3
解释：12 = 4 + 4 + 4

示例 2：
输入：n = 13
输出：2
解释：13 = 4 + 9

提示：
1 <= n <= 104
'''
from math import sqrt

'''
解题思路:
要让组合的平方数个数最少，则要使每个平方数尽量大
方法一：动态规划

e.g.,
dp[12] = min(dp[4]+dp[8], dp[9]+dp[3])

注意: 计算平方式尽量用 即j*j 而不是 j**2， 前者更快 
'''

class Solution:
    def numSquares(self, n: int) -> int:
        if n < 4:
            return n
        dp = [float('inf')]*(n+1)
        dp[0] = 0
        dp[1] = 1
        dp[3] = 3
        for i in range(4,n+1):
            for j in range(1,i-1):
                if j*j > i: break
                dp[i] = min(dp[i],dp[i - j*j])
            dp[i] +=1

        return dp[n]


    def numSquares2(self, n: int) -> int:
        if n < 4:
            return n
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        dp[3] = 3
        for i in range(4, n + 1):
            max_base = int(i ** 0.5)

            if max_base * max_base == i:
                dp[i] = 1
                continue

            for j in range(1, max_base + 1):
                dp[i] = min(dp[j * j] + dp[i - j * j], dp[i])

        return dp[n]


