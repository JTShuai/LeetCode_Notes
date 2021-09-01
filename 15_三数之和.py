from typing import List

'''
题目描述:
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。
注意：答案中不可以包含重复的三元组。

示例 1：
输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]

示例 2：
输入：nums = []
输出：[]

示例 3：
输入：nums = [0]
输出：[]
 

提示：
0 <= nums.length <= 3000
-105 <= nums[i] <= 105
'''


'''
解题思路：
**双指针**
1. 先将数组重新排序为升序
2. 开始遍历数组中的数字，每一次遍历时都再在剩余的数字里面进行双指针搜索
3. 当nums[i]>0时， 遍历结束，因为之后的数字都大于0，因此不可能相加为零了
'''


def threeSum(nums: List[int]) -> List[List[int]]:
    if len(nums) < 3 or not nums:
        return []

    nums.sort()
    res = []
    n = len(nums)

    for i in range(n):
        if nums[i]>0:
            break
        # 去除重复的开始
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        L = i+1
        R = n-1

        # 双指针搜索
        while L < R:
            if nums[i] + nums[L] + nums[R] == 0:
                # 找到了一个答案
                res.append([nums[i], nums[L],nums[R]])
                # 更新指针前应当先判断重复性
                while L<R and nums[L+1] == nums[L]:
                    L +=1
                while L<R and nums[R-1] == nums[R]:
                    R -=1
                L +=1
                R -=1
            elif nums[i] + nums[L] + nums[R] > 0:
                # 说明右边正数太大了，需要更新右指针
                R -=1
            else:
                L +=1

    return res

if __name__ == '__main__':
    print(threeSum([-1,0,1,2,-1,-4]))