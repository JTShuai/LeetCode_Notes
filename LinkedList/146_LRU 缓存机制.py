'''
题目描述:
运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制 。
实现 LRUCache 类：

LRUCache(int capacity) 以正整数作为容量 capacity 初始化 LRU 缓存

int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。

void put(int key, int value) 如果关键字已经存在，则变更其数据值；如果关键字不存在，
则插入该组「关键字-值」。当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，
从而为新的数据值留出空间。
 

进阶：你是否可以在 O(1) 时间复杂度内完成这两种操作？
'''
'''
解题思路:
方法一：
    构建链表（超出时间）
    
    
方法二:
    字典(哈希 + 双向链表)
LRU缓存机制可以通过哈希表辅以双向链表实现，我们用一个哈希表和一个双向链表维护所有在缓存中的键值对。

双向链表按照被使用的顺序存储了这些键值对，
靠近头部的键值对是最近使用的，而靠近尾部的键值对是最久未使用的。

哈希表即为普通的哈希映射（HashMap），通过缓存数据的键映射到其在双向链表中的位置。

'''

'''
方法一:
'''
class MyListNode:
    def __init__(self, key:int, val:int):
        self.key = key
        self.val = val
        self.next = None


class LRUCache1:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = 0
        self.head = MyListNode(-1,-1)

    def get(self, key: int) -> int:
        # 每次取到后，需要更新顺序
        head = self.head
        pre = None
        while head:
            if head.key == key:
                break
            pre = head
            head = head.next
        if head:
            pre.next = head.next
            head.next = self.head.next
            self.head.next = head
            return head.val

        return -1


    def put(self, key: int, value: int) -> None:

        # 要先判断key是不是已经存在了, 不用更新 cache, 但是要更新顺序
        head = self.head
        pre = None
        while head:
            if head.key == key:
                head.val = value
                # 更新链表顺序
                pre.next = head.next
                head.next = self.head.next
                self.head.next = head

                return

            pre = head
            head = head.next

        # 不存在则插入新节点
        node = MyListNode(key, value)
        if self.head.next:
            node.next = self.head.next

        self.head.next = node
        self.cache +=1

        # 判断当前 cache
        if self.cache > self.capacity:
            head = self.head
            for _ in range(self.capacity):
                head = head.next

            head.next = None

            self.cache -=1

'''
方法二
'''
class BiLinkedList:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.pre = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.size = 0

        # 使用伪头部和伪尾部节点
        self.head = BiLinkedList()
        self.tail = BiLinkedList()

        self.head.next = self.tail
        self.tail.pre = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        # 如果key存在，先通过map定位，再移到头部
        node = self.cache[key]
        self.moveToHead(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            # 创建一个新节点
            node = BiLinkedList(key,value)
            # 加入 map
            self.cache[key] = node
            # 加入双向链表
            self.addToHead(node)
            self.size += 1

            if self.size > self.capacity:
                # 删除双向链表尾部
                removed = self.removeTail()
                # 删除哈希表中对应项
                self.cache.pop(removed.key)
                self.size -= 1
        else:
            node = self.cache[key]
            node.val = value
            self.moveToHead(node)

    def addToHead(self, node: BiLinkedList):
        node.pre = self.head
        node.next = self.head.next
        self.head.next.pre = node
        self.head.next = node

    def removeNode(self, node: BiLinkedList):
        node.pre.next = node.next
        node.next.pre = node.pre

    def moveToHead(self, node: BiLinkedList):
        self.removeNode(node)
        self.addToHead(node)

    def removeTail(self):
        node = self.tail.pre
        self.removeNode(node)
        return node

