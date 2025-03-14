# time: O(n) | space: O(1)

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

       # start from the last index, traverse backwards, stop at index 0
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # edge case for 9
            digits[i] = 0
        # carry the one
        digits = [1] + digits
        return digits
