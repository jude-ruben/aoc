from collections import deque

def is_open_space(x, y, favorite_number):
    """
    Determine if a coordinate (x, y) is an open space or wall.
    Returns True if open space, False if wall.
    """
    if x < 0 or y < 0:
        return False  # Outside building
    
    # Calculate the value using the given formula
    value = x*x + 3*x + 2*x*y + y + y*y + favorite_number
    
    # Count the number of 1 bits in binary representation
    bit_count = bin(value).count('1')
    
    # Even number of 1s = open space, odd = wall
    return bit_count % 2 == 0

def visualize_maze(favorite_number, max_x=10, max_y=7):
    """
    Visualize the maze for debugging purposes.
    """
    print("  ", end="")
    for x in range(max_x):
        print(x, end="")
    print()
    
    for y in range(max_y):
        print(f"{y} ", end="")
        for x in range(max_x):
            if is_open_space(x, y, favorite_number):
                print(".", end="")
            else:
                print("#", end="")
        print()

def find_shortest_path(start_x, start_y, target_x, target_y, favorite_number):
    """
    Find the shortest path from start to target using BFS.
    Returns the number of steps, or -1 if no path exists.
    """
    if not is_open_space(start_x, start_y, favorite_number):
        return -1  # Can't start from a wall
    
    if not is_open_space(target_x, target_y, favorite_number):
        return -1  # Can't reach a wall
    
    # BFS setup
    queue = deque([(start_x, start_y, 0)])  # (x, y, steps)
    visited = set()
    visited.add((start_x, start_y))
    
    # Directions: up, down, left, right
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    
    while queue:
        x, y, steps = queue.popleft()
        
        # Check if we reached the target
        if x == target_x and y == target_y:
            return steps
        
        # Explore all possible moves
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            
            # Check bounds and if it's an open space
            if (new_x, new_y) not in visited and is_open_space(new_x, new_y, favorite_number):
                visited.add((new_x, new_y))
                queue.append((new_x, new_y, steps + 1))
    
    return -1  # No path found

def find_path_with_route(start_x, start_y, target_x, target_y, favorite_number):
    """
    Find the shortest path and return both the steps and the actual path.
    """
    if not is_open_space(start_x, start_y, favorite_number):
        return -1, []
    
    if not is_open_space(target_x, target_y, favorite_number):
        return -1, []
    
    # BFS setup with parent tracking
    queue = deque([(start_x, start_y, 0)])
    visited = set()
    visited.add((start_x, start_y))
    parent = {}  # To track the path
    parent[(start_x, start_y)] = None
    
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    
    while queue:
        x, y, steps = queue.popleft()
        
        if x == target_x and y == target_y:
            # Reconstruct path
            path = []
            current = (x, y)
            while current is not None:
                path.append(current)
                current = parent[current]
            path.reverse()
            return steps, path
        
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            
            if (new_x, new_y) not in visited and is_open_space(new_x, new_y, favorite_number):
                visited.add((new_x, new_y))
                parent[(new_x, new_y)] = (x, y)
                queue.append((new_x, new_y, steps + 1))
    
    return -1, []

def solve_part1():
    """
    Solve the puzzle: find shortest path from (1,1) to (31,39) with favorite number 1364.
    """
    favorite_number = 1364
    start_x, start_y = 1, 1
    target_x, target_y = 31, 39
    
    print(f"Finding shortest path from ({start_x},{start_y}) to ({target_x},{target_y})")
    print(f"Using favorite number: {favorite_number}")
    print()
    
    # Test with the example first
    print("Testing with example (favorite number 10):")
    visualize_maze(10)
    example_steps = find_shortest_path(1, 1, 7, 4, 10)
    print(f"Example path to (7,4): {example_steps} steps")
    print()
    
    # Solve the actual puzzle
    steps = find_shortest_path(start_x, start_y, target_x, target_y, favorite_number)
    
    if steps != -1:
        print(f"✓ Answer: {steps} steps required to reach ({target_x},{target_y})")
        
        # Get the actual path for verification
        steps_check, path = find_path_with_route(start_x, start_y, target_x, target_y, favorite_number)
        print(f"✓ Verification: Path length is {len(path)-1} steps (should match {steps})")
        
        # Show first few and last few coordinates of the path
        if len(path) > 10:
            print(f"Path starts: {path[:5]} ... ends: {path[-5:]}")
        else:
            print(f"Full path: {path}")
    else:
        print("No path found!")
    
    return steps

def count_reachable_locations(start_x, start_y, max_steps, favorite_number):
    """
    Count how many distinct locations can be reached in at most max_steps.
    This is commonly needed for Part 2 of AoC puzzles.
    """
    if not is_open_space(start_x, start_y, favorite_number):
        return 0
    
    queue = deque([(start_x, start_y, 0)])
    visited = set()
    visited.add((start_x, start_y))
    reachable = set()
    reachable.add((start_x, start_y))
    
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    
    while queue:
        x, y, steps = queue.popleft()
        
        if steps < max_steps:
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                
                if (new_x, new_y) not in visited and is_open_space(new_x, new_y, favorite_number):
                    visited.add((new_x, new_y))
                    reachable.add((new_x, new_y))
                    queue.append((new_x, new_y, steps + 1))
    
    return len(reachable)

def solve_both_parts():
    """
    Solve both parts of the puzzle.
    """
    favorite_number = 1364
    start_x, start_y = 1, 1
    target_x, target_y = 31, 39
    
    print("=== Day 13: A Maze of Twisty Little Cubicles ===")
    print(f"Favorite number: {favorite_number}")
    print(f"Starting position: ({start_x},{start_y})")
    print()
    
    # Test with the example first
    print("Testing with example (favorite number 10):")
    visualize_maze(10)
    example_steps = find_shortest_path(1, 1, 7, 4, 10)
    print(f"Example path to (7,4): {example_steps} steps (expected: 11)")
    print()
    
    # Part 1: Find shortest path to target
    print("=== Part 1 ===")
    steps = find_shortest_path(start_x, start_y, target_x, target_y, favorite_number)
    
    if steps != -1:
        print(f"✓ Answer: {steps} steps required to reach ({target_x},{target_y})")
        
        # Get the actual path for verification
        steps_check, path = find_path_with_route(start_x, start_y, target_x, target_y, favorite_number)
        print(f"✓ Verification: Path length is {len(path)-1} steps")
        
        if len(path) > 10:
            print(f"Path preview: {path[:3]} ... {path[-3:]}")
    else:
        print("No path found!")
    
    print()
    
    # Part 2: Count reachable locations (common AoC pattern)
    print("=== Part 2 (Bonus) ===")
    max_steps = 50
    reachable_count = count_reachable_locations(start_x, start_y, max_steps, favorite_number)
    print(f"Locations reachable in at most {max_steps} steps: {reachable_count}")
    
    return steps, reachable_count

if __name__ == "__main__":
    solve_both_parts()
