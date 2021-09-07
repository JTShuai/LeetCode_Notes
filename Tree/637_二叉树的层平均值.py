'''
题目描述:
给定一个非空二叉树, 返回一个由每层节点平均值组成的数组。


示例 1：
输入：
    3
   / \
  9  20
    /  \
   15   7
输出：[3, 14.5, 11]
解释：
第 0 层的平均值是 3 ,  第1层是 14.5 , 第2层是 11 。因此返回 [3, 14.5, 11] 。
'''

'''
BFS遍历
'''

from Tree import TreeNode
from typing import List

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        # 非空二叉树

        res = []
        queue = [root]

        while queue:
            k = len(queue)
            sum = 0

            for i in range(k):
                node = queue.pop(0)
                sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(sum/k)


        # res = [root.val]
        # queue = []
        # queue.append(root.left)
        # queue.append(root.right)
        #
        # while queue:
        #     sum = 0
        #     valid = 0
        #     k = len(queue)
        #     for _ in range(k):
        #         node = queue.pop(0)
        #         if node:
        #             sum += node.val
        #             valid +=1
        #             queue.append(node.left)
        #             queue.append(node.right)
        #     if valid >0:
        #         res.append(sum/valid)

        return res
