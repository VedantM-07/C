def dfs_recursive(node, graph, visited):
    
    visited.add(node)
    print(node, end=" ")  # Print node in traversal order
    
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_recursive(neighbor, graph, visited)

def dfs(graph, start_vertex):
    visited = set()
    print(f"\nDFS Traversal starting from vertex {start_vertex}: ", end="")
    if start_vertex in graph:
        dfs_recursive(start_vertex, graph, visited)
    for node in graph:
        if node not in visited:
            dfs_recursive(node, graph, visited)

n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))
graph = {i: [] for i in range(n)}   

print("Enter edges (format: u v):")
for _ in range(e):
   u, v = map(int, input().split())
   graph[u].append(v)
   graph[v].append(u)  # Undirected graph

start_vertex = int(input("Enter starting vertex: "))
dfs(graph, start_vertex)


"""
🎯 Problem Statement
Implement a solution for Depth-First Search (DFS) using a recursive algorithm for an undirected graph to traverse all vertices, as per Assignment No: 01 (Laboratory Practice II).

🔍 1. What is Depth-First Search (DFS)?
📌 Definition:
DFS is an algorithm for traversing or searching tree or graph data structures. It starts at a selected node and explores as far as possible along each branch before backtracking. It uses a stack (implicitly via recursion) to keep track of vertices to explore.

👨‍💻 In This Context:
- Variables: Vertices of the graph.
- Goal: Visit all vertices exactly once, printing the traversal order.
- Constraint: Avoid revisiting vertices to prevent cycles in the undirected graph.

🖼️ 2. What is Graph Traversal?
Graph traversal involves visiting all vertices systematically. DFS achieves this by:
- Exploring one neighbor deeply before moving to the next.
- Using a visited set to track processed vertices.
- Backtracking when no unvisited neighbors remain.

✅ Real-world Applications:
- Pathfinding: Finding paths between nodes (e.g., maze solving).
- Topological Sorting: Ordering tasks with dependencies.
- Cycle Detection: Identifying cycles in graphs (e.g., deadlock detection).
- Connected Components: Finding isolated subgraphs in networks.

🧩 3. Core Concepts and Algorithms Used
🔷 A. Recursive DFS Algorithm
- Definition: DFS uses recursion to explore vertices, implicitly using the call stack as a stack data structure.
- Steps:
  1. Mark the current vertex as visited and print it.
  2. Recursively visit all unvisited neighbors.
  3. Backtrack when no unvisited neighbors remain.
- The recursion ensures a depth-first exploration, prioritizing deeper paths.

🔷 B. Graph Representation (Adjacency List)
- We use an adjacency list:
  ```python
  graph = {
      0: [1, 2],
      1: [0, 3, 4],
      2: [0, 3],
      3: [1, 2],
      4: [1]
  }
  ```
- Each key is a vertex, and the value is a list of adjacent vertices.
- Space-efficient for sparse graphs and easy to iterate over neighbors.

📊 4. Complexity Analysis
⏳ Time Complexity:
- O(V + E), where V is the number of vertices and E is the number of edges.
- Each vertex is visited once (O(V)).
- Each edge is checked once across all adjacency lists (O(E)).

💾 Space Complexity:
- O(V) for the visited set.
- O(V) for the recursion stack in the worst case (e.g., a linear graph).
- Total: O(V).

⚙️ 5. How the Code Works (Flow Summary)
Step | Description
-----|------------
1    | User inputs number of vertices, edges, and starting vertex.
2    | Graph is built using an adjacency list from edge inputs.
3    | A visited set is initialized.
4    | dfs() is called, starting from the user-specified vertex.
5    | dfs_recursive() visits a vertex, prints it, and explores unvisited neighbors.
6    | If a component is fully explored, dfs() checks for unvisited vertices.
7    | The traversal order is printed.

🔸 6. Line-by-Line Explanation
Below is the explanation for each line of code.

# Line 1: # Depth-First Search (DFS) Implementation for Undirected Graph using Recursion
- Comment describing the purpose of the file.

# Line 3: def dfs_recursive(node, graph, visited):
- Defines the recursive DFS function with parameters: node (current vertex), graph (adjacency list), visited (set of visited vertices).

# Line 4:    #Recursively perform DFS starting from the given node."
#- Docstring explaining the function’s purpose.

# Line 5:     visited.add(node)
- Adds the current node to the visited set to mark it as processed.

# Line 6:     print(node, end=" ")  # Print node in traversal order
- Prints the current node as part of the traversal output, with a space separator.

# Line 7:     
- Empty line for readability.

# Line 8:     for neighbor in graph[node]:
- Iterates over all neighbors of the current node from the adjacency list.

# Line 9:         if neighbor not in visited:
- Checks if the neighbor has not been visited.

# Line 10:             dfs_recursive(neighbor, graph, visited)
- Recursively calls dfs_recursive on the unvisited neighbor.

# Line 11:
- Empty line for readability.

# Line 12: def dfs(graph, start_vertex):
- Defines the driver function to initialize DFS, with parameters: graph (adjacency list), start_vertex (starting vertex).

# Line 13:     "Initialize DFS traversal and handle disconnected components."
#- Docstring explaining the function’s purpose.

# Line 14:     visited = set()
- Initializes an empty set to track visited vertices.

# Line 15:     print(f"\nDFS Traversal starting from vertex {start_vertex}: ", end="")
- Prints the starting message for the traversal, with no newline.

# Line 16:     
- Empty line for readability.

# Line 17:     if start_vertex in graph:
- Checks if the start_vertex exists in the graph.

# Line 18:         dfs_recursive(start_vertex, graph, visited)
- Calls dfs_recursive to start DFS from the given vertex.

# Line 19:     
- Empty line for readability.

# Line 20:     for node in graph:
- Iterates over all vertices in the graph.

# Line 21:         if node not in visited:
- Checks if the vertex has not been visited.

# Line 22:             dfs_recursive(node, graph, visited)
- Calls dfs_recursive on unvisited vertices to handle disconnected components.

# Line 23:     
- Empty line for readability.

# Line 24:     print()
- Prints a newline after the traversal output.

# Line 25:
- Empty line for readability.

# Line 26: # Main Program with Input
- Comment indicating the start of the main program.

# Line 27: if __name__ == "__main__":
- Checks if the script is run directly (not imported as a module).

# Line 28:     n = int(input("Enter number of vertices: "))
- Prompts user to input the number of vertices and converts it to an integer.

# Line 29:     e = int(input("Enter number of edges: "))
- Prompts user to input the number of edges and converts it to an integer.

# Line 30:     graph = {i: [] for i in range(n)}
- Initializes an adjacency list as a dictionary with vertices 0 to n-1, each with an empty list.

# Line 31:
- Empty line for readability.

# Line 32:     print("Enter edges (format: u v):")
- Prompts user to input edges.

# Line 33:     for _ in range(e):
- Loops e times to read edge inputs.

# Line 34:         u, v = map(int, input().split())
- Reads two integers (u, v) representing an edge, split from user input.

# Line 35:         graph[u].append(v)
- Adds vertex v to the adjacency list of vertex u.

# Line 36:         graph[v].append(u)  # Undirected graph
- Adds vertex u to the adjacency list of vertex v (bidirectional edge).

# Line 37:
- Empty line for readability.

# Line 38:     start_vertex = int(input("Enter starting vertex: "))
- Prompts user to input the starting vertex and converts it to an integer.

# Line 39:     dfs(graph, start_vertex)
- Calls the dfs function to perform the traversal.

🔸 7. Functional Explanation

`dfs_recursive(node, graph, visited)`
- **Purpose**: Recursively traverses the graph starting from `node` using DFS.
- Marks the current node as visited and prints it.
- Iterates through neighbors, recursing on unvisited ones.
- Uses the recursion stack to backtrack when no unvisited neighbors remain.

`dfs(graph, start_vertex)`
- **Purpose**: Initializes DFS and ensures all vertices are visited, including in disconnected graphs.
- Creates a visited set.
- Starts DFS from the given vertex if valid.
- Checks for unvisited vertices to handle disconnected components.
- Prints the traversal output.

`Main Program`
- Accepts user input for vertices, edges, and starting vertex.
- Builds the graph as an adjacency list.
- Calls dfs() to perform the traversal.

🧠 8. Alignment with Assignment
- **Recursive Algorithm**: Uses recursion for DFS, as specified.
- **Undirected Graph**: Handles bidirectional edges.
- **Traversal**: Prints all vertices in DFS order.
- **Complexity**: Matches document’s O(V + E) time and O(V) space.
- **Example**: User input allows testing with any graph, demonstrating traversal.
- **Pseudocode**: Follows the document’s pseudocode (mark node, recurse on unvisited neighbors).

📌 9. Viva-Style Questions and Answers
1. **What is DFS, and how does it differ from BFS?**
   - DFS explores as far as possible along a branch before backtracking, using a stack. BFS explores all neighbors at the current depth before moving deeper, using a queue. DFS is better for deep searches; BFS for shortest paths.

2. **Why use a visited set in DFS?**
   - To prevent revisiting vertices, which could cause infinite loops in cyclic graphs.

3. **What is the time complexity of this DFS implementation?**
   - O(V + E), as each vertex and edge is processed once.

4. **How does the recursion stack work in DFS?**
   - Each recursive call adds a vertex to the stack. When no unvisited neighbors remain, the function returns, popping the vertex.

5. **Can DFS handle disconnected graphs?**
   - Yes, the code checks for unvisited vertices after the initial DFS, starting new DFS calls for disconnected components.

6. **Why use an adjacency list instead of an adjacency matrix?**
   - Adjacency lists are more space-efficient for sparse graphs and faster for iterating over neighbors.

7. **What happens if the start vertex doesn’t exist?**
   - The code checks if the start vertex is in the graph, skipping the initial DFS if invalid, and proceeds to check other vertices.

8. **How does DFS ensure all vertices are visited?**
   - By iterating over all vertices after the initial DFS and calling dfs_recursive() on unvisited ones.

9. **What are some applications of DFS?**
   - Pathfinding, cycle detection, topological sorting, and finding connected components.

10. **Is DFS guaranteed to find the shortest path?**
    - No, DFS does not guarantee the shortest path; BFS is used for that purpose.

📊 10. Example Run
Input:
```
Enter number of vertices: 5
Enter number of edges: 5
Enter edges (format: u v):
0 1
0 2
1 3
1 4
2 3
Enter starting vertex: 0
```
Output:
```
DFS Traversal starting from vertex 0: 0 1 3 2 4
```
Explanation:
- Starts at 0, visits 1, then 3, backtracks to 1, visits 4, backtracks to 0, visits 2.

📌 Final Summary
This implementation provides a recursive DFS solution for an undirected graph, meeting all assignment requirements. It uses an adjacency list, handles user input, and ensures all vertices are visited, even in disconnected graphs. The line-by-line explanation, functional details, and theory make it a complete resource for understanding DFS.
"""