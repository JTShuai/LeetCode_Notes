'''
题目描述:
给定一个整数数组 prices，其中第 i 个元素代表了第 i 天的股票价格 ；整数 fee 代表了交易股票的手续费用。

你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。

返回获得利润的最大值。

注意：这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。
'''
'''
解题思路:
类似309题，两种状态 
    0- 当日收盘后持有股票（当日有买入+昨日收盘后手上无股票, 或者昨日有股票）
    1- 当日收盘后无股票（昨日有股票+今日卖出，或者昨日无股票+今日无操作）
注意：手续费仅在完成一笔交易后收取，即在卖出操作的时候，收益需要减去手续费
'''
from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if not prices:
            return 0

        n = len(prices)
        dp = [[0]*2 for _ in range(n)]
        # 第0天买入股票
        dp[0][0] = -prices[0]

        for i in range(1,n):
            # 状态0, 有股票
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] - prices[i])

            # 状态1，没股票
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]+prices[i]-fee)

        return dp[n-1][1]


    def maxProfit2(self, prices: List[int], fee: int) -> int:
        # 状态压缩为一维数组
        if not prices:
            return 0

        dp = [-prices[0], 0]

        for price in prices:
            temp = dp[0]
            dp[0] = max(dp[0], dp[1]-price)

            dp[1] = max(dp[1], temp+price-fee)

        return dp[1]