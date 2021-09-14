'''
解题思路:
给出 n 个数对。 在每一个数对中，第一个数字总是比第二个数字小。

现在，我们定义一种跟随关系，当且仅当 b < c 时，数对(c, d) 才可以跟在 (a, b) 后面。
我们用这种形式来构造一个数对链。

给定一个数对集合，找出能够形成的最长数对链的长度。你不需要用到所有的数对，
你可以以任何顺序选择其中的一些数对来构造。



示例：
输入：[[1,2], [2,3], [3,4]]
输出：2
解释：最长的数对链是 [1,2] -> [3,4]
 

提示：
给出数对的个数在 [1, 1000] 范围内。
'''

'''
解题思路:
每一个当前数对的第一个数字，寻找与之前数对能够形成的最长数对链
dp[i]表示当前数字能和前面所组成的最长链长度
dp[i] = dp[i-1] + 1 , if paris[i][0] > paris[i-1][1]

方法二:
贪心算法
在所有可作为下一个数对的集合中选择第二个数最小的数对添加到数对链。
根据思路中的描述，按照数对第二个数的升序序列遍历所有数对，如果当前数对可以加入链，则加入。
'''
from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[-1])
        n = len(pairs)
        dp = [0]*(n+1)
        dp[1] = 1
        for i in range(2,n+1):
            for j in range(1,i):
                if pairs[i-1][0] > pairs[j-1][-1]:
                    dp[i] = max(dp[j]+1, dp[i])
                elif pairs[i-1][0] < pairs[j-1][-1]:
                    break

        return max(dp)

    def findLongestChain2(self, pairs: List[List[int]]) -> int:
        # 方法二
        # 贪心算法：可作为下一个数对的集合中选择第二个数最小的数对添加到数对链。
        pairs.sort(key=lambda x: x[-1])
        n = len(pairs)
        d = [pairs[0]]
        for i in range(2, n + 1):
            cur_pair = pairs[i-1]
            if cur_pair[0] > d[-1][-1]:
                d.append(cur_pair)
            else:
                # 寻找替换目标: 按第一个元素寻找位置
                l, r = 0, len(d)-1
                loc = r
                while l <= r:
                    mid = (l+r)//2
                    if d[mid][1] >= cur_pair[0]:
                        loc = mid
                        r = mid - 1
                    else:
                        l = mid + 1

                # 然后比较第二个元素大小判断是否替换
                if cur_pair[1] < d[loc][1]:
                    d[loc] = cur_pair

        return len(d)

if __name__ == '__main__':
    pairs = [[1,2],[2,5],[3,4],[-1,0]]
    sol = Solution()
    print(sol.findLongestChain2(pairs))