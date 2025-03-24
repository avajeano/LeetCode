time: O(n2) | space: O(1)

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums.sort()
        res = []

        for i, x in enumerate(nums):
            # duplicate value
            if i > 0 and x == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                threeSum = x + nums[left] + nums[right]
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    res.append([x, nums[left], nums[right]])
                    left += 1
                    # check for duplicate and still less than right
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return res
