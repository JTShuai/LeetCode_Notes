'''

'''
from Tree.TreeNode import TreeNode


def serialize(self, root):
    """Encodes a tree to a single string.

    :type root: TreeNode
    :rtype: str
    """
    # 前序遍历
    def dfs(root):
        if not root:
            return 'null'

        root_val = root.val

        left = dfs(root.left)
        right = dfs(root.right)

        return str(root_val)+','+left + ',' + right

    return dfs(root)


def deserialize(self, data):
    """Decodes your encoded data to tree.

    :type data: str
    :rtype: TreeNode
    """
    if not data: return None

    data = data.split(',')
    root = self.buildTree(data)
    return root


def buildTree(self, data):
    val = data.pop(0)
    if val == 'null': return None

    node = TreeNode(val)

    node.left = self.buildTree(data)
    node.right = self.buildTree(data)

    return node