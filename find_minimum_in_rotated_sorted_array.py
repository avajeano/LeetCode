# time: O(log n) | space: O(1)

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        result = nums[0]
        left = 0
        right = len(nums) - 1

        while left <= right:
            # if array is already sorted
            if nums[left] < nums[right]:
                result = min(result, nums[left])
                break

            middle = (left + right) // 2 
            result = min(result, nums[middle])
            if nums[middle] >= nums[left]:
                left = middle + 1
            else:
                right = middle - 1
        return result
