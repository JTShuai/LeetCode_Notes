'''
题目描述:
计算给定二叉树的所有左叶子之和。

示例：

    3
   / \
  9  20
    /  \
   15   7

在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24
'''
from Tree.TreeNode import TreeNode


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.left_val = 0

        def dfs(root, left_val):
            if not root:
                return

            if root.left and not root.left.left and not root.left.right:
                self.left_val += root.left.val

            dfs(root.left, self.left_val)
            dfs(root.right, self.left_val)

        dfs(root, self.left_val)

        return self.left_val