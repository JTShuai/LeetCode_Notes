'''
题目描述:
Trie（发音类似 "try"） 前缀树或字典树 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。
这一数据结构有相当多的应用情景，例如自动补完和拼写检查。

请你实现 Trie 类：

Trie() 初始化前缀树对象。
void insert(String word) 向前缀树中插入字符串 word 。
boolean search(String word) 如果字符串 word 在前缀树中，返回 true（即，在检索之前已经插入）；否则，返回 false 。
boolean startsWith(String prefix) 如果之前已经插入的字符串 word 的前缀之一为 prefix ，返回 true ；否则，返回 false 。
 

示例：

输入
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
输出
[null, null, true, false, true, null, true]

解释
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // 返回 True
trie.search("app");     // 返回 False
trie.startsWith("app"); // 返回 True
trie.insert("app");
trie.search("app");     // 返回 True

'''

'''
解题思路:

Trie，又称前缀树或字典树，是一棵有根树，其每个节点包含以下字段：
    1.指向子节点的指针数组 children。对于本题而言，数组长度为 26，即小写英文字母的数量。
    此时 children[0] 对应小写字母 a，children[1] 对应小写字母 b，…，children[25] 对应小写字母 z。
    2.布尔字段 isEnd，表示该节点是否为字符串的结尾。


插入字符串:
我们从字典树的根开始，插入字符串。对于当前字符对应的子节点，有两种情况：
    1. 子节点存在。沿着指针移动到子节点，继续处理下一个字符。
    2. 子节点不存在。创建一个新的子节点，记录在 children 数组的对应位置上，
    然后沿着指针移动到子节点，继续搜索下一个字符。
重复以上步骤，直到处理字符串的最后一个字符，然后将当前节点标记为字符串的结尾。


查找前缀:
我们从字典树的根开始，查找前缀。对于当前字符对应的子节点，有两种情况:
    1. 子节点存在。沿着指针移动到子节点，继续搜索下一个字符。
    2. 子节点不存在。说明字典树中不包含该前缀，返回空指针。
重复以上步骤，直到返回空指针或搜索完前缀的最后一个字符。

若搜索到了前缀的末尾，就说明字典树中存在该前缀。
此外，若前缀末尾对应节点的 isEnd 为真，则说明字典树中存在该字符串。
'''

'''
方法一：
二维数组
一个朴素的想法是直接使用「二维数组」来实现 Trie 树。

使用二维数组 trie[] 来存储我们所有的单词字符。
使用 index 来自增记录我们到底用了多少个格子（相当于给被用到格子进行编号）。
使用 count[] 数组记录某个格子被「被标记为结尾的次数」（当 idx 编号的格子被标记了 n 次，则有 cnt[idx] = n）。
'''
class Trie1(object):
    N = 100009

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # trie为 26xN 的二维数组
        self.trie = [[0] * self.N for i in range(26)]
        # count 为 1xN 的一维数组
        self.count = [0] * self.N

        self.index = 0

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        p = 0
        # 遍历word的每个letter
        for i in range(len(word)):
            # ASCII 数值差, 即当前字符在 'a'的前多少
            u = ord(word[i]) - ord('a')

            if self.trie[u][p] == 0:
                self.index += 1
                self.trie[u][p] = self.index

            p = self.trie[u][p]
        self.count[p] += 1

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        p = 0
        for i in range(len(word)):
            u = ord(word[i]) - ord('a')
            if self.trie[u][p] == 0:
                return False
            p = self.trie[u][p]
        return self.count[p] != 0

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        p = 0
        for i in range(len(prefix)):
            u = ord(prefix[i]) - ord('a')
            if self.trie[u][p] == 0:
                return False
            p = self.trie[u][p]
        return True


'''
方法二:
'''
class Trie2:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

    def searchPrefix(self, prefix: str) -> "Trie2":
        # 每次搜索都要从根结点开始
        node = self

        for ch in prefix:
            ch = ord(ch) - ord("a")
            if not node.children[ch]:
                return None

            node = node.children[ch]

        return node

    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            # 利用ASCII的差判断是第几个字母，如: 'a'-> 0, 'b'->1,..,'z'->25
            ch = ord(ch) - ord("a")

            # 如果对应字母的子树还是空的，则创建
            if not node.children[ch]:
                node.children[ch] = Trie2()
            # 下一个letter要保存在当前letter的子树里面
            node = node.children[ch]
        # 当word的所有字母记录完毕，在最后一个node更新单词完毕状态为True
        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self.searchPrefix(word)
        return node is not None and node.isEnd

    def startsWith(self, prefix: str) -> bool:
        return self.searchPrefix(prefix) is not None


'''
方法三:
相比二维数组，更加常规的做法是建立 TrieNode 结构节点。
随着数据的不断插入，根据需要不断创建 TrieNode 节点。
'''
# 字典实现
class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()

            node = node.children[c]

        node.is_word = True

    def search_prefix(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                return None
            node = node.children[c]
        return node

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.search_prefix(word)
        return node is not None and node.is_word

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        return self.search_prefix(prefix) is not None


# 标准实现
class TrieNode:
    def __init__(self):
        self.__R = 26
        self.isEnd = False
        self.links = [None] * self.__R

    def containsKey(self, ch):
        return self.links[ord(ch) - ord('a')] is not None

    def get(self, ch):
        return self.links[ord(ch) - ord('a')]

    def put(self, ch, node):
        self.links[ord(ch) - ord('a')] = node

class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        node = self.root
        for i in range(len(word)):
            if not node.containsKey(word[i]):
                node.put(word[i], TrieNode())
            node = node.get(word[i])
        node.isEnd = True

    def searchPrefix(self, word):
        node = self.root
        for i in range(len(word)):
            if node.containsKey(word[i]):
                node = node.get(word[i])
            else:
                return None
        return node

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.searchPrefix(word)
        return node is not None and node.isEnd

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.searchPrefix(prefix)
        return node is not None






if __name__ == '__main__':
    print(ord('a'), ord('b'))