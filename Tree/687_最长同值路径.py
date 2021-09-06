'''
题目描述:
给定一个二叉树，找到最长的路径，这个路径中的每个节点具有相同值。 这条路径可以经过也可以不经过根节点。
注意：两个节点之间的路径长度由它们之间的边数表示。

示例 1:
输入:

              5
             / \
            4   5
           / \   \
          1   1   5
输出:
2


示例 2:
输入:

              1
             / \
            4   5
           / \   \
          4   4   5
输出:
2
注意: 给定的二叉树不超过10000个结点。 树的高度不超过1000。
'''

'''
解题思路:
其实二叉树递归的难点就在于怎么构思：子节点向父节点返回的是什么? 或者说，当前节点向其父节点返回的是什么?

这题中，当前节点返回给父节点的值就是：从当前节点出发，向下延伸与其值相同的最大深度 于是返回值分两种情况：
    1.if( 如果当前节点与其左右节点都不相等)，那么深度为0，则返回0 
    2. else，这个最大深度就取其 左右子树返回值中的较大者 + 1

然后，在上面这个dfs的遍历过程中，还可以做一些其他的事情，这题做的就是 计算路径长度。由于子树的返回值已经确定了，所以需要额外的一个全局变量。
如何计算路径长度呢？其实知道了和自己数值相等的左右子树的最大高度了，那么 把左右子树返回的值相加 就是贯穿自己的最长路径了。
'''

from Tree import TreeNode
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.ans = 0

        def dfs(root, previous_val):
            if not root:
                return 0



            left = dfs(root.left, root.val)
            right = dfs(root.right, root.val)

            self.ans = max(self.ans, left+right)

            if root.val == previous_val:
                return max(left,right) + 1
            else:
                return 0

        dfs(root, root.val)
        return self.ans - 1
