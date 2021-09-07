'''
题目描述:
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，
满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

注意与235题的区别，这里不再是有序二叉树
'''

'''
解题思路:
p 和 q 在 root 的子树中，且分列 root 的 异侧（即分别在左、右子树中）；
p = root ，且 q 在 root 的左或右子树中；
q = root ，且 p 在 root 的左或右子树中；


开启递归左子节点，返回值记为 left ；
开启递归右子节点，返回值记为 right ；

返回值： 根据 left 和 right ，可展开为四种情况；
当 left 和 right 同时为空 ：说明 root 的左 / 右子树中都不包含 p,qp,q ，返回 null ；
当 left 和 right 同时不为空 ：说明 p, qp,q 分列在 root 的 异侧 （分别在 左 / 右子树），因此 root 为最近公共祖先，返回 root ；
当 left 为空 ，right 不为空 ：p,qp,q 都不在 root 的左子树中，直接返回 right 。具体可分为两种情况：
    p,q 其中一个在 root 的 右子树 中，此时 right 指向 p（假设为 p ）；
    p,q 两节点都在 root 的 右子树 中，此时的 right 指向 最近公共祖先节点 ；
当 left 不为空 ， right 为空 ：与情况 3. 同理；

'''


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def dfs(root):
            if not root:
                return None

            if root == p or root == q:
                return root

            left = dfs(root.left)
            right = dfs(root.right)

            if not left and not right:
                return left

            if left and right:
                return root

            if right:
                return right

            if left:
                return left

        return dfs(root)