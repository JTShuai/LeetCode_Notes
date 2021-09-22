'''
题目描述:
最初记事本上只有一个字符 'A' 。你每次可以对这个记事本进行两种操作：
    Copy All（复制全部）：复制这个记事本中的所有字符（不允许仅复制部分字符）。
    Paste（粘贴）：粘贴 上一次 复制的字符。

给你一个数字 n ，你需要使用最少的操作次数，在记事本上输出 恰好 n 个 'A' 。
返回能够打印出 n 个 'A' 的最少操作次数。
'''
'''
解题思路:
方法一：
n >=4:
    如果当前长度 k 能被总长度 n 整除，则复制当前所有字符（更新base）并粘贴，更新k，重复以上


方法二:
利用质因数分解。

如果我们将「1 次 Copy All + x 次 Paste」看做一次“动作”的话。
那么 一次“动作”所产生的效果就是将原来的字符串变为原来的 x + 1 倍。

    1. 起始对长度为 1 的记事本字符进行 1 次 Copy All + (k_1 - 1) 次 Paste 操作
    （消耗次数为 k_1，得到长度为 k_1的记事本长度）；
    
    2. 对长度为为 k_1的记事本字符进行 1 次 Copy All + (k_2 - 1) 次 Paste 操作
    （消耗次数为 k_1 + k_2，得到长度为 k_1 * k_2的记事本长度）
    ...

最终经过 k 次"动作"后，得到长度为 n 的记事本长度，即有：
    n = k_1 * k_2 *...* k_x
    
于是问题转化为: 对 n 进行质因数分解，使得 k_1 + k_2 + ... + k_x 最小    
e.g., n = 10 对应 n = 2 * 5 --> return 2+5
      n = 9 对应 n = 3*3 --> return 3+3
'''


class Solution:
    def minSteps(self, n: int) -> int:
        # 方法一
        if n == 1:
            return 0
        if n <= 3:
            return n

        ans = 2
        k = 2
        base = 1

        while k < n:
            if n % k == 0:
                base = k
                k *= 2
                ans += 2
            else:
                k += base
                ans += 1

        return ans

    def minSteps2(self, n: int) -> int:
        # 方法二
        ans = 0
        # 记事本已有长度
        i = 2
        while i * i <= n:
            while n % i == 0:
                # 更新 n 为 除剩下的数
                n //= i
                ans += i
            i += 1

        # 这里 n 是 分解剩下的
        if n > 1:
            ans += n

        return ans

