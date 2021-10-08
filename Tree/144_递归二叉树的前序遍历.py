'''
题目描述:
给你二叉树的根节点 root ，返回它节点值的 前序 遍历。
'''


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        self.res = []

        def dfs(root):
            if not root:
                return

            self.res.append(root.val)

            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return self.res