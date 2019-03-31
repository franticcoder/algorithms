# Leetcode : 857. Minimum Cost to Hire K Workers
#
# Author: Chungmin Kim
# Date: Mar 31, 2019
# https://leetcode.com/problems/minimum-cost-to-hire-k-workers/?fbclid=IwAR25yrFvZDHbWk-cDLlrXkgVB295nhIbQ5FO0my_IE_fFrxGX-Scbmx3yiU


import heapq

class Solution:

    def mincostToHireWorkers(self, quality: 'List[int]', wage: 'List[int]', K: 'int') -> 'float':

        if K == 1:
            return min(wage)

        min_cost = float('inf')
        myheap = []
        sum_q = 0

        # define list of tuple(ratio, wage, quality)
        # and sort the list by the ratio in ascending order
        sets = [(w/q, w, q) for w, q in zip(wage, quality)]
        sets = sorted(sets, key=lambda r: r[0])

        # Since we are calculating the minimum cost, we have to take the smallest ratio value frist.
        # Calculate the min_cost until the end of list.
        for set in sets:
            _ratio, _wage, _quality = set

            # Higher quality will have higher cost, so we go through
            # by removing the highest quality from the heap

            # push into the heap and max_heapify
            heapq.heappush(myheap, _quality)
            heapq._heapify_max(myheap)

            sum_q += _quality

            if len(myheap) > K :
                # pop(remove) the largest quality from the heap
                sum_q -= heapq.heappop(myheap)

            if len(myheap) == K:
                min_cost = min(min_cost, sum_q * _ratio )


        return min_cost


def test1():
    q = [10, 20, 5]
    w = [70, 50, 30]

    sol = Solution()
    print(sol.mincostToHireWorkers(q, w, 2))


def test2():
    q = [3, 1, 10, 10, 1]
    w = [4, 8, 2, 2, 7]
    sol = Solution()
    print(sol.mincostToHireWorkers(q, w, 3))


test1()
test2()



