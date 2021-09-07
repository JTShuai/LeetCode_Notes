'''
给出二叉 搜索 树的根节点，该树的节点值各不相同，请你将其转换为累加树（Greater Sum Tree），
使每个节点 node 的新值等于原树中大于或等于 node.val 的值之和。

提醒一下，二叉搜索树满足下列约束条件：

节点的左子树仅包含键 小于 节点键的节点。
节点的右子树仅包含键 大于 节点键的节点。
左右子树也必须是二叉搜索树。
'''

'''
解题思路:
根据题意，
每个左节点的新值为：
    父节点新值+右子树的合+自己的值
每个右节点的新值为：
    右子树的合+自己的值

中序遍历，但是从右到左
'''
from Tree import TreeNode


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        self.stack = [0]

        def dfs(root):

            if root.right:
                dfs(root.right)

            root.val += self.stack.pop()
            self.stack.append(root.val)

            if root.left:
                dfs(root.left)

            return root.val

        dfs(root)
        return root
