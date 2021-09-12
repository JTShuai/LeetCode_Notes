'''
题目描述:
给定一个头结点为 root 的链表, 编写一个函数以将链表分隔为 k 个连续的部分。

每部分的长度应该尽可能的相等: 任意两部分的长度差距不能超过 1，也就是说可能有些部分为 null。

这k个部分应该按照在链表中出现的顺序进行输出，并且排在前面的部分的长度应该大于或等于后面的长度。

返回一个符合上述规则的链表的列表。

举例： 1->2->3->4, k = 5 // 5 结果 [ [1], [2], [3], [4], null ]

示例 1：
输入:
root = [1, 2, 3], k = 5
输出: [[1],[2],[3],[],[]]
解释:
输入输出各部分都应该是链表，而不是数组。
例如, 输入的结点 root 的 val= 1, root.next.val = 2, \root.next.next.val = 3, 且 root.next.next.next = null。
第一个输出 output[0] 是 output[0].val = 1, output[0].next = null。
最后一个元素 output[4] 为 null, 它代表了最后一个部分为空链表。

示例 2：
输入:
root = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 3
输出: [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
解释:
输入被分成了几个连续的部分，并且每部分的长度相差不超过1.前面部分的长度大于等于后面部分的长度。
 

提示:
root 的长度范围： [0, 1000].
输入的每个节点的大小范围：[0, 999].
k 的取值范围： [1, 50].
'''

'''
解题思路:
长度//k 得到k个list中每个list至少要有几个Node
长度%k  得到多余的Node，应当list从前往后，一次放一个Node,直到多余的Node耗尽
'''

from LinkedList.ListNode import ListNode
from typing import List


class Solution:
    def splitListToParts(self, head: ListNode, k: int) -> List[ListNode]:

        ans = []
        # 链表长度
        queue = []
        n = 0
        while head:
            n += 1
            queue.append(head)
            head = head.next

        base = n // k
        bonus = n % k

        for _ in range(k):
            cur_part = []

            # 先放base数量
            for _ in range(base):
                cur_part.append(queue.pop(0))

            # 再放bonus
            if bonus > 0:
                cur_part.append(queue.pop(0))
                bonus -= 1

            if cur_part:
                newHead = cur_part[0]
                end = cur_part[-1]
                end.next = None
                ans.append(newHead)
            else:
                ans.append(None)

        return ans

    def splitListToParts2(self, head: ListNode, k: int) -> List[ListNode]:
        # 更快
        ans = []
        root = head
        # 链表长度
        n = 0
        while head:
            n += 1

            head = head.next

        base = n // k
        bonus = n % k

        for _ in range(k):
            ans.append(root)
            if bonus > 0:
                for _ in range(base):
                    root = root.next
                bonus -= 1
            else:
                for _ in range(base - 1):
                    root = root.next

            if root:
                temp = root.next
                root.next = None
            else:
                temp = None

            root = temp

        return ans

