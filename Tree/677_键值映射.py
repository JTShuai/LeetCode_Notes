'''
实现一个 MapSum 类，支持两个方法，insert 和 sum：

MapSum() 初始化 MapSum 对象

void insert(String key, int val) 插入 key-val 键值对，字符串表示键 key ，整数表示值 val 。
如果键 key 已经存在，那么原来的键值对将被替代成新的键值对。

int sum(string prefix) 返回所有以该前缀 prefix 开头的键 key 的值的总和。
 

示例：

输入：
["MapSum", "insert", "sum", "insert", "sum"]
[[], ["apple", 3], ["ap"], ["app", 2], ["ap"]]
输出：
[null, null, 3, null, 5]

解释：
MapSum mapSum = new MapSum();
mapSum.insert("apple", 3);
mapSum.sum("ap");           // return 3 (apple = 3)
mapSum.insert("app", 2);
mapSum.sum("ap");           // return 5 (apple + app = 3 + 2 = 5)

'''
class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.val = 0

class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()


    def insert(self, key: str, val: int) -> None:
        node = self.root
        for ch in key:
            idx = ord(ch) - ord('a')
            if node.children[idx] is None:
                node.children[idx] = TrieNode()
            node = node.children[idx]

        node.val = val



    def sum(self, prefix: str) -> int:
        node = self.root
        total_sum = 0
        early_stop = False
        for ch in prefix:
            idx = ord(ch) - ord('a')
            if node.children[idx] is None:
                early_stop = True
                break
            node = node.children[idx]
        # total_sum += node.val

        # 在最后一个字母的Node迭代搜索
        if not early_stop:
            # total_sum -= node.val
            stack = [node]
            while stack:
                node = stack.pop()
                total_sum += node.val
                for i in range(26):
                    if node.children[i]:
                        stack.append(node.children[i])


        return total_sum
