'''
题目描述:
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
 
示例 1：
输入：s = "()"
输出：true

示例 2：
输入：s = "()[]{}"
输出：true

示例 3：
输入：s = "(]"
输出：false

示例 4：
输入：s = "([)]"
输出：false

示例 5：
输入：s = "{[]}"
输出：true

'''

'''
解题思路:
利用栈：
    后入后出
    依此遍历字符,如果为左括号则入栈，当遇到右括号时，如果右括号与栈顶为一对，则出栈
    当字符串遍历完栈为空时，返回true否则返回false
    当右与栈顶无法匹配时，返回false
'''

def isValid(s: str) -> bool:
    if len(s) % 2 != 0:
        return False

    valid_map = {
        '(': ')',
        '[': ']',
        '{': '}'
    }

    stack = []
    for symbol in s:
        if symbol in valid_map.keys():
            # 左括号则入栈
            stack.append(symbol)
        else:
            if stack and valid_map[stack[-1]] == symbol:
                stack.pop()
            else:
                return False

    return not stack


if __name__ == '__main__':
    print(isValid("(([]){})"))
    # "(([]){})"