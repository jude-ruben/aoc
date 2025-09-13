from collections import deque

def WallOS(x,y, fav_num):
    result = x*x + 3*x + 2*x*y + y + y*y + fav_num
    countbinary = bin(result).count('1')
    if countbinary % 2 == 0:
        return True
    else:
        return False

def findshortestpath2(start_x, start_y, target_x, target_y):
    queue = deque([(start_x,start_y,0)])
    visited = set()
    visited.add((start_x, start_y))  # Add starting position to visited
    while queue:
        x,y,steps = queue.popleft()
        if steps == 50:
            return visited
        for dx,dy in [(0,1),(1,0),(0,-1),(-1,0)]:
            new_x,new_y = x+dx, y+dy
            if new_x >= 0 and new_y >= 0 and (new_x,new_y) not in visited and WallOS(new_x,new_y,1364):
                queue.append((new_x,new_y, steps + 1))
                visited.add((new_x,new_y))
    
    return -1

def findshortestpath(start_x, start_y, target_x, target_y):
    queue = deque([(start_x,start_y,0)])
    visited = set()
    visited.add((start_x, start_y))  # Add starting position to visited
    while queue:
        x,y,steps = queue.popleft()
        if x == target_x and y == target_y:
            return visited,steps
        for dx,dy in [(0,1),(1,0),(0,-1),(-1,0)]:
            new_x,new_y = x+dx, y+dy
            if new_x >= 0 and new_y >= 0 and (new_x,new_y) not in visited and WallOS(new_x,new_y,1364):
                queue.append((new_x,new_y, steps + 1))
                visited.add((new_x,new_y))
    
    return -1

if __name__ == "__main__":
    visited, result = findshortestpath(1,1,31,39)
    print("Part1 - Total steps:", result)
    visited2 = findshortestpath2(1,1,50,50)
    print("Part2 - Visited locations:", len(visited2))
