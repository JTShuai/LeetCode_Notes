'''
题目描述:
给你一个整数数组 nums 和一个整数 target 。

向数组中的每个整数前添加 '+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ：

例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。
返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。

 

示例 1：
输入：nums = [1,1,1,1,1], target = 3
输出：5
解释：一共有 5 种方法让最终目标和为 3 。
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3

示例 2：
输入：nums = [1], target = 1
输出：1
 

提示：
1 <= nums.length <= 20
0 <= nums[i] <= 1000
0 <= sum(nums[i]) <= 1000
-1000 <= target <= 1000
'''
'''
解题思路:
记数组的元素和为 sum，添加 - 号的元素之和为 neg(neg 为正数，这里和不算负号)，
则其余添加 + 的元素之和为 sum−neg，得到的表达式的结果为： 
    (sum - neg) - neg = sum - 2*neg = target
    neg = (sum - target)/2
由于数组 nums 中的元素都是非负整数，neg 也必须是非负整数，所以上式成立的前提是 sum−target 是非负偶数。
若不符合该条件可直接返回 0。

若上式成立，问题转化成在数组 nums 中选取若干元素，使得这些元素之和等于 neg，
计算选取元素的方案数。我们可以使用动态规划的方法求解。

定义二维数组 dp，其中 dp[i][j] 表示在数组 nums 的前 i 个数中选取元素，使得这些元素之和等于 j 的方案数。
假设数组 nums 的长度为 n，则最终答案为 dp[n][neg]。

'''

from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # 二维数组动态规划
        sum_list = sum(nums)
        if (sum_list - target) < 0 or (sum_list - target) % 2 != 0:
            return 0

        n = len(nums)
        neg = (sum_list - target) // 2
        dp = [[0] * (neg + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        # 开始填表
        for i in range(1, n + 1):
            for j in range(neg + 1):
                if j >= nums[i - 1]:
                    dp[i][j] = dp[i - 1][j - nums[i - 1]] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[n][neg]

    def findTargetSumWays2(self, nums: List[int], target: int) -> int:

        # 压缩为一维数组动态规划
        sum_list = sum(nums)
        if (sum_list - target) < 0 or (sum_list - target) % 2 != 0:
            return 0

        n = len(nums)
        neg = (sum_list - target) // 2
        dp = [1] + [0]*neg
        for i in range(n):
            for j in range(neg, nums[i]-1, -1):
                dp[j] += dp[j - nums[i]]

        return dp[neg]


if __name__ == '__main__':
    sol = Solution()
    nums = [9,7,0,3,9,8,6,5,7,6]
    target = 2
    print(sol.findTargetSumWays2(nums,target))
