# time: O(n) | space: O(n)

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        stack = []
        # map to quickly find correct corresponding character. note: keys are closing brackets
        closed_map = {')':'(', '}':'{', ']':'['}


        for c in s:
            # it's a closing bracket
            if c in closed_map:
                if stack and stack[-1] == closed_map[c]:
                    # if the brackets match remove the bracket from the stack
                    stack.pop()                
            # it's an opening bracket so add it to the stack
            else: 
                stack.append(c)
        # if stack is empty all brackets were matched correctly and returns True
        return not stack
