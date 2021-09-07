'''
题目描述:
给定一个二叉树的 根节点 root，请找出该二叉树的 最底层 最左边 节点的值。
假设二叉树中至少有一个节点。
'''
'''
BFS遍历
'''
from Tree import TreeNode
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        # 非空二叉树
        # queue = [root]
        # while queue:
        #     k = len(queue)
        #     temp = queue[0].val
        #     for _ in range(k):
        #         node = queue.pop(0)
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        #
        #     if not queue:
        #         # 一层遍历完后，如果都没有子节点，则找到了最底层
        #         return temp

        '''
        更快的解法，队列每次先存右再存左，则到最后一层时，最后判断的node(root)就为最底层最左边的节点
        '''
        queue = [root]

        while queue:
            k = len(queue)
            for _ in range(k):
                root = queue.pop(0)
                if root.right:
                    queue.append(root.right)

                if root.left:
                    queue.append(root.left)

        return root.val