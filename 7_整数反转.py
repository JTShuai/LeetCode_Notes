class Solution:
    def reverse(self, x: int) -> int:

        MAX_INT = 2 ** 31 - 1
        MIN_INT = -2 ** 31
        boudary_len = len(str(MAX_INT))
        sign = 1

        def reverseStr(s:str) -> str:
            res = ''
            k = len(s)//2
            str_nums = [_ for _ in s]
            for i in range(k):
                str_nums[i], str_nums[-(i+1)] = str_nums[-(i+1)], str_nums[i]

            for char_num in str_nums:
                res+= char_num

            return res

        def deleteZero(x:int) -> str:
            str_x = str(x)
            while(str_x[-1] == '0'):
                str_x = str_x[:-1]

            return str_x

        if x == 0:
            return 0

        if x < 0:
            sign = -1

        x = sign * x

        # 去除尾部的零
        str_x = deleteZero(x)

        if len(str_x) <= boudary_len:
            str_x = reverseStr(str_x)

            if MIN_INT <= int(str_x) * sign <= MAX_INT:
                return int(str_x) * sign
            else:
                return 0
        else:
            return 0


'''
更简洁的做法，不需要反转完再判断是否溢出，而是反转的过程中判断
'''

def new_reverse(x: int) -> int:
    res = 0
    sign = 1
    if x < 0:
        sign = -1

    x1 = x*sign

    MAX_INT = 2 ** 31 - 1
    MIN_INT = -2 ** 31

    i = 0
    bits = len(str(x1))

    while(x1!=0):

        #   对10取余数，得到末尾的数字
        temp = x1%10
        k = bits - i -1
        if sign == 1:
            if (res*10 +temp)*(10**k)>MAX_INT:
                return 0
        if sign == -1:
            if (res*10 +temp)*(10**k)*sign < MIN_INT:
                return 0

        # if res > 214748364 or (res==214748364 and temp>7):
        #     return 0
        # if res<-214748364 or (res==-214748364 and temp<-8):
        #     return 0

        res = res*10 +temp
        i +=1
        x1 //=10

    return res*sign

if __name__ == '__main__':
    # print(Solution().reverse(123))
    # print( [_ for _ in '123' ])
    print(new_reverse(123))