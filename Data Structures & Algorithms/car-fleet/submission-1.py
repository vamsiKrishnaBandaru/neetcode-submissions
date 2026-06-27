class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        fleets = prevTime = 0

        for pos, spd in cars:
            time = (target - pos) / spd
            if time > prevTime:
                fleets += 1
                prevTime = time
        return fleets