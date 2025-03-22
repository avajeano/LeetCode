# time: O(n) | space: O(1)

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        total = sum(nums)
        # sum of the left side
        prefix = 0

        for i in range(len(nums)):
            postfix = total - prefix - nums[i]
            if prefix == postfix:
                return i
            prefix += nums[i]

        return -1
