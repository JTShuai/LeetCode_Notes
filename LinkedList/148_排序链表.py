'''
题目描述:
给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。

进阶：
你可以在 O(n logn) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？
'''
'''
要求 nlogn 则需要二分法，因此需要归并排序

方法一:
    递归实现
    1. 分割 cut 环节：找到当前链表中点，并从中点将链表断开（以便在下次递归 cut 时，链表片段拥有正确边界）；
        我们使用 fast,slow 快慢双指针法，奇数个节点找到中点，偶数个节点找到中心左边的节点。
        找到中点 slow 后，执行 slow.next = None 将链表切断。
        递归分割时，输入当前链表左端点 head 和中心节点 slow 的下一个节点 tmp(因为链表是从 slow 切断的)。
        cut 递归终止条件： 当head.next == None时，说明只有一个节点了，直接返回此节点。
    2. 合并 merge 环节：将两个排序链表合并，转化为一个排序链表。
        双指针法合并，建立辅助ListNode h 作为头部。
        设置两指针 left, right 分别指向两链表头部，比较两指针处节点值大小，由小到大加入合并链表头部，指针交替前进，直至添加完两个链表。
        返回辅助ListNode h 作为头部的下个节点 h.next。
        时间复杂度 O(l + r)，l, r 分别代表两个链表长度。


方法二:
    从底至顶直接合并
    cut 环节本质上是通过二分法得到链表最小节点单元，再通过多轮合并得到排序结果。
    每一轮合并merge操作针对的单元都有固定长度 intv，例如:
        第一轮合并时 intv = 1，即将整个链表切分为多个长度为1的单元，并按顺序两两排序合并，合并完成的已排序单元长度为2。
        第二轮合并时 intv = 2，即将整个链表切分为多个长度为2的单元，并按顺序两两排序合并，合并完成已排序单元长度为4。
        以此类推，直到单元长度 intv >= 链表长度，代表已经排序完成。
    根据以上推论，我们可以仅根据 intv 计算每个单元边界，并完成链表的每轮排序合并，例如:
        当 intv = 1时，将链表第1和第2节点排序合并，第3和第4节点排序合并，……。
        当 intv = 2时，将链表第1-2和第3-4节点排序合并，第5-6和第7-8节点排序合并，……。
        当 intv = 4时，将链表第1-4和第5-8节点排序合并，第9-12和第13-16节点排序合并，……。
    
    1. 统计链表长度length，用于通过判断intv < length判定是否完成排序；
    2. 额外声明一个节点res，作为头部后面接整个链表，用于：
        intv *= 2即切换到下一轮合并时，可通过res.next找到链表头部h；
        执行排序合并时，需要一个辅助节点作为头部，而res则作为链表头部排序合并时的辅助头部pre；后面的合并排序可以将上次合并排序的尾部tail用做辅助节点。
    3. 在每轮intv下的合并流程：
        3.1 根据intv找到合并单元1和单元2的头部h1, h2。由于链表长度可能不是2^n，需要考虑边界条件：
            在找h2过程中，如果链表剩余元素个数少于intv，则无需合并环节，直接break，执行下一轮合并；
            若h2存在，但以h2为头部的剩余元素个数少于intv，也执行合并环节，h2单元的长度为c2 = intv - i。
        3.2 合并长度为c1, c2的h1, h2链表，其中：
            合并完后，需要修改新的合并单元的尾部pre指针指向下一个合并单元头部h。（在寻找h1, h2环节中，h指针已经被移动到下一个单元头部）
            合并单元尾部同时也作为下次合并的辅助头部pre。
        3.3 当h == None，代表此轮intv合并完成，跳出。
    4. 每轮合并完成后将单元长度×2，切换到下轮合并：intv *= 2。
    
    
'''
from LinkedList.ListNode import ListNode


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return head

        def recursive(head):
            if not head.next:
                return head
            slow = head
            fast = head
            while fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next

            temp = slow.next
            slow.next = None
            if temp:
                left = recursive(head)
                right = recursive(temp)

                '''
                更快的合并方法
                h = res = ListNode(0)
                while left and right:
                    if left.val < right.val: h.next, left = left, left.next
                    else: h.next, right = right, right.next
                    h = h.next
                h.next = left if left else right
                return res.next
                '''
                # 合并
                mergedList = self.connectTwoList(left,right)

                return mergedList

            return slow

        return recursive(head)

    def connectTwoList(self,l1,l2):
        if not l1:return l2
        if not l2: return l1

        if l1.val <= l2.val:
            l1.next = self.connectTwoList(l1.next, l2)
            return l1

        else:
            l2.next = self.connectTwoList(l1, l2.next)
            return l2

    def sortList2(self, head: ListNode) -> ListNode:
        # 方法二

        def merge(head1: ListNode, head2: ListNode) -> ListNode:

            dummyHead = ListNode(0)
            temp, temp1, temp2 = dummyHead, head1, head2
            while temp1 and temp2:
                if temp1.val <= temp2.val:
                    temp.next = temp1
                    temp1 = temp1.next
                else:
                    temp.next = temp2
                    temp2 = temp2.next
                temp = temp.next
            if temp1:
                temp.next = temp1
            elif temp2:
                temp.next = temp2
            return dummyHead.next

        if not head:
            return head

        length = 0
        node = head
        # 计算长度
        while node:
            length += 1
            node = node.next

        dummyHead = ListNode(0, head)
        subLength = 1

        while subLength < length:
            prev, curr = dummyHead, dummyHead.next

            while curr:
                head1 = curr

                for i in range(1, subLength):
                    if curr.next:
                        curr = curr.next
                    else:
                        break

                head2 = curr.next
                curr.next = None
                curr = head2

                for i in range(1, subLength):
                    if curr and curr.next:
                        curr = curr.next
                    else:
                        break

                succ = None

                if curr:
                    succ = curr.next
                    curr.next = None

                merged = merge(head1, head2)
                prev.next = merged

                while prev.next:
                    prev = prev.next

                curr = succ
            subLength <<= 1

        return dummyHead.next
