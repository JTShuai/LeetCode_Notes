'''
题目描述:
给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。

有效 二叉搜索树定义如下：
    节点的左子树只包含 小于 当前节点的数。
    节点的右子树只包含 大于 当前节点的数。
    所有左子树和右子树自身必须也是二叉搜索树。

'''

'''
解题思路:
中序遍历判断大小
'''
from Tree.TreeNode import TreeNode
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return False
        self.flag = True
        self.pre = None

        def inorder(root):
            if not root:
                return

            inorder(root.left)
            if self.pre is None:
                self.pre = root
            else:
                if self.pre.val >= root.val:
                    self.flag = False

                self.pre = root

            inorder(root.right)


        return self.flag