'''
题目描述:
如果连续数字之间的差严格地在正数和负数之间交替，则数字序列称为 摆动序列 。
第一个差（如果存在的话）可能是正数或负数。仅有一个元素或者含两个不等元素的序列也视作摆动序列。
    例如， [1, 7, 4, 9, 2, 5] 是一个 摆动序列 ，因为差值 (6, -3, 5, -7, 3) 是正负交替出现的。

    相反，[1, 4, 7, 2, 5] 和 [1, 7, 4, 5, 5] 不是摆动序列，第一个序列是因为它的前两个差值都是正数，
    第二个序列是因为它的最后一个差值为零。
子序列 可以通过从原始序列中删除一些（也可以不删除）元素来获得，剩下的元素保持其原始顺序。

给你一个整数数组 nums ，返回 nums 中作为 摆动序列 的 最长子序列的长度 。


示例 1：
输入：nums = [1,7,4,9,2,5]
输出：6
解释：整个序列均为摆动序列，各元素之间的差值为 (6, -3, 5, -7, 3) 。

示例 2：
输入：nums = [1,17,5,10,13,15,10,5,16,8]
输出：7
解释：这个序列包含几个长度为 7 摆动序列。
其中一个是 [1, 17, 10, 13, 10, 16, 8] ，各元素之间的差值为 (16, -7, 3, -3, 6, -8) 。

示例 3：
输入：nums = [1,2,3,4,5,6,7,8,9]
输出：2
 

提示：
1 <= nums.length <= 1000
0 <= nums[i] <= 1000
'''

'''
解题思路:
方法一：动态规划
每当我们选择一个元素作为摆动序列的一部分时，这个元素要么是上升的，要么是下降的，这取决于前一个元素的大小。
那么列出状态表达式为：
    up[i] 表示以前 i 个元素中的某一个为结尾的最长的「上升摆动序列」的长度。

    down[i] 表示以前 i 个元素中的某一个为结尾的最长的「下降摆动序列」的长度。
以 up[i] 为例:
    1. 当 nums[i]≤nums[i−1] 时，我们无法选出更长的「上升摆动序列」的方案。因为对于任何以 nums[i] 结尾的「上升摆动序列」，
    我们都可以将 nums[i] 替换为 nums[i−1]，使其成为以 nums[i−1] 结尾的「上升摆动序列」。
    2. 当 nums[i]>nums[i−1] 时，我们既可以从 up[i - 1] 进行转移，也可以从 down[i−1] 进行转移。
    下面我们证明从 down[i−1] 转移是必然合法的，即必然存在一个 down[i−1] 对应的最长的「下降摆动序列」的末尾元素小于 nums[i]。
         证明: 如果 down[i-1] 最长序列的最后一个是 nums[j],
         当 nums[j] >= num[i-1], 那么用 nums[i-1] 替换 nums[j]，后面在加上 nums[i]，上升序列增加1，
         如果 nums[j] < nums[i-1],同样的拼到 nums[j] 后面，上升序列增加1.


方法二：贪心算法

'''
from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n

        up = [1] + [0] * (n-1)
        down = [1] + [0] * (n-1)

        for i in range(1,n):
            if nums[i] > nums[i - 1]:
                up[i] = max( up[i-1], down[i-1] + 1 )
                down[i] = down[i-1]
            elif nums[i] < nums[i - 1]:
                down[i] = max(down[i-1], up[i-1] + 1)
                up[i] = up[i -1]
            else:
                down[i] = down[i-1]
                up[i] = up[i - 1]

        return max(down[n-1], up[n-1])

    def wiggleMaxLength2(self,nums):
        # 优化过的动态规划, 只维护两个变量

        n = len(nums)
        if n < 2:
            return n

        up = down = 1
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                up = max(up, down + 1)
            elif nums[i] < nums[i - 1]:
                down = max(up + 1, down)

        return max(up, down)

    def wiggleMaxLength3(self, nums):
        # 贪心算法
        n = len(nums)
        if n < 2:
            return n

        prevdiff = nums[1] - nums[0]
        ret = (2 if prevdiff != 0 else 1)

        for i in range(2, n):
            diff = nums[i] - nums[i - 1]
            if (diff > 0 and prevdiff <= 0) or (diff < 0 and prevdiff >= 0):
                ret += 1
                prevdiff = diff

        return ret




















