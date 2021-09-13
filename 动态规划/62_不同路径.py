'''
题目描述:
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。

问总共有多少条不同的路径？

提示：
1 <= m, n <= 100
题目数据保证答案小于等于 2 * 109
'''

'''
解题思路:
二维数组dp,每个位置dp[i][j]保存的是从start到(i,j)位置的走法数量
由于机器人只能向右或者向下移动，则
dp[i][j] 要么是从 dp[i-1][j]过来的，要么是从dp[i][j-1]过来的
因此 dp[i][j] = dp[i-1][j] + dp[i][j-1]

当m*n 为向量时，只有一种走法，return 1
且两条边的节点，走法也为1 -> dp数值初始化为1

'''

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m==1 or n ==1:
            return 1

        dp = [[1]*n for _ in range(m)]

        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[-1][-1]