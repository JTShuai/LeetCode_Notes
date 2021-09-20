'''
题目描述:
给定一个非空字符串 s 和一个包含非空单词的列表 wordDict，
判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

说明：
拆分时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。

示例 1：
输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
'''

'''
解题思路:
顺序完全背包问题
求解顺序的完全背包问题时，对物品的迭代应该放在最里层，对背包的迭代放在外层，
只有这样才能让物品按一定顺序放入背包中。

dp[i]: 前 i 个字符能否被字典拆分
'''
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        m = len(s)
        dp = [True] + [False]*m
        for i in range(1, m+1):
            for word in wordDict:
                word_len = len(word)
                if word_len <= i and word == s[i-word_len:i]:
                    dp[i] |= dp[i-word_len]

        return dp[m]