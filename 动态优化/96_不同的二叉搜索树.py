'''
题目描述:
给你一个整数 n ，求恰由 n 个节点组成且节点值从 1 到 n 互不相同的 二叉搜索树 有多少种？
返回满足题意的二叉搜索树的种数。

'''


class Solution:
    def numTrees(self, n: int) -> int:
        if n == 1:
            return n

        # 动态规划
        dp = [0] * n
        # num=1 -> dp[0]=1
        dp[0] = 1

        for i in range(1, n):
            num = i + 1

            for j in range(num):
                cur_root = j + 1
                left = cur_root - 1
                right = num - cur_root
                left_var = dp[left - 1] if left > 0 else 1
                right_val = dp[right - 1] if right > 0 else 1
                dp[i] += left_var * right_val

        return dp[n - 1]