# time: O(log n) | space: O(1)

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        left = 0
        right = len(nums) - 1

        # return mid when we find the target otherwise return -1
        
        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid

            # we're in the left sorted portion
            elif nums[left] <= nums[mid]:
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1 
            
            # we're in the right sorted portion
            else:
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
        
        return -1
