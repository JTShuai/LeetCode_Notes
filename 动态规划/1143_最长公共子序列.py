'''
题目描述:
给定两个字符串 text1 和 text2，返回这两个字符串的最长 公共子序列 的长度。如果不存在 公共子序列 ，返回 0 。

一个字符串的 子序列 是指这样一个新的字符串：
它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。

例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。
两个字符串的 公共子序列 是这两个字符串所共同拥有的子序列。


示例 1：
输入：text1 = "abcde", text2 = "ace"
输出：3
解释：最长公共子序列是 "ace" ，它的长度为 3 。

示例 2：
输入：text1 = "abc", text2 = "abc"
输出：3
解释：最长公共子序列是 "abc" ，它的长度为 3 。

示例 3：
输入：text1 = "abc", text2 = "def"
输出：0
解释：两个字符串没有公共子序列，返回 0 。


提示：
1 <= text1.length, text2.length <= 1000
text1 和 text2 仅由小写英文字符组成
'''
'''
解题思路:
方法一：动态规划
ls: 长度较长的字符串， ss: 长度较短的字符串
dp[i][j] : 表示 ls 前 i 个字符能与 ss 前 j 个字符 构成的最长公共子序列

if ls[i] = ss[j]:
    dp[i][j] = dp[i-1][j-1] + 1
else:
    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

动态规划也是有套路的：
    单个数组或者字符串要用动态规划时，可以把动态规划 dp[i] 定义为 nums[0:i] 中想要求的结果；
    当两个数组或者字符串要用动态规划时，可以把动态规划定义成两维的 dp[i][j] ，
    其含义是在 A[0:i] 与 B[0:j] 之间匹配得到的想要的结果。


'''

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        if n ==1 and m==1:
            return 1 if text1==text2 else 0

        dp = [[0]*(n+1) for _ in range(m+1)]

        for i in range(1,m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[m][n]

if __name__ == '__main__':
    sol = Solution()
    s1 = "abcde"
    s2 = 'afce'
    print(sol.longestCommonSubsequence(s1,s2))