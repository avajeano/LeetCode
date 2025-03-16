# time: O(n) | space: O(1)

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        candidate = None
        count = 0

        for num in nums:
            # if count is 0 set the candidate to num
            if count == 0:
                candidate = num
            # increment the count if num is the candidate otherwise decrement the count
            count += (1 if num == candidate else -1)
        return candidate
