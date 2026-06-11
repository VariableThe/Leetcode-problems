class Solution(object):
    def licenseKeyFormatting(self, s, k):
        s = s.replace("-", "").upper()

        first = len(s) % k
        parts = []

        if first:
            parts.append(s[:first])

        for i in range(first, len(s), k):
            parts.append(s[i : i + k])

        return "-".join(parts)
