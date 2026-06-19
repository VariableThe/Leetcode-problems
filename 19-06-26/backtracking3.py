class Solution(object):
    def getHappyString(self, n, k):
        res = []

        def backtrack(current_str):
            if len(current_str) == n:
                res.append(current_str)
                return

            for char in ["a", "b", "c"]:
                if not current_str or char != current_str[-1]:
                    backtrack(current_str + char)

        backtrack("")

        return res[k - 1] if k <= len(res) else ""
