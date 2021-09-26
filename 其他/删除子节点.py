class Solution:
    def Delete(self, root, data):
        # write code here
        # 前序遍历

        def dfs(root):
            if not root:
                return None
            cur_val = root.val
            if cur_val == data:
                temp_right = root.right
                temp_left = root.left
                if temp_left is None:
                    return None
                elif temp_right is None:
                    root = temp_left
                else:
                    # 两个子节点都不为空
                    root = temp_left
                    root.left = temp_right
                    root.right = temp_left.left


            root.left = dfs(root.left)
            root.right = dfs(root.right)

            return root

        return dfs(root)