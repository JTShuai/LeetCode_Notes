'''
问题描述:
给你一个整数数组 nums ，找到其中最长严格递增 子序列 的长度。
子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。
例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。

示例 1：
输入：nums = [10,9,2,5,3,7,101,18]
输出：4
解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。

示例 2：
输入：nums = [0,1,0,3,2,3]
输出：4

示例 3：
输入：nums = [7,7,7,7,7,7,7]
输出：1
 

提示：
1 <= nums.length <= 2500
-104 <= nums[i] <= 104
 

进阶：
你可以设计时间复杂度为 O(n^2) 的解决方案吗？
你能将算法的时间复杂度降低到 O(n log(n)) 吗?
'''

'''
解题思路:
方法一：动态规划
dp[i]表示 i 位置数字，与前面的所有数字所能构造的最长升序排列的长度
dp[i] = max(dp[j]) + 1, 其中 0<=j<i 且 num[j] < num[i]
最后返回最大值

方法二：贪心 + 二分查找
如果我们要使上升子序列尽可能的长，则我们需要让序列上升得尽可能慢，因此我们希望每次在上升子序列最后加上的那个数尽可能的小。

基于上面的贪心思路，我们维护一个数组 d[i]，表示长度为 i 的最长上升子序列的末尾元素的最小值，
用 len 记录目前最长上升子序列的长度，起始时 len 为 1，d[1] = nums[0]。且 d[i] 是关于 i 单调递增的。

我们依次遍历数组 nums 中的每个元素，并更新数组 d 和 len 的值。如果 nums[i]>d[len] 则更新 len =len+1，
否则在 d[1…len] 中找满足 d[i−1]<nums[j]<d[i] 的下标 i，并更新 d[i]=nums[j]。

根据 d 数组的单调性，我们可以使用二分查找寻找下标 i，优化时间复杂度。
'''
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * (n+1)
        for i in range(2, n+1):
            for j in range(1,i):
                if nums[i-1] > nums[j-1]:
                    dp[i] = max(dp[j] + 1, dp[i])

        return max(dp)

    def lengthOfLIS2(self, nums: List[int]) -> int:
        # 方法二
        d = []
        for n in nums:
            if not d or n > d[-1]:
                d.append(n)

            else:
                l, r = 0, len(d) - 1
                loc = r
                while l <= r:
                    mid = (l + r) // 2
                    if d[mid] >= n:
                        loc = mid
                        r = mid - 1
                    else:
                        l = mid + 1
                d[loc] = n
        return len(d)

        # n = len(nums)
        # if n == 1:
        #     return 1
        # dp = [1] * (n + 1)
        # k = 1
        # local_max = - float('inf')
        # max_k = 1
        # max_k_map = {}
        #
        # for i in range(2, n + 1):
        #     if nums[i - 1] == nums[i - 2]:
        #         dp[i] = dp[i - 1]
        #
        #     if nums[i - 1] < nums[i - 2]:
        #         if max_k_map and nums[i-1] > max_k_map[max_k]:
        #
        #             if max_k+1>k:
        #                 max_k += 1
        #                 k = max_k
        #                 max_k_map = {max_k:nums[i-1]}
        #
        #         # 虽然当前数字没有之前max_k记录的大，但是此时k已经超过了max_k
        #         if k > max_k:
        #             max_k_map = {k: nums[i - 2]}
        #             max_k = k
        #
        #         dp[i] = max( k ,dp[i - 1])
        #
        #         k = 1
        #
        #
        #     if nums[i - 1] > nums[i - 2]:
        #         if nums[i - 1] > local_max:
        #             local_max = nums[i - 1]
        #             dp[i] = dp[i - 1] + 1
        #
        #         else:
        #
        #             '''
        #             1.1 k+1 > max_k: dp[i] = max(dp[i-1], k+1), k +=1 -> max_k = k, max_k_map = {max_k: num(i)}
        #             1.2 k+1 < max_k and nums(i)> max_k_map[max_k]: dp[i]= max(dp[i-1], max_k+1), 更新
        #             '''
        #             k += 1
        #             if k > max_k:
        #                 dp[i] = max(dp[i - 1], k)
        #                 max_k = k
        #                 max_k_map = {max_k:nums[i-1]}
        #             elif k < max_k and nums[i-1] > max_k_map[max_k]:
        #                 dp[i] = max(dp[i-1], max_k+1)
        #                 max_k += 1
        #                 max_k_map = {max_k, nums[]}


if __name__ == '__main__':
    sol = Solution()
    nums = [10,9,2,5,3,7,101,18]
    print(sol.lengthOfLIS(nums))
