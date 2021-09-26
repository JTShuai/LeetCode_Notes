'''
整形数组： 数字可能为负
返回最大连续子序列和
'''
'''
动态规划：
dp[i] = 前 i 个
'''
from typing import List


def task(nums:List) -> int:
    n = len(nums)

    ans = 0
    for i in range(n):
        base = nums[i]
        for j in range(i+1,n):
            if nums[j]<0:
                break
            else:
                base += nums[j]
        ans = max(ans, base)

    return ans



if __name__ == '__main__':
    nums = [1,2,3,-1,4]
    print(task(nums))