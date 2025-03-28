# time: O(n) | space: O(1)

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        i = 0
        j = len(height) - 1

        res = 0

        while i < j:
            area = (j - i) * min(height[i], height[j])
            # find the greater value and update res
            res = max(res, area)

            if height[i] < height[j]:
                i += 1
            else:
                j -=1
        return res
