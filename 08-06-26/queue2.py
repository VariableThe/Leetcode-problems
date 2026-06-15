class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        total_time = 0

        for i in range(len(tickets)):
            if i <= k:
                total_time += min(tickets[i], tickets[k])
            else:
                total_time += min(tickets[i], tickets[k] - 1)

        return total_time
