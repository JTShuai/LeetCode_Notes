'''
题目描述:
在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。
这个地区只有一个入口，我们称之为“根”。 除了“根”之外，每栋房子有且只有一个“父“房子与之相连。
一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。
如果 两个直接相连 的房子在同一天晚上被打劫，房屋将自动报警。
计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。

示例 1:
输入: [3,2,3,null,3,null,1]

     3*
    / \
   2   3
    \   \
     3*  1*

输出: 7
解释: 小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = 7.

示例 2:
输入: [3,4,5,1,3,null,1]

     3
    / \
   4*  5*
  / \   \
 1   3   1

输出: 9
解释: 小偷一晚能够盗取的最高金额 = 4 + 5 = 9.
'''

'''
解题思路:
动态规划
方法一：
    当前节点能偷到的最大钱为 max(当前节点+4个孙节点, 2个儿节点)，再利用Hashmap避免重复子问题,TreeNode 当做 key，能偷的钱当做 value。
方法二：
    任何一个节点能偷到的最大钱的状态可以定义为:    
        当前节点选择不偷：当前节点能偷到的最大钱数 = 左孩子能偷到的钱 + 右孩子能偷到的钱
        当前节点选择偷：当前节点能偷到的最大钱数 = 左孩子选择自己不偷时能得到的钱 + 右孩子选择不偷时能得到的钱 + 当前节点的钱数
'''
from Tree import TreeNode


class Solution:
    def rob(self, root: TreeNode) -> int:
        # 方法一
        if not root:
            return 0

        self.unordered_map = {}

        def dfs(root):
            if not root:
                return 0
            if root in self.unordered_map: return self.unordered_map[root]

            money = root.val

            if root.left:
                money += dfs(root.left.left) + dfs(root.left.right)
            if root.right:
                money += dfs(root.right.left) + dfs(root.right.right)

            result = max(money, dfs(root.left)+dfs(root.right))
            self.unordered_map[root] = result

            return result

        return dfs(root)

    def rob2(self, root: TreeNode) -> int:
        # 方法二
        # 0 表示不偷当前节点，1 表示偷当前节点

        def dfs(root):
            if not root:
                return [0]*2

            res = [0]*2

            left = dfs(root.left)
            right = dfs(root.right)

            res[0] = max(left[0], left[1]) + max(right[0], right[1])
            res[1] = left[0] + right[0] + root.val

            return res

        res = dfs(root)
        return max(res[0], res[1])


