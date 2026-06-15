class Solution(object):
    def waysToMakeFair(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_even = sum(nums[0::2])
        total_odd = sum(nums[1::2])

        prefix_even = 0
        prefix_odd = 0
        fair_count = 0

        for i, num in enumerate(nums):
            if i % 2 == 0:
                suffix_even = total_even - prefix_even - num
                suffix_odd = total_odd - prefix_odd
            else:
                suffix_even = total_even - prefix_even
                suffix_odd = total_odd - prefix_odd - num

            if prefix_even + suffix_odd == prefix_odd + suffix_even:
                fair_count += 1

            if i % 2 == 0:
                prefix_even += num
            else:
                prefix_odd += num

        return fair_count
