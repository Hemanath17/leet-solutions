class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        pacific = set()
        atlantic = set()
        def dfs(r,c,visited):
            visited.add((r,c))
            directions = [
                (-1,0),
                (1,0),
                (0,-1),
                (0,1)
            ]
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if nr<0 or nr>=rows or nc<0 or nc>=cols:
                    continue
                if (nr,nc) in visited:
                    continue
                if heights[nr][nc]<heights[r][c]:
                    continue
                dfs(nr,nc,visited)
        for c in range(cols):
            dfs(0,c,pacific)
        for r in range(rows):
            dfs(r,0,pacific)
        for c in range(cols):
            dfs(rows-1,c,atlantic)
        for r in range(rows):
            dfs(r,cols-1,atlantic)
        result = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pacific and (r,c) in atlantic:
                    result.append([r,c])
        return result