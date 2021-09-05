'''
题目描述：
给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。
这条路径可能穿过也可能不穿过根结点。 

示例 :
给定二叉树

          1
         / \
        2   3
       / \
      4   5
返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。

'''

'''
解题思路:
dfs

假设我们知道对于该节点的左儿子向下遍历经过最多的节点数 L（即以左儿子为根的子树的深度） 
和其右儿子向下遍历经过最多的节点数 R（即以右儿子为根的子树的深度），
那么以该节点为起点的路径经过节点数的最大值即为 L+R+1。

我们记节点 node 为起点的路径经过节点数的最大值为 d_node，那么二叉树的直径就是所有节点
d_node的最大值减一。

e.g., 路径 [9, 4, 2, 5, 7, 8] 可以被看作以 2 为起点，
从其左儿子向下遍历的路径 [2, 4, 9] 和从其右儿子向下遍历的路径 [2, 5, 7, 8] 拼接得到。
其中，d_node = 2(L)+3(R)+1, 直径=d_node -1 = 5
          1
         /  \
        2    3
       /  \
      4    5
     /    / \
    9    7   6
        / 
       8

因此算法为：
利用递归函数，返回以当前节点为根结点的子树深度。
1. 分别求得左右儿子深度，L、R
2. 则当前节点的 d_node = L+R+1
3. 当前节点为根构造的子树深度为: max(L+R) + 1
4. 设一个全局变量记录最大d_node
5. 最后返回 d_node-1
'''

from 树.TreeNode import TreeNode

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:

        self.ans = 1

        def dfs(root):
            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            self.ans = max(self.ans, left + right + 1)

            return 1 + max(left, right)

        dfs(root)

        return self.ans - 1



