class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid == None:
            return 0

        cols = len(grid[0])
        rows = len(grid)
        visit = set()
        island = 0
        def bfs(r,c):
            q = collections.deque()
            q.append((r,c))
            visit.add((r,c))

            while q:
                m, n = q.popleft()
                directions = [(0,1), (0,-1), (1,0),(-1,0)]
                for dr,dc in directions:
                    row = m + dr
                    col = n + dc

                    if (row in range(rows) and col in range(cols)
                        and grid[row][col] == "1" and (row,col) not in visit):
                        q.append((row,col))
                        visit.add((row,col))
            

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r,c)
                    island = island + 1
        return island






