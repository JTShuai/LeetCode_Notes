'''
题目描述:
给定一个二叉树，找出其最小深度。
最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明：叶子节点是指没有子节点的节点。
'''


'''
解题思路:
dfs遍历+回溯, 先序
'''

from Tree.TreeNode import TreeNode


class Solution:
    def minDepth(self, root: TreeNode) -> int:

        if not root:
            return 0

        self.min_depth = float('inf')

        def dfs(root, depth):
            if not root:
                return

            if not root.left and not root.right:
                self.min_depth = min(self.min_depth, depth+1)


            depth += 1

            dfs(root.left, depth)
            dfs(root.right, depth)


        dfs(root, 0)
        return self.min_depth


    # 更简洁的写法
    def minDepth2(self, root: TreeNode) -> int:

        def dfs(root):
            if not root:
                return 0

            if not root.left and not root.right:
                return 1

            m1 = dfs(root.left)
            m2 = dfs(root.right)

            if not (root.left and root.right):
                # 如果有一个孩节点为空，则m1,m2其中一个为0
                return m1+m2+1

            return min(m1,m2) + 1

        return dfs(root)