'''
题目描述:
给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。

你可以对一个单词进行如下三种操作：
    插入一个字符
    删除一个字符
    替换一个字符
'''
'''
解题思路:
对于字符串A和B来说，为了使它们相等：
对 A 插入一个字符 等价于 对 B 删除一个字符，反之亦然。
而对 A 替换一个字符 等价于 对 B 替换一个字符

而对两个字符串来说，如果已知当前的转换次数 m ，此时其中增加一个char时，
需要的总最少操作数最多为 m+1 (增添或删除操作)。

dp[i][j]: A 的 前 i 个字符与 B 的前 j 个字符转换为相同需要的最少操作次数
因此当 
    A[i]==B[j]时，dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]+1, dp[i][j-1]+1)
    A[i]!=B[j]时，dp[i][j] = min(dp[i-1][j-1]+1, dp[i-1][j]+1, dp[i][j-1]+1)
'''

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        if not word1 or not word2:
            return max(m, n)

        dp = [[0]*(n+1) for _ in range(m+1)]

        # 初始化空字符串的情况（i=0或j=0）dp[0][j] = j, dp[i][0] = i
        for i in range(1, m+1):
            dp[i][0] = i
            for j in range(1, n+1):
                if dp[0][j] == 0:
                    dp[0][j] = j

                if word1[i-1] == word2[j-1]:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]+1, dp[i][j-1]+1)
                else:
                    dp[i][j] = min(dp[i-1][j-1]+1, dp[i-1][j]+1, dp[i][j-1]+1)

        return dp[m][n]

if __name__ == '__main__':
    s = Solution()
    w1 = ''
    w2 = 'a'
    s.minDistance(w1,w2)