'''
题目描述:
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
'''
'''
解题思路:
动态规划
f[i] = max(f[i-1]+nums[i], nums[i])


分治
对于一个区间 [l,r]，我们取 m = (l+r)/2，对区间 [l,m] 和 [m+1,r] 分治求解。
当递归逐层深入直到区间长度缩小为 1 的时候，递归「开始回升」。
这个时候我们考虑如何通过 [l,m] 区间的信息和 [m+1,r] 区间的信息合并成区间 [l,r] 的信息。
最关键的两个问题是：
    我们要维护区间的哪些信息呢？
    我们如何合并这些信息呢？
对于一个区间 [l, r]，我们可以维护四个量:
    lSum 表示 [l,r] 内以 l 为左端点的最大子段和
    rSum 表示 [l,r] 内以 r 为右端点的最大子段和
    mSum 表示 [l,r] 内的最大子段和
    iSum 表示 [l,r] 的区间和


以下简称 [l,m] 为 [l,r] 的「左子区间」，[m+1,r] 为 [l,r] 的「右子区间」。我们考虑如何维护这些量呢
（如何通过左右子区间的信息合并得到 [l,r] 的信息）？
对于长度为 1 的区间 [i,i]，四个量的值都和 nums[i] 相等。对于长度大于 1 的区间：
    首先最好维护的是 iSum，区间 [l,r] 的 iSum 就等于「左子区间」的 iSum 加上「右子区间」的 iSum。
    
    对于 [l,r] 的 lSum，存在两种可能，它要么等于「左子区间」的 lSum，要么等于「左子区间」的 iSum 加上「右子区间」的 lSum，二者取大。
    
    对于 [l,r] 的 rSum，同理，它要么等于「右子区间」的 rSum，要么等于「右子区间」的 iSum 加上「左子区间」的 rSum，二者取大。
    
    当计算好上面的三个量之后，就很好计算 [l,r] 的 mSum 了。我们可以考虑 [l,r] 的 mSum 对应的区间是否跨越 m——
    它可能不跨越 m，也就是说 [l,r] 的 mSum 可能是「左子区间」的 mSum 和 「右子区间」的 mSum 中的一个；
    它也可能跨越 m，可能是「左子区间」的 rSum 和 「右子区间」的 lSum 求和。三者取大。

'''

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        n = len(nums)
        dp = [0]*n
        dp[0] = nums[0]
        ans = nums[0]
        for i in range(1,n):
            dp[i] = max(nums[i],nums[i]+dp[i-1])
            ans = max(ans,dp[i])

        return ans

    def maxSubArray2(self, nums: List[int]) -> int:
        # 优化版
        pre = nums[0]
        ans = nums[0]
        for num in nums[1:]:
            pre = max(num, pre+num)
            ans = max(ans, pre)

        return ans

    def maxSubArray3(self, nums: List[int]) -> int:
        # 分治
        class wtevTree:  # 线段树
            lSum = 0  # 以左区间为端点的最大子段和
            rSum = 0  # 以右区间为端点的最大子段和
            iSum = 0  # 区间所有数的和
            mSum = 0  # 该区间的最大子段和

            def __init__(self, l, r, i, m):  # 构造函数
                self.lSum = l
                self.rSum = r
                self.iSum = i
                self.mSum = m

                # 通过既有的属性,计算上一层的属性,一步步往上返回,获得线段树

        def pushUp(self, leftT: wtevTree, rightT: wtevTree) -> wtevTree:
            # 新子段的lSum等于左区间的lSum或者左区间的 区间和 加上右区间的lSum
            l = max(leftT.lSum, leftT.iSum + rightT.lSum)
            # 新子段的rSum等于右区间的rSum或者右区间的 区间和 加上左区间的rSum
            r = max(leftT.rSum + rightT.iSum, rightT.rSum)
            # 新子段的区间和等于左右区间的区间和之和
            i = leftT.iSum + rightT.iSum
            # 新子段的最大子段和,其子段有可能穿过左右区间,或左区间,或右区间
            m = max(leftT.rSum + rightT.lSum, max(leftT.mSum, rightT.mSum))
            return wtevTree(l, r, i, m)

        # 递归建立和获得输入区间所有子段的结构
        def getInfo(self, nums: List[int], left: int, right: int) -> wtevTree:
            if (left == right):  # 若区间长度为1,其四个子段均为其值
                return wtevTree(nums[left], nums[left], nums[left], nums[left])
            mid = (left + right) >> 1  # 获得中间点mid,右移一位相当于除以2,运算更快
            leftT = getInfo(self, nums, left, mid)
            rightT = getInfo(self, nums, mid + 1, right)  # mid+1,左右区间没有交集。
            return pushUp(self, leftT, rightT)  # 递归结束后,做最后一次合并

        if (not nums or len(nums) <= 0):  # 输入校验
            return 0
        lens = len(nums)  # 获取输入长度

        return getInfo(self, nums, 0, lens - 1).mSum