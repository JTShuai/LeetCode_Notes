'''
题目描述:
给定一个二叉搜索树的根节点 root ，和一个整数 k ，请你设计一个算法查找其中第 k 个最小元素（从 1 开始计数）。
'''

'''
解题思路:
dfs，中序遍历，不过是从右到左
'''
from Tree import TreeNode


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:

        self.ans = None
        def dfs(root):
            if not root:
                return []

            right = dfs(root.right)
            right.append(root.val)

            left = dfs(root.left)
            right.extend(left)

            if len(right) >= k:
                self.ans = right[-k]

            return right

        dfs(root)

        return self.ans

    # 更简洁的解法
    def kthSmallest2(self, root: TreeNode, k: int) -> int:
        self.cnt = 0
        self.val = None
        def dfs(root, k):
            if not root:
                return
            dfs(root.left,k)
            self.cnt +=1
            if self.cnt == k:
                self.val = root.val
                return
            dfs(root.right, k)
        dfs(root,k)

        return self.val