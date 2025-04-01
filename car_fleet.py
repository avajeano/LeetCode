# time: O(n long n) | space: O(n)

class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        
        # pair cars with their position and speed
        # reverse order allows us to loop through starting at the closest car to the target
        cars = sorted(zip(position, speed), reverse=True)

        # track fleets using a stack by storing time
        fleets = []

        # loop through unpacked car tuples 
        for pos, spd in cars:
            time = float(target - pos) / spd
            # if fleets is empty or the car cannot catch up 
            if not fleets or time > fleets[-1]:
                fleets.append(time)
        return len(fleets)
