# Advent of Code - Day 13: A Maze of Twisty Little Cubicles

## Problem Description

You're in a maze of cubicles where each coordinate (x,y) is either a wall or open space, determined by a mathematical formula:

1. Calculate: `x*x + 3*x + 2*x*y + y + y*y + favorite_number`
2. Count the number of 1s in the binary representation
3. Even count = open space (.), odd count = wall (#)

**Part 1**: Find the shortest path from (1,1) to (31,39) with favorite number 1364.

## Solution

The solution uses **Breadth-First Search (BFS)** to find the shortest path in the maze.

### Key Components:

1. **`is_open_space(x, y, favorite_number)`**: Determines if a coordinate is passable
2. **`find_shortest_path()`**: BFS implementation to find minimum steps
3. **`find_path_with_route()`**: Enhanced version that returns the actual path
4. **`visualize_maze()`**: Helper function to visualize small sections of the maze

### Results:

- **Example verification**: Path from (1,1) to (7,4) with favorite number 10 = 11 steps ✓
- **Answer**: **86 steps** required to reach (31,39) with favorite number 1364

### Algorithm Complexity:

- **Time**: O(V + E) where V is visited nodes and E is edges
- **Space**: O(V) for the visited set and queue
- **Optimized**: Only explores reachable coordinates, doesn't pre-generate the entire maze

## Files:

- `day13.py`: Complete solution with visualization and path verification

## Usage:

```bash
python day13.py
```

The script will:
1. Verify the example case
2. Solve Part 1 and display the answer
3. Show path verification
4. Calculate reachable locations for a bonus Part 2
