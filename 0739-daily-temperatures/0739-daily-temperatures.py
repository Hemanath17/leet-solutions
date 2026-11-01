class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for r in range(len(temperatures)):
            while stack and temperatures[r]>temperatures[stack[-1]]:
                prev = stack.pop()
                res[prev] = r-prev
            stack.append(r)
        return res