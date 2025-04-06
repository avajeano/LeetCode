# time: O(log m + log n) | space: O(1)

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
                
        Rows = len(matrix)
        # accessing first row column
        Cols = len(matrix[0])
        top = 0
        bottom = Rows - 1

        # search for the possible row
        while top <= bottom:
            # find the middle row
            row = (top + bottom) // 2

            # if target is greater than the largest value in this row
            if target > matrix[row][-1]:
                top = row + 1

            elif target < matrix[row][0]:
                bottom = row - 1

            else:
                break
        
        if not (top <= bottom):
            # none of the rows contains the target value
            return False
        
        row = (top + bottom) // 2
        left = 0
        right = Cols - 1

        # search within the row
        while left <= right:
            middle = (left + right) // 2
            if target > matrix[row][middle]:
                left = middle + 1
            elif target < matrix[row][middle]:
                right = middle - 1
            else:
                return True

        return False
