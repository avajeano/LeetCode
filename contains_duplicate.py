# time: O(n) | space: O(n)

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(set(nums)) != len(nums):
            return True
        else:
            return False
