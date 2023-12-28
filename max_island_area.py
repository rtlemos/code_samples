"""
You are given an m x n binary matrix grid.
An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.)
You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0 or 1.
"""

from typing import List


def maxAreaOfIsland(grid: List[List[int]]) -> int:
    islands = []  # for validation, we record the coordinates of island grid cells
    m, n = len(grid), len(grid[0])  # number of latitude and longitude grid cells
    search_cells = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # down, up, left, right

    # recursive function that explores a newly discovered island
    def explore(y: int, x: int):
        for delta in search_cells:
            if (0 <= y + delta[0] < m and
                    0 <= x + delta[1] < n and
                    grid[y + delta[0]][x + delta[1]] == 1):
                new_y = y + delta[0]
                new_x = x + delta[1]
                islands[len(islands) - 1].append((new_y, new_x))
                grid[new_y][new_x] = 0
                explore(new_y, new_x)

    for la in range(m):
        for ln in range(n):
            if grid[la][ln] == 1:  # new island discovered
                islands.append([(la, ln)])
                grid[la][ln] = 0
                explore(la, ln)

    areas = [len(i) for i in islands]
    return max(areas) if len(areas) > 0 else 0


def maxAreaOfIslandSuccinct(grid: List[List[int]]) -> int:
    # succinct version
    m, n = len(grid), len(grid[0])

    def explore(y: int, x: int):
        if 0 <= y < m and 0 <= x < n and grid[y][x] == 1:
            grid[y][x] = 0
            return 1 + explore(y-1, x) + explore(y+1, x) + explore(y, x-1) + explore(y, x+1)
        else:
            return 0

    areas = [explore(y, x) for y in range(m) for x in range(n) if grid[y][x] == 1]
    return max(areas) if len(areas) > 0 else 0


def maxAreaOfIslandNotRecursive(grid: List[List[int]]) -> int:
    # useful for large grids, to avoid stack overflow
    data = np.array(grid)
    m, n = data.shape
    delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # down, up, left, right
    
    def explore(y, x):
        # adds valid land pixels to list of sought pixels
        search_cells = [[y + d[0], x + d[1]] for d in delta]
        seek.extend(
            [s for s in search_cells
             if 0 <= s[0] < m and 0 <= s[1] < n and data[s[0], s[1]] == 1])
    
    areas = []
    for la in range(m):
        for ln in range(n):
            if data[la, ln] == 1:  # new island discovered
                cnt = 1
                seek = []
                data[la, ln] = 0
                explore(la, ln)
                while len(seek) > 0:
                    sla, sln = seek.pop(0)
                    if data[sla, sln] == 1:  # new pixel within island
                        cnt += 1
                        data[sla, sln] = 0
                        explore(sla, sln)
                areas.append(cnt)

    max_area = max(areas) if len(areas) > 0 else 0
    return max_area


print(maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]))
print(maxAreaOfIslandSuccinct([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]))
print(maxAreaOfIsland([[0,0,0,0,0,0,0,0]]))
print(maxAreaOfIslandSuccinct([[0,0,0,0,0,0,0,0]]))
