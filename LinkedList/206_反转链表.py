'''
题目描述:
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
'''

'''
解题思路:
迭代法:
利用pre保存上一个node，一边遍历一边反转

递归法:
假设链表的其余部分已经被反转，现在应该反转它前面的部分。
若从节点 n_{k+1}到 n_m已经被反转，而我们正处于 n_k。
我们希望 n_{k+1}的下一个节点指向 n_k。
所以，n_k.next.next = n_k。

需要注意的是 n_1的下一个节点必须指向None

'''
from LinkedList.ListNode import ListNode


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        pre = None
        while head:
            temp = head.next
            head.next = pre

            pre = head
            head = temp

        return pre

    def reverseList2(self, head: ListNode) -> ListNode:
        # 方法二: 递归
        if not head or not head.next:
            return head

        newHead = self.reverseList2(head.next)
        head.next.next = head
        head.next = None

        return newHead











