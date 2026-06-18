class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s

        rev_s = s[::-1]
        combined = s + "#" + rev_s

        n = len(combined)
        table = [0] * n
        for i in range(1, n):
            j = table[i - 1]
            while j > 0 and combined[i] != combined[j]:
                j = table[j - 1]
            if combined[i] == combined[j]:
                j += 1
            table[i] = j

        pal_len = table[-1]

        return rev_s[: len(s) - pal_len] + s
