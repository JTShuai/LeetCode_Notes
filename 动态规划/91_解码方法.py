'''
题目描述:
一条包含字母 A-Z 的消息通过以下映射进行了 编码 ：
'A' -> 1
'B' -> 2
...
'Z' -> 26

要 解码 已编码的消息，所有数字必须基于上述映射的方法，反向映射回字母（可能有多种方法）。
例如，"11106" 可以映射为：
"AAJF" ，将消息分组为 (1 1 10 6)
"KJF" ，将消息分组为 (11 10 6)
注意，消息不能分组为  (1 11 06) ，因为 "06" 不能映射为 "F" ，这是由于 "6" 和 "06" 在映射中并不等价。

给你一个只含数字的 非空 字符串 s ，请计算并返回 解码 方法的 总数 。

题目数据保证答案肯定是一个 32 位 的整数。

提示：
1 <= s.length <= 100
s 只包含数字，并且可能包含前导零。
'''
'''
解题思路:
dp[i] 代表 前i个字母解码的种类数量
s[i] 不为 0：
    1. s[i-1,i] <=26，且 s[i-1]不为0, dp[i] = dp[i-2] + dp[i-1]
    2. else: dp[i] = dp[i-1]
s[i]为0：
    1. s[i-1] 不为零，且小于3， dp[i] = dp[i-2]
    2. else: return 0
边界条件:
    1. 字符串'0' 开头, return 0
    2. dp[0] = 1
'''


class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        n = len(s)
        dp = [0]* (n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            if s[i-1] != '0':
                if s[i-2] != '0' and int(s[i-2:i])<=26:
                    dp[i] = dp[i - 1] + dp[i-2]
                else:
                    dp[i] = dp[i-1]

            else:
                if s[i-2] != '0' and int(s[i-2:i])<=26:
                    dp[i] = dp[i - 2]
                else:
                    return 0

        return dp[n]

if __name__ == '__main__':
    sol = Solution()
    print(sol.numDecodings('2101'))