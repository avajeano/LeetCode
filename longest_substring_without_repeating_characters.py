# time: O(n) | space: O(n)

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        result = 0
        # keep track of duplicates in the substrings
        characterSet = set()
        left = 0

        for right in range(len(s)):
            # while the character is in our set we will update out sliding window
            while s[right] in characterSet: 
                characterSet.remove(s[left])
                left += 1
            # after we've removed all duplicates we'll add the right most character to our set
            characterSet.add(s[right])
            result = max(result, right - left + 1)
        return result
