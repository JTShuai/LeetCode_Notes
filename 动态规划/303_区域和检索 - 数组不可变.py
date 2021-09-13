'''
题目描述:
给定一个整数数组  nums，求出数组从索引 i 到 j（i ≤ j）范围内元素的总和，包含 i、j 两点。

实现 NumArray 类：
NumArray(int[] nums) 使用数组 nums 初始化对象
int sumRange(int i, int j) 返回数组 nums 从索引 i 到 j（i ≤ j）范围内元素的总和，
包含 i、j 两点（也就是 sum(nums[i], nums[i + 1], ... , nums[j])）
'''
from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        cur = 0
        for i in range(left,right+1):
            cur += self.nums[i]
        return cur

    '''
    改进：利用前缀和, 这样调用sumRange时，可以 O(1)
    '''