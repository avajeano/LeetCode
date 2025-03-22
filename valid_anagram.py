# time: O(n) | space: O(n)

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if len(s) != len(t):
            return False

        s_dict = {}
        t_dict = {}

        for c in s:
            if c not in s_dict:
                s_dict[c] = 1
            else:
                s_dict[c] += 1

        for c in t:
            if c not in t_dict:
                t_dict[c] = 1
            else:
                t_dict[c] += 1
        
        return s_dict == t_dict
