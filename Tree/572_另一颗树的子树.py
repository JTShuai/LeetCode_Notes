'''
题目描述:
给你两棵二叉树 root 和 subRoot 。检验 root 中是否包含和 subRoot 具有相同结构和节点值的子树。
如果存在，返回 true ；否则，返回 false 。

二叉树 tree 的一棵子树包括 tree 的某个节点和这个节点的所有后代节点。tree 也可以看做它自身的一棵子树。
'''


'''
解题思路:
方法一：
    深度优先搜索暴力匹配，双递归
方法二：
    深度优先搜索序列上做串匹配：判断「s 的深度优先搜索序列包含 t 的深度优先搜索序列」
方法三：
    树哈希：考虑把每个子树都映射成一个唯一的数，
    如果 t 对应的数字和 s 中任意一个子树映射的数字相等，则 t 是 s 的某一棵子树。
'''

from Tree.TreeNode import TreeNode

# 方法一
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if not root:
            return False

        def check(root,subRoot) -> bool:
            if not root and not subRoot:
                return True

            if not (root and subRoot):
                return False

            if root.val != subRoot.val:
                return False

            return check(root.left, subRoot.left) and check(root.right, subRoot.right)

        def dfs(root,subRoot):
            if not root:
                return False
            return check(root,subRoot) or dfs(root.left, subRoot) or dfs(root.right,subRoot)

        return dfs(root,subRoot)

# 方法二
class Solution2:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:

        # 遍历树，并保存序列
        def backorder(root):
            stack = [root]
            result = []
            while stack:
                root = stack.pop()
                if root == "lnull" or root == "rnull":
                    result.append(root)
                else:
                    result.append(root.val)
                    if root.left:
                        stack.append(root.left)
                    else:
                        stack.append("lnull")
                    if root.right:
                        stack.append(root.right)
                    else:
                        stack.append("rnull")
            return result[::-1]

        slist = backorder(s)
        tlist = backorder(t)
        for i in range(len(slist) - len(tlist) + 1):
            if slist[i:len(tlist) + i] == tlist:
                return True
        return False
