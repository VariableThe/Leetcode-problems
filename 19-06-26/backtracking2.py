class Solution(object):
    def restoreIpAddresses(self, s):
        res = []
        if len(s) > 12 or len(s) < 4:
            return res

        def backtrack(start, parts):
            if len(parts) == 4:
                if start == len(s):
                    res.append(".".join(parts))
                return

            for i in range(1, 4):
                if start + i > len(s):
                    break

                segment = s[start : start + i]

                if (segment[0] == "0" and len(segment) > 1) or int(segment) > 255:
                    continue

                backtrack(start + i, parts + [segment])

        backtrack(0, [])
        return res
