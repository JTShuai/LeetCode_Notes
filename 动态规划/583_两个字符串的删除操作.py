'''
题目描述:
给定两个单词 word1 和 word2，找到使得 word1 和 word2 相同所需的最小步数，
每步可以删除任意一个字符串中的一个字符。
'''
'''
解题思路:
转换为求两个字符串的最长公共子序列问题。
ans = m+n -2*dp[m][n]
'''


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        dp = [[0]*(n+1) for _ in range(m+1)]

        for i in range(1,m+1):
            for j in range(1, n+1):

                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return m+n-2*dp[m][n]