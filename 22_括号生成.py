from typing import List
'''
题目描述:
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

有效括号组合需满足：左括号必须以正确的顺序闭合。


示例 1：
输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]

示例 2：
输入：n = 1
输出：["()"] 


提示：
1 <= n <= 8
'''

def generateParenthesis(n: int) -> List[str]:
    if n==1:
        return ["()"]

    res = []
    left = n-1
    right = n
    remained_left = 1

    def backtrack(combination, left, right, remained_left):
        if left == 0:
            res.append(combination + ')'*right)

        elif left == 1 and right ==1 and remained_left==0:
            res.append(combination+'()')

        else:
            if remained_left > 0:
                options = ['(',')']
                for side in options:
                    if side == '(':
                        backtrack(combination + side, left-1, right, remained_left+1)
                    else:
                        backtrack(combination + side, left, right-1, remained_left-1)

            else:
                # 只能生左枝
                backtrack(combination + '(', left-1, right, remained_left+1)


    backtrack('(', left, right, remained_left)

    return res

if __name__ == '__main__':
    print(generateParenthesis(3))