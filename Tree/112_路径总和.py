'''
问题描述：
给你二叉树的根节点 root 和一个表示 目标和 的整数targetSum ，
判断该树中是否存在 根节点到叶子节点 的路径，这条路径上所有节点值相加等于目标和 targetSum 。

叶子节点 是指没有子节点的节点。

'''

'''
解题思路:
1. 后序遍历，将所有可能保存，再判断target在不在其中
2. 先序遍历，先将target减去当前节点数值，当到叶子节点减到零，说明找到了
'''



from typing import Optional
from Tree.TreeNode import TreeNode

def hasPathSum(root: Optional[TreeNode], targetSum: int) -> bool:
    if not root:
        return False

    def dfs(root: TreeNode, residual: int) -> bool:

        if not root:
            if residual == 0:
                return True
            else:
                return False

        cur_val = root.val
        # 需要剪枝，因为不是满二叉树，可能存在节点只有一个子节点
        left, right = False, False
        if not root.left and root.right:
            right = dfs(root.right, residual - cur_val)
        elif root.left and not root.right:
            left = dfs(root.left, residual - cur_val)
        else:
            left = dfs(root.left, residual-cur_val)
            right = dfs(root.right, residual-cur_val)


        return left or right

    return dfs(root, targetSum)

'''
更快的解法：
    def hasPathSum(root: Optional[TreeNode], targetSum: int) -> bool:

        if not root: 
            return False
        
        # 这里不会进入None节点，而是在叶子节点出做判断
        if not root.left and not root.right:
            return sum == root.val
        
        return hasPathSum(root.left, sum - root.val) or hasPathSum(root.right, sum - root.val)
'''