'''
题目描述:
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

进阶：你能尝试使用一趟扫描实现吗？

链表中结点的数目为 sz
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
'''

'''
解题思路:
快慢指针
'''
from LinkedList.ListNode import ListNode


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # slow比fast慢 n 步
        dummy = ListNode()
        dummy.next = head

        slow = dummy
        fast = dummy

        while n > 0:
            fast = fast.next
            n -= 1

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return dummy.next
