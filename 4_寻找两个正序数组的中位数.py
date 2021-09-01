from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ordered_nums = []
        index_1 = 0
        index_2 = 0

        def mergeTwoList(ordered_nums,index_1,index_2,nums1,nums2):

            if index_1 == len(nums1): ordered_nums.extend(nums2[index_2:])
            elif index_2 == len(nums2): ordered_nums.extend(nums1[index_1:])
            else:

                if nums1[index_1] <= nums2[index_2]:
                    ordered_nums.append(nums1[index_1])
                    mergeTwoList(ordered_nums,index_1+1,index_2,nums1,nums2)
                else:
                    ordered_nums.append(nums2[index_2])
                    mergeTwoList(ordered_nums,index_1,index_2+1,nums1,nums2)

        mergeTwoList(ordered_nums,index_1,index_2,nums1,nums2)

        # 计算中位数
        mid_pos = len(ordered_nums)//2
        if len(ordered_nums)%2 == 0:
            # 长度为偶数
            mid_num = (ordered_nums[mid_pos-1] + ordered_nums[mid_pos])/2
        else:
            mid_num = ordered_nums[mid_pos]

        return mid_num


if __name__ == '__main__':
    print(len(str(2**31 -1)) )