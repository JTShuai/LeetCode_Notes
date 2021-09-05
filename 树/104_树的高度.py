'''
题目描述：
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，index:[0,1,2,3,4,5,6]

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。
'''

'''
解题思路：
一颗二叉树的节点数为 2^k -1,其中k为层数

但是本题的输入是根结点(root)，因此需要使用dfs

1. 先序遍历：
    先计数，再搜索
2. 中序遍历：
    左-计数-右
3. 后序遍历：
    左-右-计数
'''
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
def maxDepth(root: TreeNode) -> int:
    if not root:
        return 0

    def dfs(node:TreeNode):

        depth = 1
        sub_depth_left = 0
        sub_depth_right = 0
        if node.left:
            sub_depth_left = dfs(node.left)
        if node.right:
            sub_depth_right = dfs(node.right)

        # 到这说明当前节点无节点
        return depth+max(sub_depth_left,sub_depth_right)

    return dfs(root)

'''


# 改进版:
def maxDepth(root: TreeNode) -> int:

    def dfs(node: TreeNode):

        if node is None:
            return 0
        else:
            depth = 1

            sub_depth_left = dfs(node.left)
            sub_depth_right = dfs(node.right)

            return depth + max(sub_depth_left, sub_depth_right)

    return dfs(root)
