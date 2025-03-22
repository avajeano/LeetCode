# time: O(n) | space: O(n)

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        # initialize a list to the length of nums
        output = [1] * len(nums)
        # to calculate before current index
        prefix = 1
        # to calculate after current index
        postfix = 1

        # loop through left to right
        for i in range(len(nums)):
            # stores prefix product in output
            output[i] = prefix
            # update prefix to include current element for the next index
            prefix *= nums[i]

        # loop through right to left
        for i in range(len(nums) -1, -1, -1):
            # multiplies prefix product with with postfix product
            output[i] *= postfix
            # update postfix to include current element for the next index
            postfix *= nums[i]
        
        return output
