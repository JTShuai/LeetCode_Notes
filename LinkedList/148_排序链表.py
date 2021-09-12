'''
题目描述:
给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。

进阶：
你可以在 O(n logn) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？
'''
'''
要求 nlogn 则需要二分法，因此需要归并排序
'''
from LinkedList.ListNode import ListNode


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
