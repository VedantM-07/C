# 8.Implement a solution for a Constraint Satisfaction Problem for Graph Coloring .



def is_safe(node, color, graph, c):
    for neighbor in graph[node]:
        if color[neighbor] == c:
            return False
    return True

def solve(node, graph, m, color):
    if node == len(graph):
        return True
    for c in range(1, m + 1):
        if is_safe(node, color, graph, c):
            color[node] = c
            if solve(node + 1, graph, m, color):
                return True
            color[node] = 0
    return False

def graph_coloring(graph, m):
    color = [0] * len(graph)
    if solve(0, graph, m, color):
        print("\nColor Assignments:", color)
    else:
        print("\nNo solution with", m, "colors.")

# ------------------------
# Main Program with Input
# ------------------------
if __name__ == "__main__":
    n = int(input("Enter number of vertices: "))
    e = int(input("Enter number of edges: "))
    graph = {i: [] for i in range(n)}

    print("Enter edges (format: u v):")
    for _ in range(e):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    m = int(input("Enter number of colors: "))
    graph_coloring(graph, m)






# ------------------------- Explaination ------------------------

"""


Sure! Here's a **line-by-line and function-by-function explanation** of the user-input-based Graph Coloring code using **backtracking** (Constraint Satisfaction Problem):

---

### 🔸 `is_safe(node, color, graph, c)`

```python
def is_safe(node, color, graph, c):
```

* **Purpose**: Checks if it's safe to assign color `c` to `node`.
* **Parameters**:

  * `node`: the current vertex being colored.
  * `color`: list holding color assigned to each vertex.
  * `graph`: adjacency list representation of the graph.
  * `c`: the color we're trying to assign to `node`.

```python
    for neighbor in graph[node]:
        if color[neighbor] == c:
            return False
```

* Loops through all neighbors of the node.
* If any neighbor already has the same color `c`, return `False` (conflict).

```python
    return True
```

* If no neighbor has color `c`, return `True` — assignment is safe.

---

### 🔸 `solve(node, graph, m, color)`

```python
def solve(node, graph, m, color):
```

* **Purpose**: Recursive backtracking function to assign colors to all nodes.

```python
    if node == len(graph):
        return True
```

* Base case: If all vertices are assigned a color, return `True` — solution found.

```python
    for c in range(1, m + 1):
```

* Try every color from 1 to `m` for the current node.

```python
        if is_safe(node, color, graph, c):
            color[node] = c
```

* If it's safe, assign color `c` to this node.

```python
            if solve(node + 1, graph, m, color):
                return True
```

* Recurse to next node. If successful, propagate `True`.

```python
            color[node] = 0
```

* Backtrack: Unassign the color if further steps failed.

```python
    return False
```

* If no color can be assigned, return `False`.

---

### 🔸 `graph_coloring(graph, m)`

```python
def graph_coloring(graph, m):
```

* **Purpose**: Initializes the color list and starts the recursive coloring.

```python
    color = [0] * len(graph)
```

* Creates a list of size equal to number of vertices, initialized with 0 (uncolored).

```python
    if solve(0, graph, m, color):
        print("\nColor Assignments:", color)
    else:
        print("\nNo solution with", m, "colors.")
```

* Starts coloring from node `0`.
* If coloring succeeds, prints the final assignment.
* Otherwise, notifies that it's impossible with given colors.

---

### 🔸 `Main Program with User Input`

```python
if __name__ == "__main__":
```

* Entry point of the program when run directly.

```python
    n = int(input("Enter number of vertices: "))
```

* Accepts number of vertices (nodes in the graph).

```python
    e = int(input("Enter number of edges: "))
```

* Accepts number of edges (connections).

```python
    graph = {i: [] for i in range(n)}
```

* Initializes an empty adjacency list for each vertex.

```python
    print("Enter edges (format: u v):")
    for _ in range(e):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
```

* Accepts `e` pairs of vertex connections.
* Adds each edge bidirectionally since it’s an undirected graph.

```python
    m = int(input("Enter number of colors: "))
```

* Accepts the number of available colors.

```python
    graph_coloring(graph, m)
```

* Calls the main function to solve the graph coloring problem.

---

### ✅ Summary of Functions:

| Function           | Purpose                                            |
| ------------------ | -------------------------------------------------- |
| `is_safe()`        | Check if a color can be safely assigned to a node. |
| `solve()`          | Recursively assign colors using backtracking.      |
| `graph_coloring()` | Set up color list and start solving.               |
| `main block`       | Get user input and call the solver.                |

---





"""





# Theory :

