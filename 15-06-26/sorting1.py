class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr.sort()

        min_diff = float("inf")
        result = []

        for i in range(1, len(arr)):
            current_diff = arr[i] - arr[i - 1]

            if current_diff < min_diff:
                min_diff = current_diff
                result = [[arr[i - 1], arr[i]]]
            elif current_diff == min_diff:
                result.append([arr[i - 1], arr[i]])

        return result
