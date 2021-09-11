'''
题目描述:

存在一个按升序排列的链表，给你这个链表的头节点 head ，
请你删除所有重复的元素，使每个元素 只出现一次 。

返回同样按升序排列的结果链表。
'''
from LinkedList.ListNode import ListNode


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None

        if not head.next:
            return head

        while head.next and head.val == head.next.val:
            head = head.next

        head.next = self.deleteDuplicates(head.next)

        return head

    def deleteDuplicates2(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        head.next = self.deleteDuplicates2(head.next)

        return head.next if head.val == head.next.val else head