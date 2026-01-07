from collections import deque

def WallOS(x,y, fav_num):
    result = x*x + 3*x + 2*x*y + y + y*y + fav_num
    countbinary = bin(result).count('1')
    if countbinary % 2 == 0:
        return True
    else:
        return False

def findshortestpath_with_directions(start_x, start_y, target_x, target_y, directions, label):
    queue = deque([(start_x,start_y,0)])
    visited = set()
    visited.add((start_x, start_y))
    
    while queue:
        x,y,steps = queue.popleft()
        if x == target_x and y == target_y:
            return steps
        for dx,dy in directions:
            new_x,new_y = x+dx, y+dy
            if new_x >= 0 and new_y >= 0 and (new_x,new_y) not in visited and WallOS(new_x,new_y,1364):
                queue.append((new_x,new_y, steps + 1))
                visited.add((new_x,new_y))
    return -1

# Test different direction orders
direction_sets = [
    ([(0,1),(1,0),(0,-1),(-1,0)], "Original: Down, Right, Up, Left"),
    ([(1,0),(0,1),(-1,0),(0,-1)], "Right, Down, Left, Up"),
    ([(-1,0),(0,-1),(1,0),(0,1)], "Left, Up, Right, Down"),
    ([(0,-1),(-1,0),(0,1),(1,0)], "Up, Left, Down, Right"),
]

print("Testing different direction orders:")
print("="*50)

for directions, label in direction_sets:
    result = findshortestpath_with_directions(1, 1, 31, 39, directions, label)
    print(f"{label}: {result} steps")

print("="*50)
print("All should give the same result: 86 steps")
