from typing import List


class Solution:
    def findK(self, nums:List, k:int) -> int:
        if not nums:
            return 0

        n = len(nums)

        dp = [[0]*(1+k) for _ in range(n+1)]

        for i in range(1, n+1):
            cur_num = nums[i-1]
            for j in range(1,k+1):
                if cur_num > j:
                    dp[i][j] = dp[i-1][j]
                elif cur_num == j:
                    dp[i][j] = dp[i-1][j] + 1
                else:
                    dp[i][j] = dp[i-1][j//cur_num] + 1

        return dp[n][k]

    def findK2(self, nums:List, k:int) -> int:
        if not nums:
            return 0

        ans = 0
        n = len(nums)
        for i in range(n):
            if nums[i] <= k:
                ans +=1
                base = nums[i]
                for j in range(i+1,n):
                    if base*nums[j] <= k:
                        ans +=1
                        base *= nums[j]
                    else:
                        break

        return ans




if __name__ == '__main__':
    s = Solution()
    nums = [2,3,4]
    k = 100
    print(s.findK2(nums,k))