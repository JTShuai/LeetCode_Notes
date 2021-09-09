'''
非递归实现
'''
from typing import List

from Tree.TreeNode import TreeNode


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        ans = []
        stack = []

        while root or stack:

            while root:
                stack.append(root)
                ans.append(root.val)
                root=root.left

            root = stack.pop()
            root = root.right

        return ans