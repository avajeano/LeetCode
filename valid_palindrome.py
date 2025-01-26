# time: O(n) | space: O(n)

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()

        s_clean = []

        for c in s:
            if c.isalnum():
                s_clean.append(c)
        
        s_string = ''.join(s_clean)

        if s_string == s_string[::-1]:
            return True
        else:
            return False
