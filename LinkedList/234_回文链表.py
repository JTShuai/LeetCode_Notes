'''
题目描述:
给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。
如果是，返回 true ；否则，返回 false 。
'''

'''
解题思路:
递归
快慢指针
'''
from LinkedList.ListNode import ListNode


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        self.front = head

        # 先遍历到尾节点，而self.front还在head
        def check(node):
            if node:
                if not check(node.next):
                    return False

                if self.front.val != node.val:
                    return False

                self.front = self.front.next

            return True

        return check(head)

    def isPalindrome2(self, head: ListNode) -> bool:
        '''
        快慢指针
        将链表的后半部分反转（修改链表结构），然后将前半部分和后半部分进行比较。
        比较完成后我们应该将链表恢复原样。
        '''
        if head is None:
            return True

        # 找到前半部分链表的尾节点并反转后半部分链表
        first_half_end = self.end_of_first_half(head)
        second_half_start = self.reverse_list(first_half_end.next)

        # 判断是否回文
        result = True
        first_position = head
        second_position = second_half_start
        while result and second_position is not None:
            if first_position.val != second_position.val:
                result = False
            first_position = first_position.next
            second_position = second_position.next

        # 还原链表并返回结果
        first_half_end.next = self.reverse_list(second_half_start)
        return result

    def end_of_first_half(self, head):
        fast = head
        slow = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse_list(self, head):
        previous = None
        current = head
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous


