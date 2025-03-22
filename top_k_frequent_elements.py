# time: O(n) | space: O(n)

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        count = {}
        # store the nums in order of frequency - max frequency equals length of nums
        freq = [[]for i in range(len(nums)+1)]
        output = []

        for num in nums:
            # if the num doesn't exist in count default to 0
            count[num] = 1 + count.get(num, 0)
        # return key value pair
        for n, c in count.items():
            # value n occurs c number of times
            freq[c].append(n)

        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                output.append(n)
                if len(output) == k:
                    return output
