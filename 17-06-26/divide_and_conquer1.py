class Solution(object):
    def beautifulArray(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = [1]

        while len(res) < n:
            odds = [i * 2 - 1 for i in res]
            evens = [i * 2 for i in res]

            res = odds + evens

        return [i for i in res if i <= n]
