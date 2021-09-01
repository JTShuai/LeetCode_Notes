class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        str_len = len(s)
        char_map = {}
        left_index = 0

        for i in range(str_len):
            right_char = s[i]

            # 字符第一次出现
            if right_char not in char_map.keys():
                char_map[right_char] = i+1
            else:
                # 遇到了重复的字符，更新窗口左边,与字典
                left_index = max(char_map[right_char], left_index)
                char_map[right_char] = i+1

            max_len = max(i - left_index + 1, max_len)

        return max_len




if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring("tmmzuxt"))

    # print('abc'+'d')