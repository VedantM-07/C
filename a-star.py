import heapq

def astar(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    def heuristic(a, b): return abs(a[0]-b[0]) + abs(a[1]-b[1])
    
    open_list = [(0 + heuristic(start, goal), 0, start, [])]
    visited = set()

    while open_list:
        f, g, current, path = heapq.heappop(open_list)
        if current in visited:
            continue
        visited.add(current)
        path = path + [current]
        if current == goal:
            return path

        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:  # 4 directions
            nx, ny = current[0] + dx, current[1] + dy
            neighbor = (nx, ny)
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0 and neighbor not in visited:
                heapq.heappush(open_list, (g+1 + heuristic(neighbor, goal), g+1, neighbor, path))
    return None

# 0 = free, 1 = wall
grid = [
    [0, 0, 0, 0, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
goal = (4, 4)

path = astar(grid, start, goal)
print("Path found:" if path else "No path found.")
if path:
    for p in path:
        print(p)

'''
A Algorithm Overview*

A* is a search algorithm used in pathfinding and graph traversal. Its goal is to find a path from a starting node to a goal node while minimizing the total cost. It balances between:

    Cost to reach a node from the start (g).

    Estimated cost to reach the goal from the node (h, heuristic).

The total cost for a node is:
f(n)=g(n)+h(n)f(n)=g(n)+h(n)
Components in the Code

    Grid Representation

        0 represents a walkable cell.

        1 represents a wall (unwalkable).

    Heuristic Function

        Manhattan distance is used:
        h(a,b)=∣ax−bx∣+∣ay−by∣h(a,b)=∣ax​−bx​∣+∣ay​−by​∣

        This estimates the shortest distance between two points assuming no obstacles.

    Priority Queue (open list)

        Nodes are prioritized based on their f value.

    Visited Set

        Prevents reprocessing already visited nodes.

    Path Reconstruction

        Each node maintains the path taken to reach it, ensuring the algorithm returns the full path to the goal.

Execution Steps

    Initialization

        Start position is added to the open_list.

        Heuristic value (h) is calculated for the starting node.

    Main Loop

        Nodes are dequeued based on their f value.

        Neighbors are explored (up, down, left, right).

        Valid neighbors (not visited, not walls) are added to the open_list.

    Termination

        The loop ends when the goal node is dequeued or the open_list is empty.

    Output

        The path to the goal is returned if found, or None if no path exists.

Key Insights

    Optimality: A* guarantees the shortest path if the heuristic is admissible (never overestimates).

    Efficiency: The heuristic function directs the search toward the goal, avoiding unnecessary exploration.

    Flexibility: A* can work with various heuristics and grid types.


Detailed Explanation of A* Algorithm Execution

The A Algorithm* finds the shortest path from the start to the goal in a weighted grid by considering both the cost to reach a node (gg) and an estimate of the cost to the goal (hh, the heuristic). Here's a step-by-step walkthrough of how the algorithm works in this case:
1. Initialization

    Grid Representation: A 5x5 grid is defined:

[
    [0, 0, 0, 0, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0]
]

    0: Walkable cell.

    1: Wall (unwalkable cell).

Start Position: (0, 0) (top-left corner).

Goal Position: (4, 4) (bottom-right corner).

Heuristic Function: The Manhattan distance:

h(current, goal) = |x1 - x2| + |y1 - y2|

This estimates the distance between two points in the grid.

Data Structures:

    open_list: A priority queue storing nodes to explore. Each entry is a tuple (f, g, current, path):

        f=g+hf=g+h: Total estimated cost of the node.

        gg: Cost to reach this node from the start.

        current: The current grid cell being processed.

        path: The list of grid cells forming the path so far.

    Initially:

open_list = [(8, 0, (0, 0), [])]

h((0,0),(4,4))=8h((0,0),(4,4))=8.

visited: A set to store nodes already processed:

        visited = {}

2. Algorithm Execution

The main loop runs until the open_list is empty or the goal is found.
Iteration 1:

    Pop from open_list: Node (0, 0) with f=8,g=0,path=[]f=8,g=0,path=[].

    Mark (0, 0) as visited:

visited = {(0, 0)}

Update Path: path = [(0, 0)].

Explore Neighbors (using the four possible movements: up, down, left, right):

    (1, 0) (down): Wall. Skip.

    (0, 1) (right): Walkable. Calculate:

g = 1 (cost to move to (0, 1))
h = 7 (Manhattan distance to (4, 4))
f = g + h = 8

Add to open_list:

        open_list = [(8, 1, (0, 1), [(0, 0)])]

Iteration 2:

    Pop from open_list: Node (0, 1) with f=8,g=1,path=[(0,0)]f=8,g=1,path=[(0,0)].

    Mark (0, 1) as visited:

visited = {(0, 0), (0, 1)}

Update Path: path = [(0, 0), (0, 1)].

Explore Neighbors:

    (0, 2) (right): Walkable. Calculate:

g = 2
h = 6
f = 8

Add to open_list:

        open_list = [(8, 2, (0, 2), [(0, 0), (0, 1)])]

Iteration 3:

    Pop from open_list: Node (0, 2) with f=8,g=2,path=[(0,0),(0,1)]f=8,g=2,path=[(0,0),(0,1)].

    Mark (0, 2) as visited:

visited = {(0, 0), (0, 1), (0, 2)}

Update Path: path = [(0, 0), (0, 1), (0, 2)].

Explore Neighbors:

    (0, 3) (right): Walkable. Calculate:

g = 3
h = 5
f = 8

Add to open_list:

        open_list = [(8, 3, (0, 3), [(0, 0), (0, 1), (0, 2)])]

Subsequent Iterations:

    The algorithm continues similarly, exploring nodes and adding valid neighbors:

        (0, 3) → (0, 4) → (1, 4) → (2, 4) → (3, 4) → (4, 4).

        At each step:

            The node with the smallest ff value is processed.

            The path is updated, and neighbors are added to the open_list.

Final Iteration:

    Pop from open_list: Node (4, 4) with f=8,g=8,path=[(0,0),...,(3,4)]f=8,g=8,path=[(0,0),...,(3,4)].

    Goal Reached: The algorithm terminates, returning the complete path.

3. Output

The path found by the algorithm is:

[(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)]

    This path is the shortest route from (0, 0) to (4, 4) while avoiding walls.

Key Insights

    Efficient Search:

        The heuristic ensures nodes closer to the goal are prioritized, reducing unnecessary exploration.

    Path Cost:

        The cost gg accumulates as the path grows, ensuring only viable paths are pursued.

    Avoid Cycles:

        The visited set ensures each node is processed only once.

    Heuristic Influence:

        A well-designed heuristic (like Manhattan distance here) accelerates the search.

This explanation clarifies how the algorithm iteratively refines its path to achieve the goal.
'''
