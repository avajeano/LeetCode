time: O(n) | space: O(1)

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        left = 0 
        right = len(numbers) - 1

        while left <= right:
            curSum = numbers[left] + numbers[right]
            if curSum > target:
                right -= 1
            elif curSum < target:
                left += 1
            else:
                return [left + 1, right + 1]
