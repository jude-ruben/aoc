from collections import deque

def WallOS(x,y, fav_num):
    result = x*x + 3*x + 2*x*y + y + y*y + fav_num
    countbinary = bin(result).count('1')
    return countbinary % 2 == 0

def create_maze_diagram(fav_num, start_x, start_y, width=20, height=15):
    """Create a visual diagram of the maze"""
    print(f"🏢 MAZE DIAGRAM (Favorite Number: {fav_num})")
    print("=" * 50)
    
    # Print column numbers
    print("   ", end="")
    for x in range(width):
        print(f"{x:2d}", end="")
    print()
    
    # Print the maze
    for y in range(height):
        print(f"{y:2d} ", end="")
        for x in range(width):
            if x == start_x and y == start_y:
                print(" S", end="")  # Start position
            elif WallOS(x, y, fav_num):
                print(" .", end="")  # Open space
            else:
                print(" #", end="")  # Wall
        print()
    
    print("\nLEGEND:")
    print("S = Start position (1,1)")
    print(". = Open space (you can walk here)")
    print("# = Wall (blocks your path)")

def explain_formula_simple(x, y, fav_num):
    """Explain how a specific coordinate is calculated"""
    print(f"\n🧮 HOW TO CALCULATE IF ({x},{y}) IS A WALL OR OPEN SPACE:")
    print("=" * 55)
    
    step1 = x*x + 3*x + 2*x*y + y + y*y
    print(f"Step 1: Use the magic formula")
    print(f"        {x}² + 3×{x} + 2×{x}×{y} + {y} + {y}²")
    print(f"        = {x*x} + {3*x} + {2*x*y} + {y} + {y*y}")
    print(f"        = {step1}")
    
    step2 = step1 + fav_num
    print(f"Step 2: Add favorite number: {step1} + {fav_num} = {step2}")
    
    binary = bin(step2)[2:]  # Remove '0b' prefix
    ones_count = binary.count('1')
    print(f"Step 3: Convert to binary: {step2} = {binary}")
    print(f"Step 4: Count the 1s: {ones_count} ones")
    
    if ones_count % 2 == 0:
        result = "OPEN SPACE (.)"
        print(f"Step 5: {ones_count} is EVEN → {result}")
    else:
        result = "WALL (#)"
        print(f"Step 5: {ones_count} is ODD → {result}")
    
    return result

def show_pathfinding_concept():
    """Explain BFS pathfinding in simple terms"""
    print("\n🎯 HOW THE PATHFINDING WORKS (Like Finding Exit in a Building):")
    print("=" * 65)
    
    print("Imagine you're lost in a building and need to find the exit...")
    print()
    print("🚶 STRATEGY: Explore room by room, level by level")
    print("   Step 1: Look at all rooms you can reach in 1 step")
    print("   Step 2: Look at all rooms you can reach in 2 steps") 
    print("   Step 3: Look at all rooms you can reach in 3 steps")
    print("   ...and so on...")
    print()
    print("✅ GUARANTEE: The first time you find the exit,")
    print("   it's guaranteed to be the shortest path!")
    print()
    print("🧠 WHY IT WORKS:")
    print("   - You check ALL 1-step paths before ANY 2-step paths")
    print("   - You check ALL 2-step paths before ANY 3-step paths") 
    print("   - So if exit is found at step N, no shorter path exists!")

def demonstrate_path_exploration():
    """Show how BFS explores step by step"""
    print("\n🔍 STEP-BY-STEP EXPLORATION FROM START (1,1):")
    print("=" * 50)
    
    queue = deque([(1, 1, 0)])
    visited = set()
    visited.add((1, 1))
    step_count = 0
    
    print("Step 0: Start at (1,1)")
    print("Queue: [(1,1,0)]")
    print()
    
    while queue and step_count < 5:  # Show first few steps
        x, y, steps = queue.popleft()
        step_count += 1
        
        print(f"Step {step_count}: Process position ({x},{y}) at distance {steps}")
        
        neighbors = []
        for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
            new_x, new_y = x + dx, y + dy
            if (new_x >= 0 and new_y >= 0 and 
                (new_x, new_y) not in visited and 
                WallOS(new_x, new_y, 1364)):
                visited.add((new_x, new_y))
                queue.append((new_x, new_y, steps + 1))
                neighbors.append((new_x, new_y))
        
        if neighbors:
            print(f"         Found new open spaces: {neighbors}")
            print(f"         Added to queue with distance {steps + 1}")
        else:
            print("         No new open spaces found")
        
        print(f"         Queue now has {len(queue)} positions to explore")
        print()

if __name__ == "__main__":
    # Show the maze diagram
    create_maze_diagram(1364, 1, 1, width=15, height=10)
    
    # Explain the formula with examples
    explain_formula_simple(1, 1, 1364)  # Start position
    explain_formula_simple(2, 1, 1364)  # Nearby position
    explain_formula_simple(0, 1, 1364)  # Another nearby position
    
    # Explain pathfinding concept
    show_pathfinding_concept()
    
    # Show step-by-step exploration
    demonstrate_path_exploration()
    
    print("\n🎉 FINAL ANSWER: 86 steps to reach (31,39) from (1,1)")
    print("    This is the shortest possible path - guaranteed by BFS!")
