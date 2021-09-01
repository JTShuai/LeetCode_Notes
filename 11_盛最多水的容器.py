from typing import List

'''
题目描述：
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器。

e.g.,:
输入：[1,8,6,2,5,4,8,3,7]
输出：49 
解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。

示例 2：
输入：height = [1,1]
输出：1

示例 3：
输入：height = [4,3,2,1,4]
输出：16

示例 4：
输入：height = [1,2,1]
输出：2
'''

'''
解题思路：
由于装水的多少，取决于短板的高度与两板之间的距离

左右两指针从两端出发，将较低的那块板子往中间移动
(1. 如果移动长板，则装的水只能减小不能增大，因为两板距离减小，而且最低板高只会更小或者不变，导致装的水只会减小
2. 如果移动短板，则装的水有可能增加
)

'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 左右指针
        left = 0
        right = len(height) - 1
        max_area = 0

        while(left<right):
            valid_height = min(height[left], height[right])
            cur_area = valid_height * (right-left)
            max_area = max(cur_area,max_area)

            if height[left]<=height[right]:
                left +=1
            else:
                right -=1


        return max_area

if __name__ == '__main__':
    print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))