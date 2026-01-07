from collections import deque
import sys
import argparse

# AoC Day 24: Air Duct Spelunking (Part 1)
# Compute the fewest steps starting at 0 to visit all other digits at least once.


def read_grid(path: str):
    with open(path, 'r', encoding='utf-8') as f:
        lines = [line.rstrip('\n') for line in f if line.strip() != '']
    return lines


def find_digit_positions(grid):
    positions = {}
    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch.isdigit():
                positions[ch] = (r, c)
    return positions


def bfs_distances_from(grid, start):
    rows, cols = len(grid), len(grid[0])
    sr, sc = start
    q = deque([(sr, sc, 0)])
    visited = [[False] * cols for _ in range(rows)]
    visited[sr][sc] = True
    dists = {}
    while q:
        r, c, d = q.popleft()
        ch = grid[r][c]
        if ch.isdigit() and ch not in dists:
            dists[ch] = d
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                if grid[nr][nc] != '#':
                    visited[nr][nc] = True
                    q.append((nr, nc, d + 1))
    return dists


def build_distance_matrix(grid, digits, positions):
    # Returns dict-of-dicts: dist[a][b] = shortest steps
    dist = {}
    for a in digits:
        dist[a] = bfs_distances_from(grid, positions[a])
    return dist


def solve_part1(grid):
    positions = find_digit_positions(grid)
    digits = sorted(positions.keys(), key=lambda x: int(x))
    dist = build_distance_matrix(grid, digits, positions)

    n = len(digits)
    index_of = {d: i for i, d in enumerate(digits)}
    start = '0'
    start_idx = index_of[start]

    # Bitmask DP: dp[(mask, i)] = min steps to be at digit i having visited mask
    full_mask = (1 << n) - 1
    start_mask = 1 << start_idx
    dp = {(start_mask, start_idx): 0}

    for mask in range(full_mask + 1):
        for i in range(n):
            key = (mask, i)
            if key not in dp:
                continue
            cost = dp[key]
            from_digit = digits[i]
            for j in range(n):
                if mask & (1 << j):
                    continue  # already visited
                to_digit = digits[j]
                if from_digit in dist and to_digit in dist[from_digit]:
                    new_mask = mask | (1 << j)
                    new_cost = cost + dist[from_digit][to_digit]
                    nk = (new_mask, j)
                    if nk not in dp or new_cost < dp[nk]:
                        dp[nk] = new_cost

    # Minimal cost reaching any digit with all visited
    ans = min(dp[(full_mask, j)] for j in range(n) if (full_mask, j) in dp)
    return ans


def solve_part2(grid):
    # Same as part 1, but after visiting all digits, return to '0'.
    positions = find_digit_positions(grid)
    digits = sorted(positions.keys(), key=lambda x: int(x))
    dist = build_distance_matrix(grid, digits, positions)

    n = len(digits)
    index_of = {d: i for i, d in enumerate(digits)}
    start = '0'
    start_idx = index_of[start]

    full_mask = (1 << n) - 1
    start_mask = 1 << start_idx
    dp = {(start_mask, start_idx): 0}

    for mask in range(full_mask + 1):
        for i in range(n):
            key = (mask, i)
            if key not in dp:
                continue
            cost = dp[key]
            from_digit = digits[i]
            for j in range(n):
                if mask & (1 << j):
                    continue
                to_digit = digits[j]
                if from_digit in dist and to_digit in dist[from_digit]:
                    new_mask = mask | (1 << j)
                    new_cost = cost + dist[from_digit][to_digit]
                    nk = (new_mask, j)
                    if nk not in dp or new_cost < dp[nk]:
                        dp[nk] = new_cost

    # After visiting all, add cost to return to start '0'
    best = None
    for j in range(n):
        key = (full_mask, j)
        if key in dp:
            from_digit = digits[j]
            if from_digit in dist and start in dist[from_digit]:
                total = dp[key] + dist[from_digit][start]
                if best is None or total < best:
                    best = total
    return best if best is not None else -1


def main():
    parser = argparse.ArgumentParser(description="AoC Day 24: Air Duct Spelunking")
    parser.add_argument("input", help="Path to input file")
    parser.add_argument("--part", type=int, choices=[1, 2], default=1, help="Which part to solve (default: 1)")
    args = parser.parse_args()

    grid = read_grid(args.input)
    if args.part == 1:
        print(solve_part1(grid))
    else:
        print(solve_part2(grid))


if __name__ == "__main__":
    main()
