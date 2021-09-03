# import heapq
from typing import List
from heapq import heappush, heappop
#
#
# class Solution:
#     def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
#         """顺序扫描优化"""
#         # s: [-height, right]
#         s = []
#         ans = []
#         cur = 0
#
#         for left, right, height in buildings:
#             # 如果队列有记录了，且队列记录的上一个最高的右端点在当前建筑的左边
#             while s and s[0][1] < left:
#                 '''
#                 Pop and return the smallest item from the heap, maintaining the heap invariant.
#                 If the heap is empty, IndexError is raised. To access the smallest item without popping it, use heap[0].
#                 '''
#                 rh, r = heapq.heappop(s)
#                 if r >= cur:
#                     if not s or rh != s[0][0]:
#                         while s and r > s[0][1]:
#                             heapq.heappop(s)
#                         rh = -s[0][0] if s else 0
#                         # 避免右端点重复
#                         if r == ans[-1][0]:
#                             ans[-1][1] = min(ans[-1][1], rh)
#                         else:
#                             ans.append([r, rh])
#                     cur = r
#
#             # 如果 s 为空 或者 当前高度大于队列中的右端点高度
#             if not s or height > -s[0][0]:
#                 # 避免左端点重复的问题
#                 if ans and left == ans[-1][0]:
#                     ans[-1][1] = height
#                 else:
#                     ans.append([left, height])
#
#             '''
#             heapq.heappush(heap, item):
#             Push the value item onto the heap, maintaining the heap invariant.
#             '''
#             heapq.heappush(s, [-height, right])
#         while s:
#             rh, r = heapq.heappop(s)
#             if r >= cur:
#                 if not s or rh != s[0][0]:
#                     while s and r > s[0][1]:
#                         heapq.heappop(s)
#                     rh = -s[0][0] if s else 0
#                     # 避免右端点重复
#                     if r == ans[-1][0]:
#                         ans[-1][1] = min(ans[-1][1], rh)
#                     else:
#                         ans.append([r, rh])
#                 cur = r
#         return ans



class Solution:

    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # 将每个需要扫描的点(房子的左右边缘)记录并排序
        scan_points = []

        for b in buildings:
            scan_points += [b[0], 0, b[2], b[1]], [b[1],1]

        scan_points.sort(key=lambda x: x[0])

        i = 0
        height_heap = [[0, float('inf')]] # 堆里先放入一个结束点为无穷，高度为0的记录，简化后面pop时的边界条件
        prev_height = 0
        key_points = []
        while(i < len(scan_points)):
            x = scan_points[i][0]
            # 清除已越过的队列顶端元素
            while(height_heap[0][1] <= x):
                heappop(height_heap)
            # 将该扫描点处起始的所有房屋高度入队列
            while(i < len(scan_points) and scan_points[i][0] == x):
                # == 0 则说明为起始点
                if scan_points[i][1] == 0:
                    heappush(height_heap, [-scan_points[i][2], scan_points[i][3]])
                i += 1

            # 如果此时的高度扫描点之前的高度不同则记录关键点(这应该是最简洁的处理方法了)
            if prev_height != -height_heap[0][0]:
                key_points.append([x, -height_heap[0][0]])
                prev_height = -height_heap[0][0]
        return key_points


if __name__ == "__main__":
    buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
    # for left, right, height in buildings:
    #     print(left, right, height)

    print(Solution().getSkyline(buildings))

    # for i in range(10):
    #
    #     if i == 4:
    #         continue
    #     print(i)