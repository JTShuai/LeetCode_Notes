'''
题目描述:
给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。
'''


from typing import List
from Tree.TreeNode import TreeNode


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        ans = []
        queue = [root]

        while queue:
            cur_level_len = len(queue)
            cur_val = []
            for _ in range(cur_level_len):
                root = queue.pop(0)
                cur_val.append(root.val)

                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
            ans.append(cur_val)

        return ans