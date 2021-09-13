'''
问题描述:
给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

提示：

m == grid.length
n == grid[i].length
1 <= m, n <= 200
0 <= grid[i][j] <= 100
'''

'''
解题思路:
dp为二维数组，
dp[i][j]指从左上角到 (i,j)位置的最小路径
则 dp[i][j] = nums[i][j] + min(dp[i][j-1],dp[i-1][j])
最后return dp[m][n]
'''
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        if n==1 and m==1:
            return grid[0][0]

        dp = [[101]* (n) for _ in range(m)]
        dp[0][0] = grid[0][0]

        # 先确定两条边界
        if n>1:
            for j in range(1,n):
                dp[0][j] = grid[0][j] + dp[0][j-1]
        if m==1:
            return dp[0][n-1]

        for i in range(1,m):
            dp[i][0] = grid[i][0] + dp[i-1][0]
        if n == 1:
            return dp[m-1][0]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = grid[i][j] + min(dp[i][j-1],dp[i-1][j])


        return dp[m-1][n-1]




if __name__ == '__main__':
    grid = [[1,2] for _ in range(3)]
    print(len(grid))