'''
题目描述:
给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 高度平衡 二叉搜索树。

高度平衡 二叉树是一棵满足「每个节点的左右两个子树的高度差的绝对值不超过 1 」的二叉树。
'''

'''
解题思路:
BST的中序遍历是升序的，因此本题等同于 根据中序遍历的序列 恢复二叉搜索树。
因此我们可以以升序序列中的任一个元素作为根节点，以该元素左边的升序序列构建左子树，
以该元素右边的升序序列构建右子树，这样得到的树就是一棵二叉搜索树
又因为本题要求高度平衡，因此我们需要选择升序序列的中间元素作为根节点
'''
from Tree.TreeNode import TreeNode
from typing import List

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:

        def dfs( low, high):
            if low > high:
                return None

            mid = (high + low)//2
            root = TreeNode(nums[mid])

            root.left = dfs( low, mid-1)
            root.right = dfs( mid+1, high)

            return root

        return dfs( 0, len(nums)-1)