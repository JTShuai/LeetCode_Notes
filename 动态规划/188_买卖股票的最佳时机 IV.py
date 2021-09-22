'''
问题描述:
给定一个整数数组 prices ，它的第 i 个元素 prices[i] 是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
'''
'''
解题思路:
dp[i][k][0/1]
0: 持有股票
1： 不持股票

k: 0,1,2,..,k.  已经卖出了k 次
'''
from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)

        dp = [ [[0]*2 for _ in range(k+1)] for _ in range(n)]

        # 第0天
        for j in range(k):
            dp[0][j][0] = -prices[0]
        dp[0][k][0] = float('-inf')

        for i in range(1,n):

            for j in range(k):
                # 更新状态 0：当日收盘后持有股票
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1]-prices[i])
                # 更新状态1：当日收盘后不持有股票
                dp[i][j][1] = max(dp[i-1][j-1][0]+prices[i], dp[i-1][j][1])

            # 补充 k 次卖出
            dp[i][k][1] = max(dp[i-1][k-1][0]+prices[i], dp[i-1][k][1])
            dp[i][k][0] = float('-inf')

        ans = 0
        for j in range(1,k+1):
            ans = max(ans, dp[n-1][j][1])

        return ans

    def maxProfit2(self, k: int, prices: List[int]) -> int:
        # 状态压缩
        if not prices:
            return 0

        # 创建 2个 k长度的列表，分别表示 (k-1) 次 buy, sell 操作
        buy = [0] + [-prices[0]]* k
        sell = [0] * (k+1)

        for price in prices[1:]:
            for j in range(1,k+1):
                buy[j] = max(buy[j], sell[j-1] - price )

                sell[j] = max(buy[j]+price, sell[j])

        return max(sell)


