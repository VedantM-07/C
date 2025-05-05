from collections import deque

def recursive_bfs(graph, queue, visited=None):
    if not queue:
        return
    
    if visited is None:
        visited = set()
    
    node = queue.popleft()  
    if node not in visited:
        print(node)  
        visited.add(node)    
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
    
    recursive_bfs(graph, queue, visited)

n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))
graph = {i: [] for i in range(n)}

print("Enter edges (format: u v):")
for _ in range(e):
   u, v = map(int, input().split())
   graph[u].append(v)
   graph[v].append(u)  # Undirected graph

start_vertex = int(input("Enter starting vertex: "))
print("Recursive BFS traversal:")
recursive_bfs(graph, deque([start_vertex]))















"""
  Thought for a second


Let’s walk through this code step by step, covering both the key Python concepts it uses and exactly what each line is doing.

---

## Concepts Used

1. **`collections.deque`**

   * A **deque** (“double-ended queue”) is a data structure from Python’s standard `collections` module.
   * It allows fast appends and pops from both ends (`append()`, `appendleft()`, `pop()`, `popleft()`) in O(1) time.
   * Here, we use it as our FIFO (first‑in, first‑out) queue for BFS.

2. **Recursive Function**

   * A function that calls itself.
   * We use recursion to process one node at a time and then immediately recurse to handle the rest of the queue.

3. **Breadth‑First Search (BFS)**

   * A graph‐traversal algorithm that explores neighbors level by level.
   * Normally implemented with a loop and a queue; here we instead use recursion + deque.

4. **`set` for Tracking “Visited”**

   * We keep a Python `set` of nodes already seen to avoid revisiting them (and potentially infinite loops in cyclic graphs).

5. **`if __name__ == "__main__":`**

   * A common Python idiom that ensures the “driver” code (graph definition and function call) runs only when the script is executed directly, not when it’s imported as a module.

---

## Line‑by‑Line Explanation

```python
from collections import deque
```

* **Import statement**
* Brings the `deque` class into our namespace so we can write `deque()` directly.

---

```python
def recursive_bfs(graph, queue, visited=None):
```

* **Function definition** for `recursive_bfs`.
* **Parameters:**

  * `graph`: a dict mapping each node to a list of its neighbors.
  * `queue`: a `deque` of nodes pending to visit.
  * `visited`: an optional set of nodes we’ve already printed/processed.

---

```python
    if not queue:
        return
```

* **Base case** of the recursion.
* If `queue` is empty (`not queue` is `True`), there are no more nodes to process—so simply return and unwind the recursion.

---

```python
    if visited is None:
        visited = set()
```

* **Initialize `visited`** on the first call.
* If the caller didn’t pass in a `visited` set (i.e. `visited=None`), we create an empty set now.

---

```python
    node = queue.popleft()
```

* **Dequeue the next node** to process.
* `popleft()` removes and returns the leftmost element of the deque => FIFO behavior.

---

```python
    if node not in visited:
```

* **Check if we’ve seen this node before.**
* If not, we’ll “visit” it by printing and marking it.

---

```python
        print(node)
        visited.add(node)
```

* **Visit the node:**

  1. **Print** its label.
  2. **Add** it to the `visited` set to avoid future repeats.

---

```python
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
```

* **Enqueue all unvisited neighbors** of the current node:

  * Iterate through `graph[node]` (the adjacency list).
  * For each neighbor not already in `visited`, do `queue.append(neighbor)`.
  * This ensures they’ll be processed in FIFO order after all nodes already in the queue.

---

```python
    recursive_bfs(graph, queue, visited)
```

* **Recursive call** to process the next node in the queue (and carry along our `visited` set).
* Continues until the base case `if not queue:` is met.

---

```python
if __name__ == "__main__":
```

* Only run the following “demo” code when the script is executed directly, not imported.

---

```python
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
```

* **Define a sample undirected graph** as an adjacency‐list dictionary.
* Each key is a node label; its value is the list of neighbors.

---

```python
    print("Recursive BFS traversal:")
    recursive_bfs(graph, deque(['A']))
```

1. **Print** a header.
2. **Start the BFS** by calling `recursive_bfs` with:

   * `graph` as defined.
   * A `deque` initialized with the starting node `['A']`.
   * `visited` defaults to `None`, so inside the function it becomes an empty set.

---

### What Happens When You Run It

1. **Queue** initially: `['A']`, **Visited**: `{}`
2. Dequeue `A` → Print `A` → mark visited → enqueue its neighbors `B, C` → Queue: `['B','C']`
3. Recurse…
4. Dequeue `B` → Print `B` → enqueue its unvisited neighbors `D, E` → Queue: `['C','D','E']`
5. Recurse…
6. Dequeue `C` → Print `C` → enqueue `F` → Queue: `['D','E','F']`
7. And so on, until the queue is empty.

Final printed order:

```
A
B
C
D
E
F
```

That’s a full breakdown of every Python feature and each line in the code!



     """