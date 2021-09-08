'''
非递归形式实现二叉树后序遍历
'''
from typing import List

from Tree.TreeNode import TreeNode


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        stack = []
        pre = None
        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            if not root.right or root.right == pre:
                ans.append(root.val)
                pre = root
                root = None
            else:
                stack.append(root)
                root = root.right

        return ans