'''
题目描述:
给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
如果 pos 是 -1，则在该链表中没有环。注意，pos 仅仅是用于标识环的情况，并不会作为参数传递到函数中。

说明：不允许修改给定的链表。

进阶：
你是否可以使用 O(1) 空间解决此题？
'''
'''
解题思路:
1. 先判断有没有环
2. 有环时，慢指针走了 k 步，快指针走了 2k 步，则环的周长为k
3. 则令head开始往前走，slow继续往前走，当两指针相遇时，即在环的开始位置
'''
from LinkedList.ListNode import ListNode


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:

        slow = head
        fast = head

        def check(slow, fast):
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
                if slow == fast:
                    return slow

            return None

        slow = check(slow, fast)
        if slow:
            while slow != head:
                head = head.next
                slow = slow.next

            return slow

        return None