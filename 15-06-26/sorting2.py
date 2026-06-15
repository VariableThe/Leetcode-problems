class Solution(object):
    def reductionOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()

        total_operations = 0
        current_level = 0

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                current_level += 1

            total_operations += current_level

        return total_operations
