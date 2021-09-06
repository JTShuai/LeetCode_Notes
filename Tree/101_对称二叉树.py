'''
题目描述:
给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3
'''

'''
解题思路:
递归实现:
    递归的比较左子树和右子树。左子树的左子节点要等于右子树的右子节点
    
迭代实现:
    利用队列，首先从队列中拿出两个节点(left 和 right)比较
        将 left 的 left 节点和 right 的 right 节点放入队列
        将 left 的 right 节点和 right 的 left 节点放入队列
    
'''
from Tree.TreeNode import TreeNode

class Solution:
    def isSymmetric1(self, root: TreeNode) -> bool:

        if not root:
            return False

        def check(left, right) -> bool:
            if not left and not right:
                return True

            if not (left and right):
                return False

            if left.val == right.val:
                return check(left.left, right.right) and check(left.right, right.left)
            else:
                return False

        return check(root.left, root.right)


    def isSymmetric2(self, root: TreeNode) -> bool:

        if not root:
            return False

        queue = [root.left, root.right]

        while queue:
            left = queue.pop(0)
            right = queue.pop(0)

            if not left and not right:
                continue

            if not (left and right):
                return False

            if left.val != right.val:
                return False

            queue.append(left.left)
            queue.append(right.right)

            queue.append(left.right)
            queue.append(right.left)

        return True




