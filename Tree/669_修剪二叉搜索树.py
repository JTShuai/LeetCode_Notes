'''
题目描述:
给你二叉搜索树的根节点 root ，同时给定最小边界low 和最大边界 high。
通过修剪二叉搜索树，使得所有节点的值在[low, high]中。
修剪树不应该改变保留在树中的元素的相对结构（即，如果没有被移除，原有的父代子代关系都应当保留）。 可以证明，存在唯一的答案。

所以结果应当返回修剪好的二叉搜索树的新的根节点。注意，根节点可能会根据给定的边界发生改变。 
'''

'''
解题思路:
二叉搜索树：是父结点值大于左子树任意结点值，小于右子树任意结点值
    1. 如果左孩大于low,则当前节点大于low
    2. 如果左孩节点小于low, 删去左孩，并判断当前节点是否大于low
    3. 如果右孩子节点小于high, 则当前节点小于high
    4. 如果右孩节点大于high, 删去右孩，并判断当前节点是否小于high

1. 如果当前节点小于low，左子树必定小于low
2. 如果当前节点大于high,右子树必定大于high
因此考虑中序遍历
'''
from Tree import TreeNode


class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        if not root:
            return []

        def inorder(root):
            if not root:
                return None

            left = inorder(root.left)
            cur_val = root.val
            right = inorder(root.right)

            if low <= cur_val <= high:
                root.left = left
                root.right = right
                return root
            if cur_val<low:
                return right
            if cur_val>high:
                return left


        return inorder(root)