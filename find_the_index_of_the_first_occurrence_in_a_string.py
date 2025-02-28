# time: O(m) | space: O(1)

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        return haystack.find(needle)
