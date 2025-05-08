class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        # edge case
        if not strs:
            return ""

        # we assume maybe the first word is the common prefix 
        prefix = strs[0]

        # start iterating over the rest of the strings
        for s in strs[1:]:
            while not s.startswith(prefix):
                # if it doesn't start with the prefix we shorten the prefix 
                prefix = prefix[:-1]

                # if we removed all the characters from the prefix we return an empty string 
                if not prefix:
                    return ""
        return prefix
