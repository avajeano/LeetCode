# time: O(n) | space: O(n)

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # remove duplicates
        nums = set(nums)

        longest = 0

        for n in nums:
            # check if n is that start of a sequence by looking for its left neighbor
            if(n-1) not in nums:
                # length of sequence
                length = 0
                while (n + length) in nums:
                    # increment length while there is a consecutive sequence
                    length += 1
                    longest = max(length, longest)
        return longest
