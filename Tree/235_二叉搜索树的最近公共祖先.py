'''
题目描述:
给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，
满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
'''

'''
解题思路:
如果两个节点值都小于根节点，说明他们都在根节点的左子树上，我们往左子树上找
如果两个节点值都大于根节点，说明他们都在根节点的右子树上，我们往右子树上找
如果一个节点值大于根节点，一个节点值小于根节点，说明他们他们一个在根节点的左子树上一个在根节点的右子树上，那么根节点就是他们的最近公共祖先节点。
'''


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def dfs(root):
            if (root.val - p.val) * (root.val - q.val) <= 0:
                return root

            if p.val > root.val and q.val > root.val:
                return dfs(root.right)

            if p.val < root.val and q.val < root.val:
                return dfs(root.left)

        return dfs(root)