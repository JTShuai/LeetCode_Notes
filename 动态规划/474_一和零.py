'''
题目描述:
给你一个二进制字符串数组 strs 和两个整数 m 和 n 。

请你找出并返回 strs 的最大子集的长度，该子集中 最多 有 m 个 0 和 n 个 1 。

如果 x 的所有元素也是 y 的元素，集合 x 是集合 y 的 子集 。

 

示例 1：
输入：strs = ["10", "0001", "111001", "1", "0"], m = 5, n = 3
输出：4
解释：最多有 5 个 0 和 3 个 1 的最大子集是 {"10","0001","1","0"} ，因此答案是 4 。
其他满足题意但较小的子集包括 {"0001","1"} 和 {"10","1","0"} 。{"111001"} 不满足题意，因为它含 4 个 1 ，大于 n 的值 3 。

示例 2：
输入：strs = ["10", "0", "1"], m = 1, n = 1
输出：2
解释：最大的子集是 {"0", "1"} ，所以答案是 2 。
 

提示：
1 <= strs.length <= 600
1 <= strs[i].length <= 100
strs[i] 仅由 '0' 和 '1' 组成
1 <= m, n <= 100
'''

'''
解题思路:
动态规划 0-1 背包问题

dp[i][j][k] 表示输入字符串在子区间 [0, i] 能够使用 j 个 0 和 k 个 1 的字符串的最大数量。
'''

from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        length = len(strs)

        # 最多 有 m 个 0 和 n 个 1
        dp = [[[0]*(n+1) for _ in range(m+1)] for _ in range(length+1)]

        for i in range(1, length+1):
            cur_one, cur_zero = self.count(strs[i - 1])
            # j 和 k 的遍历要从0开始，因为有些字符串是完全由 '0'或'1'组成的
            for j in range(m+1):
                for k in range(n+1):
                    dp[i][j][k] = dp[i - 1][j][k]
                    if cur_zero <= j and cur_one <= k:
                        dp[i][j][k] = max(dp[i][j][k], 1+dp[i-1][j- cur_zero][k - cur_one])

        return dp[length][m][n]

    def findMaxForm2(self, strs: List[str], m: int, n: int) -> int:
        # 压缩为二维数组
        dp = [[0]*(n+1) for _ in range(m+1)]
        for s in strs:
            cur_one, cur_zero = self.count(s)
            for j in range(m,cur_zero-1, -1):
                for k in range(n, cur_one-1, -1):
                    dp[j][k] = max(dp[j][k], dp[j - cur_zero][k-cur_one] + 1)

        return dp[m][n]

    def count(self,string:str):
        count_one = count_zero = 0
        for s in string:
            if s == '0':
                count_zero +=1
            else:
                count_one +=1

        return count_one, count_zero

if __name__ == '__main__':
    sol = Solution()
    strs = ["11111","100","1101","1101","11000"]
    length = len(strs)
    m = 5
    n = 7
    print(sol.findMaxForm2(strs,m,n))
    # dp = [[[0] * (n + 1) for _ in range(m + 1)] for _ in range(length + 1)]
    #
    # print(dp[1][1])




