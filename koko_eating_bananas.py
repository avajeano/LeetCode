# time: O(n * log m) | space: O(1)

class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        
        # initial minimum number of bananas per hour
        left = 1
        # maximum number of bananas per hour
        right = max(piles)
        res = right

        # looping through our predetermined speed range [1... max(piles)]
        while left <= right:
            # middle pile
            k = (left + right) // 2
            # initialize hours to 0
            hours = 0
            for p in piles:
                # sum how long it takes to eat each pile
                # round the number up
                hours += math.ceil(float(p) / k)
            
            # check if the calculated time it takes to eat all the bananas is under the given h
            if hours <= h:
                # update the minimum time it takes (k)
                res = min(res, k)
                # see if we can go slower
                right = k - 1
            else:
                # we need to go faster 
                left = k + 1

        return res
