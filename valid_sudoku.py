# time: O(n2) | space: O(n2)

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        # hash set to keep track of duplicates
        columns = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        # key = (r//3, c//3)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                # check for duplicates in rows, columns and squares 
                if (board[r][c] in rows[r]
                or board[r][c] in columns[c]
                or board[r][c] in squares[(r//3, c//3)]):
                    return False
                # if there's not duplicates update the hash sets
                columns[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
        return True
