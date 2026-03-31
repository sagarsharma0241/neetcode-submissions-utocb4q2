class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                prev_id, prev_temp = stack.pop()
                res[prev_id] = i - prev_id
            stack.append([i,temp])
        return res
