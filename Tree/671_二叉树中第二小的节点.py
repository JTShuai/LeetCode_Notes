'''
题目描述:
给定一个非空特殊的二叉树，每个节点都是正数，并且每个节点的子节点数量只能为 2 或 0。
如果一个节点有两个子节点的话，那么该节点的值等于两个子节点中较小的一个。

更正式地说，root.val = min(root.left.val, root.right.val) 总成立。

给出这样的一个二叉树，你需要输出所有节点中的第二小的值。如果第二小的值不存在的话，输出 -1 。
'''

'''
解题思路:
如果当前节点有孩节点:
    左孩子.val = 当前节点.val
    右孩子.val >= 当前节点.val 

如果右节点的值不等于左(当前)节点，则第二小的值一定为root的右孩，
如果右节点=当前节点，则向下继续搜索
'''

from Tree import TreeNode


class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if not root:
            return -1

        self.min = root.val

        def dfs(root):

            if not root:
                return -1

            if root.val > self.min:
                return root.val

            left = dfs(root.left)
            right = dfs(root.right)
            if left == -1 or right == -1:
                # 因为子节点数要么为0，要么为2，这种情况说明当前节点是叶子节点。
                # return max(left,right) 其实为 return -1
                return max(left, right)
            else:
                # 说明当前节点有子节点（子树），则返回两个大值中较小的那个
                # 如果不存在 root.val > self.min，则一定会有 -1
                return min(left, right)

        return dfs(root)