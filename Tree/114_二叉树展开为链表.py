'''
题目描述:
给你二叉树的根结点 root ，请你将它展开为一个单链表：
展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。
展开后的单链表应该与二叉树 先序遍历 顺序相同。
'''
'''
解题思路:
dfs前序遍历
'''
from Tree.TreeNode import TreeNode


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None

        stack = [root]
        prev = None

        while stack:
            curr = stack.pop()
            if prev:
                prev.left = None
                prev.right = curr

            left, right = curr.left, curr.right
            if right:
                stack.append(right)
            if left:
                stack.append(left)
            prev = curr

    def flatten2(self, root: TreeNode) -> None:
        # 方法二: 将右子树接到左子树最上面的右节点
        while root:
            if root.left is None:
                root = root.right
            else:
                # 找左子树最右节点
                pre = root.left
                while pre.right:
                    pre = pre.right
                # 将原来的右子树接到左子树的最右边节点
                pre.right = root.right
                # 将左子树插到右子树的地方
                root.right = root.left
                root.left = None

                # 考虑下一个节点
                root = root.right