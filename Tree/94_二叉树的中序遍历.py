'''
利用非递归方式实现，即使用迭代方式
'''
from typing import List

from Tree import TreeNode


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        ans = []
        # 利用后进先出, 最左叶子节点最后进去，但要最先出来
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            # 收集左子树
            # 考虑最后一个左节点不是叶子节点，而是有右子树
            root = stack.pop()
            ans.append(root.val)

            root = root.right

        return ans