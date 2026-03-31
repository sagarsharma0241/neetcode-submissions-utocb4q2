class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pos_speed = list(zip(position, speed))
        print(pos_speed)
        pos_speed.sort(key=lambda x: x[0], reverse=True)
        print(pos_speed)
        for p,s in pos_speed:
            d = target - p
            t = d/s
            stack.append(t)
            if stack and len(stack) >= 2 and stack[-1] <= stack[-2] :
                stack.pop()
        return len(stack)