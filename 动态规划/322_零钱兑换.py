'''
题目描述：
给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。

计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。

你可以认为每种硬币的数量是无限的。
'''
'''
动态规划
dp[j],当目标金额是j时，至少需要dp[j]个硬币组成
每当选择一个硬币coins[i]的时候，总金额都会减少,只需要求dp[j−coins[i]]的值就可以了，如此往复递归


'''


from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return amount
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount+1):
                dp[x] = min(dp[x], dp[x-coin]+1)

        return dp[amount] if dp[amount]!= float('inf') else -1

    def coinChange2(self, coins: List[int], amount: int) -> int:
        # 二维数组
        '''
        完全不使用当前的硬币coins[i]的情况下最少硬币数量,即dp[i-1][j-0*coins[i]]+0
        使用1个当前的硬币coins[i]的情况下最少硬币数量,  即dp[i-1][j-1*coins[i]]+1
        使用2个当前的硬币coins[i]的情况下最少硬币数量,  即dp[i-1][j-2*coins[i]]+2
        ...
        使用k个当前的硬币coins[i]的情况下最少硬币数量,  即dp[i-1][j-k*coins[i]]+k,要求j-k*coins[i]≥0
        '''
        n = len(coins)
        # 第一列都是0（目标金额为0，即不选）
        dp = [ [0] + [float('inf')] * amount for _ in range(n+1)]

        # 初始化第一行
        for j in range(1,amount+1):
            if j-coins[0] >= 0 and j % coins[0] == 0:
                dp[0][j] = dp[0][j-coins[0]] + 1

        # 开始遍历填表
        for i in range(1,n+1):
            for j in range(1,amount+1):
                temp = float('inf')
                if j - coins[i-1] >=0 and dp[i][j-coins[i-1]] != float('inf'):
                    temp = dp[i][j-coins[i-1]] + 1

                dp[i][j] = min(temp, dp[i-1][j])

        return dp[n][amount] if dp[n][amount] != float('inf') else -1

    def coinChange3(self, coins: List[int], amount: int) -> int:
        if not amount:
            return amount
        coins.sort()
        n = len(coins)
        dp = [ [0] + [float('inf')] * amount for _ in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, amount+1):
                if coins[i-1] == j:
                    dp[i][j] = 1
                elif coins[i-1] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    # coin < j
                    # if j % coins[i-1] == 0:
                    #     dp[i][j] = dp[i-1][]
                    '''因为是不限数量，所以这里是 dp[i][j-coins[i-1] 而不是 dp[i-1][j-coins[i-1]'''
                    dp[i][j] = min(dp[i-1][j], 1+ dp[i][j - coins[i-1]])
                    # m = 0
                    # target = j
                    # for k in range(i-1, -1,-1):
                    #     m += target // coins[k]
                    #     target = target % coins[k]
                    #     if target == 0:
                    #         break
                    # if target != 0:
                    #     dp[i][j] = -1
                    # else:
                    #     dp[i][j] = m

        return dp[n][amount] if dp[n][amount] != float('inf') else -1

if __name__ == '__main__':
    s = Solution()
    coins = [186,419,83,408]
    amount = 6249
    print(s.coinChange3(coins,amount))