class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        res = [0] * n
        stack = []
        prev_time = 0

        for log in logs:
            parts = log.split(":")
            fn_id = int(parts[0])
            action = parts[1]
            timestamp = int(parts[2])

            if action == "start":
                if stack:
                    res[stack[-1]] += timestamp - prev_time
                stack.append(fn_id)
                prev_time = timestamp
            else:
                res[stack.pop()] += timestamp - prev_time + 1
                prev_time = timestamp + 1

        return res
