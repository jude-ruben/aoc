# AoC Day 24: Air Duct Spelunking

Compute the fewest steps to start at `0`, visit every other numbered location at least once, optionally returning to `0`.

## Run

- Part 1 (visit all numbers):

```pwsh
python bfs/day24/src/solve.py bfs/day24/data/input.txt --part 1
```

- Part 2 (visit all numbers and return to 0):

```pwsh
python bfs/day24/src/solve.py bfs/day24/data/input.txt --part 2
```

The program prints the minimal step count for the selected part.
