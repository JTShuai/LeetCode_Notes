'''
给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

'''

'''
解题思路:
方法一:
    把链表转化为数组
方法二:
    快慢指针实现像108题中的取中间值
方法三:
    中序遍历：链表头节点对应 BST 最左子树的根节点。
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedListToBST1(self, head: ListNode) -> TreeNode:
        # 方法一：把链表转化为数组
        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        # 基于nums进行中序搜索
        def dfs(nums, left, right):
            if left>right:
                return None
            mid = (left + right)//2
            root = TreeNode(val=nums[mid])
            root.left = dfs(nums,left,mid-1)
            root.right = dfs(nums,mid+1,right)
            return root

        return dfs(nums,0,len(nums)-1)

    def sortedListToBST2(self, head: ListNode) -> TreeNode:
        # 方法二：快慢指针
        def dfs(head):
            if not head:
                return None

            fast = head
            slow = head
            preSlow = None

            while fast and fast.next:
                preSlow = slow
                fast = fast.next.next
                slow = slow.next

            # 这时候slow就是mid
            root = TreeNode(val=slow.val)
            root.right = dfs(slow.next)

            if preSlow:
                preSlow.next = None
                root.left = dfs(head)

            return root

        return dfs(head)

    def sortedListToBST3(self, head: ListNode) -> TreeNode:
        # 方法三：中序遍历，先构建左子树，再构建根节点，再构建右子树。
        if not head:
            return None

        # 记住head位置
        self.h = head

        # 获得链表长度
        length = 0
        while head:
            length += 1
            head = head.next

        def inorder(start, end):
            if start > end:
                return None

            mid = (start + end)//2

            # 左区间递归创建左子树
            left = inorder(start,mid-1)

            # 创建父节点
            root = TreeNode(self.h.val)
            # 创建一个父节点便更新h的位置
            self.h = self.h.next

            # 连接左子树和父节点
            root.left = left

            # 右区间创建右子树
            root.right = inorder(mid + 1, end)

            return root

        return inorder(0,length-1)





