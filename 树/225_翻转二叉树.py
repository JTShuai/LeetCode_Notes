'''
题目描述:
翻转一棵二叉树。

示例：

输入：
     4
   /   \
  2     7
 / \   / \
1   3 6   9

输出：
     4
   /   \
  7     2
 / \   / \
9   6 3   1

'''
from 树.TreeNode import TreeNode

'''
解题思路：
后序遍历
从最底下开始，把子树的左右调换
'''
def invertTree(root: TreeNode) -> TreeNode:

    def dfs(root):

        if not root:
            return None

        # left = dfs(root.left)
        # right = dfs(root.right)
        # root.left, root.right = right, left

        dfs(root.left)
        dfs(root.right)
        root.left, root.right = root.right, root.left

        return root

    return dfs(root)

