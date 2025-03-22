# time: O(n) | space: O(n)

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        # total count of subarrays 
        res = 0
        curSum = 0
        # when the subarray starts at index 0 the prefix sum is 0 atleast once
        prefixSum = {0:1}

        for n in nums:
            curSum += n
            diff = curSum - k

            # if the diff exists in prefixSum then we know that there's a subarray that ends at the current index
            res += prefixSum.get(diff, 0)

            # adding curSum to the prefixSum map
            prefixSum[curSum] = 1 + prefixSum.get(curSum, 0)

        return res
