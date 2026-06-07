class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        time = lambda x, y: (target - x) / y
        cars = sorted(zip(position, speed), reverse=True)

        for pos, spd in cars:
            stack.append(time(pos, spd))
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
            
        return len(stack)
