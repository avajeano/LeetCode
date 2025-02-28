# time: O(n²) | space: O(1)

class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # count number of good pairs starting at zero
        count = 0

        # loop through all pairs where i < j
        for i in range(len(nums)):
            # j starts i+1
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    count += 1
        return count
