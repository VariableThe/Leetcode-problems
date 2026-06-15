class Solution(object):
    def minSubarray(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        target = sum(nums) % p

        if target == 0:
            return 0

        mod_map = {0: -1}
        current_sum = 0
        min_len = len(nums)

        for i, num in enumerate(nums):
            current_sum = (current_sum + num) % p

            needed_mod = (current_sum - target + p) % p

            if needed_mod in mod_map:
                min_len = min(min_len, i - mod_map[needed_mod])

            mod_map[current_sum] = i

        return min_len if min_len < len(nums) else -1
