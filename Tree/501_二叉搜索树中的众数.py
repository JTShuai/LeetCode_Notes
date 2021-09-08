from typing import List

from Tree.TreeNode import TreeNode


class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        '''
        中序遍历
        记录出现次数, 并更新答案数组
        '''
        self.max_count = 0
        self.count = 0
        self.ans = []
        self.pre = None

        def dfs(root):
            if not root:
                return
            dfs(root.left)
            base = root.val
            if self.pre is None:
                self.pre = base
                self.count = 1
            else:
                if self.pre == base:
                    self.count += 1
                else:
                    self.count = 1

            if self.count == self.max_count:
                self.ans.append(base)
            elif self.count > self.max_count:
                self.ans = [base]
                self.max_count = self.count

            self.pre = base
            dfs(root.right)

        dfs(root)
        return self.ans