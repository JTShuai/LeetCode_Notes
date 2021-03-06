from typing import List
'''
# 题目描述
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

示例 1：
输入：digits = "23"
输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]

示例 2：
输入：digits = ""
输出：[]

示例 3：
输入：digits = "2"
输出：["a","b","c"]

'''

'''
解题思路：
方法一：
    回溯法
    
方法二：
    队列

'''

phone = {'2':['a','b','c'],
         '3':['d','e','f'],
         '4':['g','h','i'],
         '5':['j','k','l'],
         '6':['m','n','o'],
         '7':['p','q','r','s'],
         '8':['t','u','v'],
         '9':['w','x','y','z']}

def letterCombinations(digits: str) -> List[str]:
    if not digits:
        return []

    res = []

    def backtrack(digits, combination) -> List[str]:
        if len(digits) == 0:
            res.append(combination)
        else:

            char_options = phone[digits[0]]

            for char in char_options:
                backtrack(digits[1:], combination+char)



    backtrack(digits,'')

    return res

if __name__ == '__main__':

    print(letterCombinations("23"))

