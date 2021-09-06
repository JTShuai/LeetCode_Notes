'''
题目描述:
给定一个二叉树的根节点 root ，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的 路径 的数目。
路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

'''

'''
解题思路:
前缀和: 一个节点的前缀和就是 该节点 到 根 之间的路径和。

拿下图解释：
节点4的前缀和为：1 + 2 + 4 = 7
节点8的前缀和：1 + 2 + 4 + 8 = 15
节点9的前缀和：1 + 2 + 5 + 9 = 17

      1
     /  \ 
    2    3
   / \    \ 
  4   5    6
 / \   \ 
7   8   9

题目要求的是找出路径和等于给定数值的路径总数, 而:
    两节点间的路径和 = 两节点的前缀和之差

还是拿下图解释：
             1
            / 
           2    
          / 
         3   
        / 
       4  
               
假如题目给定数值为5
节点1的前缀和为: 1
节点3的前缀和为: 1 + 2 + 3 = 6
prefix(3) - prefix(1) == 5
所以 节点1 到 节点3 之间有一条符合要求的路径( 2 --> 3 )

因此我们只用遍历整颗树一次，记录每个节点的前缀和，并查询该节点的祖先节点中符合条件的个数，将这个数量加到最终结果上。

HashMap的key是前缀和， value是该前缀和的节点数量，记录数量是因为有出现复数路径的可能
递归进入左右子树后，回到当前层，要把当前节点添加的前缀和去除，避免回溯之后影响上一层。

要注意的是，hashmap初始化时要有 {0:1}, 这是为了令root有个虚拟的父节点，比如在上图中，如果target=3，则到节点2时，
其前缀和=3，需要找一个前缀和为0的起始节点，而从起始节点往后一个节点开始直到当前节点的节点值之和才为target，因此为了不漏掉
从root出发的节点值之和=target，所以要有一个虚拟的root父节点，其前缀和为零，出现一次，即{0:1}。
'''

from Tree.TreeNode import TreeNode

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        # 初始化字典保存前缀和与其出现的次数
        prefix_map = {0:1}
        self.ans = 0

        def dfs(root:TreeNode, last_prefix):
            if not root:
                return 0

            cur_val = root.val
            cur_prefix = last_prefix + cur_val
            req_prefix = cur_prefix - targetSum

            if req_prefix in prefix_map.keys():
                self.ans += prefix_map[req_prefix]

            if cur_prefix in prefix_map.keys():
                prefix_map[cur_prefix] += 1
            else:
                prefix_map[cur_prefix] = 1

            # 向下搜索
            dfs(root.left, cur_prefix)
            dfs(root.right, cur_prefix)

            # 遍历完左右子节点，在向父节点回溯前，撤销当前的记录
            prefix_map[cur_prefix] -=1

        dfs(root, 0)
        return self.ans
