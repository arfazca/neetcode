from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q, fresh = self.initialize_grid(grid)
        if fresh == 0:
            return 0
        time = self.simulate_rotting(grid, q, fresh)
        return time if self.all_oranges_rotten(grid) else -1

    def initialize_grid(self, grid: List[List[int]]) -> tuple:
        q = deque()
        fresh = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))
        return q, fresh

    def simulate_rotting(self, grid: List[List[int]], q: deque, fresh: int) -> int:
        time = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while q:
            time += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if self.is_valid_fresh(grid, row, col):
                        grid[row][col] = 2
                        q.append((row, col))
                        fresh -= 1
            if fresh == 0:
                return time
        return time

    def is_valid_fresh(self, grid: List[List[int]], row: int, col: int) -> bool:
        return (0 <= row < len(grid) and
                0 <= col < len(grid[0]) and
                grid[row][col] == 1)

    def all_oranges_rotten(self, grid: List[List[int]]) -> bool:
        return all(cell != 1 for row in grid for cell in row)