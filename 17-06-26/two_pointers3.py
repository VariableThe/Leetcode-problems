class Solution(object):
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n <= 3:
            return 1

        s = [1, 2, 2]
        head = 2
        next_num = 1

        while len(s) < n:
            count = s[head]

            s.extend([next_num] * count)
            next_num = 3 - next_num
            head += 1

        return s[:n].count(1)
