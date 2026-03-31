class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None: 
        ROWS = len(grid)
        COLS = len(grid[0])
        visit = set()
        q = collections.deque()
        dist = 0
        
        def addRow(r,c):
            if (r < 0 or r == ROWS or c < 0 or c == COLS or
            grid[r][c] == -1 or (r,c) in visit):
                return
            q.append((r,c))
            visit.add((r,c))


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append( (r,c))
                    visit.add((r,c))
        

        while q:
            for i in range(len(q)):
                (r,c) = q.popleft()
                grid[r][c] = dist
                addRow(r-1,c)
                addRow(r+1,c)
                addRow(r,c-1)
                addRow(r,c+1)
            dist = dist + 1


