from collections import deque

def WallOS(x,y, fav_num):
    result = x*x + 3*x + 2*x*y + y + y*y + fav_num
    countbinary = bin(result).count('1')
    return countbinary % 2 == 0

def bfs_with_detailed_logging(start_x, start_y, target_x, target_y, max_steps=10):
    """
    BFS with detailed logging to show how it explores level by level
    """
    queue = deque([(start_x, start_y, 0)])
    visited = set()
    visited.add((start_x, start_y))
    
    step_count = 0
    current_level = 0
    
    print("=== BFS Exploration (Level by Level) ===")
    print(f"Level {current_level}: Starting at ({start_x},{start_y})")
    
    while queue and step_count < max_steps:
        x, y, steps = queue.popleft()
        
        # Show when we move to a new level
        if steps > current_level:
            current_level = steps
            print(f"\nLevel {current_level}: (All positions reachable in {current_level} steps)")
        
        print(f"  Processing ({x},{y}) at {steps} steps")
        
        if x == target_x and y == target_y:
            print(f"\n🎯 TARGET FOUND at ({x},{y}) in {steps} steps!")
            return steps
        
        # Explore neighbors
        neighbors_added = []
        for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
            new_x, new_y = x + dx, y + dy
            
            if (new_x >= 0 and new_y >= 0 and 
                (new_x, new_y) not in visited and 
                WallOS(new_x, new_y, 1364)):
                
                visited.add((new_x, new_y))
                queue.append((new_x, new_y, steps + 1))
                neighbors_added.append((new_x, new_y))
        
        if neighbors_added:
            print(f"    → Added neighbors: {neighbors_added}")
        
        step_count += 1
    
    return -1

# Demonstrate with a small example first
print("Let's see how BFS explores the maze step by step:")
print("(Showing first 20 steps of exploration)\n")

result = bfs_with_detailed_logging(1, 1, 7, 4, max_steps=20)
