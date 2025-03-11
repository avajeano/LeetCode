# time: O(n) | space: O(1)

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        # pointer 
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                # swaping/shifting non val elements to the front of the array
                nums[k] = nums[i]
                # counting/incrementing k
                k += 1
        return k 
