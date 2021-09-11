'''
题目描述:
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
'''

'''
解题思路:
地板除2相等的两个节点交换

方法二:
递归解法
'''

from LinkedList.ListNode import ListNode


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return None
        if not head.next:
            return head

        dummy = head.next
        i = 0
        j = 0
        pre = None
        while head:
            if pre is None:
                pre = head
                head = head.next

            else:
                if i // 2 == j // 2:
                    pre.next, head.next = head.next, pre
                    head = pre.next
                    if pre.next and pre.next.next:
                        pre.next = pre.next.next
                else:
                    pre = head
                    head = head.next

                i += 1

            j += 1

        return dummy

    def swapPairs2(self, head: ListNode) -> ListNode:
        # 递归法
        if not head or not head.next:
            return head

        rest = head.next.next
        newHead = head.next
        newHead.next = head

        head.next = self.swapPairs2(rest)

        return newHead
