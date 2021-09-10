from Tree.TreeNode import TreeNode


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        # 中序遍历，记录全局最大值
        self.max_sum = -1001

        def dfs(root):
            if not root:
                return 0

            left = dfs(root.left)
            cur_val = root.val

            right = dfs(root.right)

            if left <= 0 and right <= 0:
                self.max_sum = max(self.max_sum, cur_val)
                return cur_val
            else:
                self.max_sum = max(self.max_sum, cur_val + max(0, right) + max(left, 0))
                return cur_val + max(left, right)

        dfs(root)

        return self.max_sum