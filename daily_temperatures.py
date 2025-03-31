# time: O(n) | space: O(n)

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        
        # store indices of temp in decreasing order
        st = []

        # length of output - default 0 if no warmer days
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            # while the stack is not empty and the current temp is greater than the top of st
            while st and temperatures[st[-1]] < temperatures[i]:
                # result = current warmer day - previous day
                res[st[-1]] = i - st[-1]
                # found the warmer day so remove the previous day from the stack
                st.pop()
            # haven't found a warmer day yet
            st.append(i)
        return res
