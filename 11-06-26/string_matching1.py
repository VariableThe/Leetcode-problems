class Solution(object):
    def repeatedSubstringPattern(self, s):
        for i in range(1, len(s) // 2 + 1):
            if len(s) % i == 0:
                if s[:i] * (len(s) // i) == s:
                    return True
        return False
