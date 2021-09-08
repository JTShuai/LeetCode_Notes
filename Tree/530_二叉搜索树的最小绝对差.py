from Tree.TreeNode import TreeNode


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        # 中序遍历，记录上一个值
        self.min_diff = float('inf')
        self.pre = None

        def dfs(root):
            if not root:
                return

            dfs(root.left)

            if self.pre is None:
                self.pre = root.val
            else:
                self.min_diff = min( self.min_diff, root.val - self.pre)

            self.pre = root.val
            dfs(root.right)

        dfs(root)

        return int(self.min_diff)