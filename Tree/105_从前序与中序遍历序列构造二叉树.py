'''
题目描述:
给定一棵树的前序遍历 preorder 与中序遍历 inorder。
请构造二叉树并返回其根节点。
'''

'''
解题思路:
preorder中的每个元素，找到在 inorder 中的位置in_idx,
in_idx左边的所有元素，即为当前node的左子树，in_idx右边的所有元素即为当前node的右子树
重复上述操作
'''
from typing import List
from Tree.TreeNode import TreeNode


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        def build(preorder, inorder):
            if not preorder or not inorder:
                return None

            node_val = preorder.pop(0)
            root = TreeNode(node_val)

            in_idx = inorder.index(node_val)
            left_sub = inorder[:in_idx]
            root.left = build(preorder, left_sub)

            right_sub = inorder[in_idx+1:]
            root.right = build(preorder, right_sub)

            return root


        return build(preorder, inorder)
