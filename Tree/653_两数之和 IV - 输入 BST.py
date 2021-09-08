'''
题目描述:
给定一个二叉搜索树 root 和一个目标结果 k，
如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 true。
'''

'''
解题思路:
使用中序遍历得到有序数组之后，再利用双指针对数组进行查找。
应该注意到，这一题不能用分别在左右子树两部分来处理这种思想，因为两个待求的节点可能分别在左右子树中。
'''

from Tree.TreeNode import TreeNode


class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        self.nums = []

        def inorder(root):
            if not root:
                return

            inorder(root.left)

            self.nums.append(root.val)

            inorder(root.right)


            return root.val

        inorder(root)

        # 两数之和问题
        visitied = {}
        n = len(self.nums)
        for num in self.nums:
            req = k - num
            if req in visitied:
                return True
            visitied[num] = 1

        return False