"""
🎯 Problem Statement
Implement a solution for a Constraint Satisfaction Problem (CSP) for Graph Coloring using Backtracking.

🔍 1. What is a Constraint Satisfaction Problem (CSP)?
📌 Definition:
A Constraint Satisfaction Problem is defined by:

Variables: Entities you want to assign values to.

Domains: The set of possible values each variable can take.

Constraints: Rules that limit how values can be assigned.

👨‍💻 In Graph Coloring:
Variables: Each vertex (node) in the graph.

Domain: A finite set of colors (e.g., {1, 2, ..., m}).

Constraint: No two adjacent vertices can have the same color.

🖼️ 2. What is Graph Coloring?
Graph coloring is a classical CSP where we aim to:

Assign a color to each vertex.

Ensure adjacent vertices (connected by an edge) do not share the same color.

Use at most m colors.

✅ Real-world Applications:
Timetable Scheduling: No overlapping exams/classes for same student group.

Map Coloring: No two neighboring countries share the same color.

Register Allocation: In compiler design to avoid register conflicts.

Frequency Assignment: In mobile networks to avoid signal interference.

🧩 3. Core Concepts and Algorithms Used
🔷 A. Backtracking Algorithm
Definition:
Backtracking is a recursive algorithm that tries all possibilities to find a solution and undoes previous steps (backtracks) when a constraint is violated.

Steps in Graph Coloring:

Start from vertex 0.

Try assigning the first available color (greedy trial).

Check if it violates constraints.

If not, move to the next vertex.

If it leads to a conflict later, go back and try another color (backtrack).

Repeat until all vertices are assigned valid colors or return failure.

🔷 B. is_safe() Function (Constraint Checker)
Purpose:
Before assigning a color to a vertex, this function checks:

If any of its adjacent vertices already have the same color.

If yes → return False.

If no → return True.

This function implements the main constraint of the problem.

🔷 C. solve() Function (Recursive Coloring)
Purpose:
The solve() function uses backtracking:

It assigns colors to vertices one by one.

It uses is_safe() to ensure constraints are met.

If it reaches a dead-end, it backtracks and tries a different color.

This function drives the core logic of assigning colors recursively.

🔷 D. graph_coloring() Function (Driver)
Purpose:

Initializes the color array.

Starts the coloring process from vertex 0.

Displays the result or reports failure.

🔷 E. Graph Representation (Adjacency List)
We represent the graph using an adjacency list:

python
Copy
Edit
graph = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1]
}
Each key is a node.

The value is a list of nodes connected to it.

This format is space-efficient for sparse graphs.

📊 4. Complexity Analysis
⏳ Time Complexity:
In the worst case, the algorithm checks all color combinations.

For n vertices and m colors → O(m^n) (exponential).

That's why it's suitable for small or medium-sized graphs only.

💾 Space Complexity:
O(n) for the color assignment array.

O(n) recursion stack in worst case (depth = number of vertices).

⚙️ 5. How the Code Works (Flow Summary)
Step	Description
1	User inputs number of vertices, edges, and color count.
2	The graph is built using an adjacency list.
3	A color array is initialized with 0 (uncolored).
4	The solve() function is called with vertex 0.
5	It tries each color one by one for a vertex.
6	The is_safe() function checks constraints.
7	If valid, it assigns the color and moves to the next node.
8	If coloring fails later, it resets (backtracks) the current vertex color to 0 and tries next.
9	If all vertices are successfully colored, the solution is printed.
10	If not, the program prints “No solution with m colors”.

🧠 6. Additional CSP Concepts That Apply Here
CSP Concept	Applied How?
Domain Reduction	Skip colors already used by adjacent nodes.
Forward Checking	We check validity (constraints) before assigning.
Backtracking Search	Core algorithm that tries and undoes steps.
Greedy Heuristic	Tries the first color that seems valid (no advanced heuristics like MRV used).

📌 Final Summary
Graph coloring as a CSP is a great example of:

Problem modeling using variables, domains, and constraints.

Solving it via recursive backtracking.

Efficiently checking constraints with adjacency lists.

Applying core AI and logic programming concepts.! Here are **10 viva-style questions and answers** based on the **Graph Coloring CSP using Backtracking**. These cover theoretical, practical, and implementation aspects, and are tailored for both **internal and external viva** evaluations.

---

1. What is a Constraint Satisfaction Problem (CSP)?
Answer:
A CSP is a type of problem where:

You have a set of variables, each with a domain of values,

And a set of constraints that specify allowable combinations of values.
The goal is to assign values to variables such that all constraints are satisfied.

2. How is graph coloring formulated as a CSP?
Answer:

Variables: Each vertex in the graph.

Domain: A finite set of colors (e.g., {1, 2, 3}).

Constraint: No two adjacent vertices should have the same color.

3. What algorithm is used to solve the Graph Coloring CSP in your code?
Answer:
We use the Backtracking algorithm, which tries to assign colors to vertices one by one, and undoes choices (backtracks) if any constraint is violated.

4. What is the role of the is_safe() function?
Answer:
The is_safe() function checks whether a given color can be assigned to a vertex without violating the constraint that no two adjacent vertices share the same color.

5. What is the worst-case time complexity of this solution?
Answer:
The worst-case time complexity is O(m^n), where:

m = number of colors

n = number of vertices
This is because we may try every color for every vertex in the worst case.

6. Why do we use an adjacency list to represent the graph?
Answer:
An adjacency list is space-efficient, especially for sparse graphs. It also allows us to quickly access all neighbors of a given vertex to check constraints.

7. Can this algorithm solve the problem if the number of colors is less than the chromatic number?
Answer:
No. If the number of colors is less than the graph’s chromatic number (minimum number of colors needed), then no solution exists, and the algorithm will return failure.

8. What is backtracking, and why is it suitable for this problem?
Answer:
Backtracking is a depth-first search strategy that builds solutions incrementally and abandons partial solutions as soon as it detects a conflict.
It is suitable for graph coloring because it explores all possible color assignments and ensures constraint satisfaction.

9. What happens if a graph is not colorable with the given number of colors?
Answer:
The backtracking function will exhaust all possibilities and return False, indicating that no valid coloring exists with the given number of colors.

10. What are some real-world applications of graph coloring?
Answer:

Scheduling problems (e.g., exam or class scheduling)

Map coloring (e.g., coloring countries so neighbors differ)

Register allocation in compilers

Frequency assignment in wireless networks




"""