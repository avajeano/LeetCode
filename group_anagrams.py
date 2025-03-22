# time: O(m * n) | space: O(m)

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        # char count to list of anagrams
        output = defaultdict(list)

        for s in strs:
            # a ... z
            count = [0] * 26

            for c in s:
                # setting the ASCII value
                count[ord(c) - ord("a")] += 1

            # using a tuple becuase a list cannot be a key in python
            output[tuple(count)].append(s)

        return output.values()
