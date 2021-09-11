'''

给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。

你可以假设除了数字 0 之外，这两个数字都不会以零开头。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from LinkedList.ListNode import ListNode


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_stack = []
        l2_stack = []
        while l1:
            l1_stack.append(l1)
            l1 = l1.next

        while l2:
            l2_stack.append(l2)
            l2 = l2.next

        if len(l1_stack) < len(l2_stack):
            l1_stack, l2_stack = l2_stack, l1_stack

        add_shift = 0
        while l2_stack:
            l2 = l2_stack.pop()
            l1 = l1_stack.pop()
            temp = (l2.val + l1.val + add_shift) // 10
            l1.val = (l2.val + l1.val + add_shift) % 10
            add_shift = temp

        while l1_stack:
            l1 = l1_stack.pop()
            temp = (l1.val + add_shift) // 10
            l1.val = (l1.val + add_shift) % 10
            add_shift = temp

        if add_shift > 0:
            start = ListNode(add_shift)
            start.next = l1
            return start

        return l1

    def addTwoNumbers2(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 更快的实现
        l1_stack = []
        l2_stack = []
        while l1:
            l1_stack.append(l1)
            l1 = l1.next

        while l2:
            l2_stack.append(l2)
            l2 = l2.next

        add_shift = 0
        ans = None
        while l1_stack or l2_stack or add_shift != 0:
            # 当栈空了后，对应的值置为零
            a = ListNode(0) if not l1_stack else l1_stack.pop()
            b = ListNode(0) if not l2_stack else l2_stack.pop()

            temp = a.val + b.val + add_shift
            add_shift = temp // 10
            a.val = temp % 10
            a.next = ans
            ans = a

        return ans



