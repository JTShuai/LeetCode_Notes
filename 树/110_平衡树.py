'''
题目描述:
给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：
一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1 。


示例 1：
输入：root = [3,9,20,null,null,15,7]
输出：true

示例 2：
输入：root = [1,2,2,3,3,null,null,4,4]
输出：false

示例 3：
输入：root = []
输出：true
 
提示：
树中的节点数在范围 [0, 5000] 内
-104 <= Node.val <= 104
'''


'''
解题思路：
利用后序遍历
从底至顶返回子树最大高度，若判定某子树不是平衡树则 “剪枝” ，直接向上返回。

当节点root 左 / 右子树的高度差 < 2：
    则返回以节点root为根节点的子树的最大高度，即节点 root 的左右子树中最大高度加 11 （ max(left, right) + 1 ）；
当节点root 左 / 右子树的高度差 ≥ 2：
    则返回 -1 ，代表 此子树不是平衡树 。

'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isBalanced(root: TreeNode) -> bool:

    def dfs(root: TreeNode):
        if not root:
            return 0

        left = dfs(root.left)
        right = dfs(root.right)

        # 如果子树有不平衡子树或左右两边不平衡
        if abs(left-right) >=2 or -1 in [left,right]:
            return -1

        return 1 + max(left, right)

    return -1 != dfs(root)



