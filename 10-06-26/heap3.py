import heapq


class Solution(object):
    def isPossible(self, target):
        total = sum(target)
        heap = [-x for x in target]
        heapq.heapify(heap)

        while True:
            largest = -heapq.heappop(heap)
            rest = total - largest

            if largest == 1 or rest == 1:
                return True

            if rest == 0 or largest < rest or largest % rest == 0:
                return False

            new_val = largest % rest
            total = rest + new_val
            heapq.heappush(heap, -new_val)
