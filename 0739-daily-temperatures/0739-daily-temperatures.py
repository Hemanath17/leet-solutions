class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []
        for i in range(n):
            current_temp = temperatures[i]
            while stack and temperatures[stack[-1]] < current_temp:
                waiting_day = stack.pop()
                res[waiting_day] = i- waiting_day
            stack.append(i)
        return res