from pathlib import Path
from collections import deque
import itertools

def bfs_distances_from(grid, start):
    rows, cols = len(grid), len(grid[0])
    sr, sc = start

    #Initialize BFS
    q = deque([(sr, sc, 0)])
    visited = [[False] * cols for _ in range(rows)]
    visited[sr][sc] = True
    dists = {}

    while q:
        r,c,d = q.popleft()
        ch = grid[r][c]
        if ch.isdigit() and ch not in dists:
            dists[ch] = d

        for dr, dc in ((-1,0),(1,0),(0,-1),(0,1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                if grid[nr][nc] != '#':
                    visited[nr][nc] = True
                    q.append((nr, nc, d + 1))
    return dists

def load_file(path: str = "input.txt") -> None:
    data_path = Path(__file__).parent.parent / "data" / path
    lines = data_path.read_text().strip().splitlines()
    grid = [list(row) for row in lines]
    #print(grid)
    vents = {}
    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch.isdigit():
                vents[ch] = (r, c)
    #print(vents)
    return grid,vents


if __name__ == "__main__":
    grid, positions = load_file()
    # Compute pairwise distances between all numbered locations
    def compute_all_pairwise_distances(grid, vents):
        all_d = {}
        for k, pos in vents.items():
            all_d[k] = bfs_distances_from(grid, pos)
        return all_d

    def shortest_path_length(vents, dists, return_to_start=False):
        nodes = [k for k in vents.keys() if k != '0']
        best_path = None
        best_cost = 10**18
        for perm in itertools.permutations(nodes):
            total = 0
            cur = '0'
            ok = True
            for nxt in perm:
                if nxt not in dists[cur]:
                    ok = False
                    break
                total += dists[cur][nxt]
                cur = nxt
            if not ok:
                continue
            if return_to_start:
                if '0' not in dists[cur]:
                    continue
                total += dists[cur]['0']
            if total < best_cost:
                best_cost = total
                best_path = ('0',) + perm + (( '0',) if return_to_start else ())
        return best_path, best_cost

    all_dists = compute_all_pairwise_distances(grid, positions)
    p1_path, p1_cost = shortest_path_length(positions, all_dists, return_to_start=False)
    p2_path, p2_cost = shortest_path_length(positions, all_dists, return_to_start=True)

    print(f"Part 1: cost={p1_cost}, path={p1_path}")
    print(f"Part 2: cost={p2_cost}, path={p2_path}")