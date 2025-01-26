# time: O(n) | space: O(n)

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        # convert the string into an array of words 
        words = s.split(' ')

        # remove any empty string caused by trailing spaces
        words = list(filter(bool, words))    
        
        # return the length of the last word
        return len(words[-1]) if words else 0
