'''
题目描述:
给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。
如果两个链表没有交点，返回 null 。

题目数据 保证 整个链式结构中不存在环。
'''

'''
解题思路:
设 A 的长度为 a + c，B 的长度为 b + c，其中 c 为尾部公共部分长度，
可知 a + c + b = b + c + a。

当访问 A 链表的指针访问到链表尾部时，令它从链表 B 的头部开始访问链表 B；
同样地，当访问 B 链表的指针访问到链表尾部时，令它从链表 A 的头部开始访问链表 A。
这样就能控制访问 A 和 B 两个链表的指针能同时访问到交点。

如果不存在交点，那么 a + b = b + a，以下实现代码中 l1 和 l2 会同时为 null，从而退出循环。


如果只是判断是否存在交点，那么就是另一个问题，即 编程之美 3.6 的问题。有两种解法：

把第一个链表的结尾连接到第二个链表的开头，看第二个链表是否存在环；
或者直接比较两个链表的最后一个节点是否相同。
'''

from LinkedList.ListNode import ListNode


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        l1 = headA
        l2 = headB

        while l1 != l2:
            l1 = l1.next if l1 else headB
            l2 = l2.next if l2 else headA

        return l1
