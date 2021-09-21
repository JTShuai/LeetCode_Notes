'''
题目描述:
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
'''

'''
解题思路:
最多只有两次交易
则需要有个计数器记录已经发生过几次交易
依然是两个状态：0、1
k = 0,1,2 记录卖过的次数

dp[i][0][k]: 今天收盘后持有股票
    - 昨天无股票 + 交易次数没超过(k<2) + 今天买的(k+=1)
    - 昨天持股票 + 今天没操作
dp[i][1][k]: 今天收盘后无股票
    - 昨天无股票 + 今天没操作
    - 昨天有股票 + 今天卖出了（因为如果昨天能持有股票，则说明当前没超过操作限制次数，这里也就不用再做判断）


更快的方法:
在任意一天结束之后，我们会处于以下五个状态中的一种：
    未进行过任何操作；
    只进行过一次买操作；
    进行了一次买操作和一次卖操作，即完成了一笔交易；
    在完成了一笔交易的前提下，进行了第二次买操作；
    完成了全部两笔交易。
由于第一个状态的利润显然为 0，因此我们可以不用将其记录。
对于剩下的四个状态，我们分别将它们的最大利润记为
buy_1, sell_1, buy_2以及 sell_2。

对于 buy_1 而言，在第 i 天我们可以不进行任何操作，保持不变，也可以在未进行任何操作
的前提下以 prices[i] 的价格买入股票，那么 buy_1 的转移方程为：
    buy_1 = max(buy_1', -prices[i])
    
对于 sell_1 而言，在第 i 天我们可以不进行任何操作，保持不变，也可以在只进行过一次买操作的前提下
以 prices[i] 的价格卖出股票，那转移方程为
    sell_1 = max(sell_1', buy_1' + prices[i])

同理得到 buy_2 和 sell_2 的转移方程:
    buy_2 = max(buy_2', sell_1' - prices[i])
    sell_2 = max(sell_2', buy_2' + prices[i])
'''
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        dp = [[[0]*3 for _ in range(2)] for _ in range(n)]

        # 第0天买入
        dp[0][0][0] = -prices[0]
        # 第0天不可能已经有交易
        dp[0][1][1] = float('-inf')
        dp[0][1][2] = float('-inf')
        dp[0][0][1] = float('-inf')
        dp[0][0][2] = float('-inf')

        for i in range(1, n):

            # 状态0, 持有股票, 昨天买了或者今天买的
            # 当前持有，且没卖过，要么昨天就持有了且没卖过，要么今天之前从来没交易过并且今天买了
            dp[i][0][0] = max(dp[i - 1][0][0], dp[i - 1][1][0] - prices[i])
            # 当前持有，且卖过一次
            dp[i][0][1] = max(dp[i - 1][0][1], dp[i - 1][1][1] - prices[i])
            # 当前持有，且卖过两次：不可能
            dp[i][0][2] = float('-inf')

            # 状态1，不持有股票
            # k=0 表明从来没交易过，收益为0，由于默认值为0，可忽略该项更新
            # k =1 表明收盘后卖过一次，要么是之前就卖过一次了，要么是之前没卖过+今天卖了一次
            dp[i][1][1] = max(dp[i - 1][1][1], dp[i - 1][0][0] + prices[i])
            # k = 2 表明收盘后卖过两次，要么是之前就卖过两次了，要么是之前卖过一次+今天卖了一次
            dp[i][1][2] = max(dp[i - 1][1][2], dp[i - 1][0][1] + prices[i])


        return max(dp[n-1][1][1], dp[n-1][1][2])

    def maxProfit2(self, prices: List[int]) -> int:
        # 状态压缩
        n = len(prices)
        # buy_2 即为在同一天买入并且卖出后再以 prices[0] 的价格买入股票
        buy1 = buy2 = -prices[0]
        sell1 = sell2 = 0

        for price in prices[1:]:
            buy1 = max(buy1, -price)
            sell1 = max(sell1, buy1 + price)

            buy2 = max(buy2, sell1 - price)
            sell2 = max(sell2, buy2 + price)

        return max(sell1,sell2,0)
if __name__ == '__main__':
    s = Solution()
    prices = [1,2,3,4,5]
    print(s.maxProfit(prices))