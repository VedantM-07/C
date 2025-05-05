#7. Implement a solution for a Constraint Satisfaction Problem using Branch and Bound and Backtracking for n-queens problem
def is_safe(board, row, col, n):
    # Check for conflicts in the current row and previous columns
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check for conflicts in the upper diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check for conflicts in the lower diagonal
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens_util(board, col, n):
    if col == n:  # All queens placed successfully
        return True

    for row in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1  # Place queen

            if solve_n_queens_util(board, col + 1, n):
                return True

            board[row][col] = 0  # Backtrack

    return False

def solve_n_queens(n):
    board = [[0] * n for _ in range(n)]  # Initialize the board

    if solve_n_queens_util(board, 0, n):
        for row in board:
            print(" ".join("Q" if cell == 1 else "." for cell in row))
    else:
        print("No solution exists.")

# Example usage
n = 6  # Change the board size here
solve_n_queens(n)


'''
Theory of the N-Queens Problem

The N-Queens problem is a classical combinatorial challenge aiming to place NN queens on an N×NN×N chessboard so that no two queens threaten each other. A queen can attack another if they share the same row, column, or diagonal.

    For N=1N=1: 1 solution exists.

    For N=2N=2 or N=3N=3: No solutions exist.

    For N=4N=4: 2 unique solutions.

It is a Constraint Satisfaction Problem (CSP) where:

    Variables: Positions of queens on the board.

    Domain: Possible positions in each column.

    Constraints: No two queens share the same row, column, or diagonal.

Approach
Backtracking Algorithm:

    Start with an empty board.

    Place a queen in the first column.

    Move to the next column and place a queen that doesn't conflict with existing queens.

    If a conflict arises, backtrack by removing the last placed queen and trying the next row.

    Repeat until all queens are placed or all possibilities are exhausted.

Branch and Bound:

Prunes invalid branches early in the search, reducing the need to explore configurations that cannot lead to a solution.
Key Components in the Code

    is_safe Function: Ensures a queen can be safely placed without conflicts.

    Recursive solve_n_queens_util: Places queens column by column and backtracks on conflicts.

    solve_n_queens Function: Initializes the board and triggers the recursive solution. Prints the solution or indicates if none exists.

Complexity

    Time Complexity: O(N!)O(N!) in the worst case, but backtracking reduces actual runtime.

    Space Complexity: O(N2)O(N2) for the board and O(N)O(N) for the recursive stack.

Applications

    AI for constraint reasoning.

    Scheduling and resource allocation.

    Demonstration of backtracking and constraint-solving algorithms.
1. How can the backtracking algorithm for the N-Queens problem be optimized?

Answer:
The backtracking algorithm can be optimized in the following ways:

    Bitwise Representation: Use bit manipulation to track attacks on rows, diagonals, and anti-diagonals. This reduces space complexity and speeds up conflict checks.

    Early Termination: Prune branches of the search tree where placing additional queens becomes impossible.

    Symmetry Reduction: Exploit symmetry by considering only half of the possible placements in the first row (or column). For each solution, generate its symmetric counterpart.

    Heuristic Ordering: Use a heuristic to choose rows or columns based on their likelihood of success.

6. How can the algorithm be modified to count all possible solutions for a given NN?

Answer:
To count all solutions instead of finding just one:

    Modify the solve_n_queens_util function to not stop when it finds a valid placement. Instead, continue searching all possibilities.

    Maintain a counter variable that increments each time a valid configuration is found.

    Return the counter value at the end of the recursion.

Modified pseudo-code:

def solve_n_queens_count(board, col, n, count):
    if col == n:
        return count + 1  # Increment count when a solution is found

    for row in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            count = solve_n_queens_count(board, col + 1, n, count)
            board[row][col] = 0  # Backtrack

    return count

# Initialize with solve_n_queens_count(board, 0, n, 0)

11. What is the time complexity of solving the N-Queens problem for large NN, and how can it be reduced?

Answer:

    Worst-case Time Complexity: O(N!)O(N!), as each queen placement potentially leads to exploring N−1,N−2,...N−1,N−2,... rows for subsequent queens.

    Optimizations to Reduce Complexity:

        Pruning: Eliminate impossible placements early using constraints.

        Bitwise Implementation: Reduce the cost of safety checks.

        Symmetry Exploitation: Cut the search space by half (or more) using symmetry.

        Advanced Algorithms: Use genetic algorithms or simulated annealing for heuristic-based faster solutions.

15. What are practical applications of the N-Queens problem in scheduling or resource allocation?

Answer:
The N-Queens problem represents scenarios where mutually exclusive resource allocations are required:

    Job Scheduling: Assigning jobs to time slots without overlap in constraints.

    Network Optimization: Placing servers or routers in a network while avoiding interference.

    Seating Arrangements: Planning seating layouts in events where certain individuals should not be near each other.

    Timetable Design: Scheduling classes or exams to avoid clashes between subjects.

20. What is the mathematical significance of the N-Queens problem in combinatorics?

Answer:
The N-Queens problem is significant in combinatorics because:

    It demonstrates the enumeration of valid permutations under constraints.

    It involves placing objects (queens) into distinct groups (board cells) with conditions, which relates to the study of permutations and combinations.

    The problem highlights the symmetry and rotational invariance in mathematical structures.

    It’s an example of constraint satisfaction problems where the solution space is systematically explored.

23. How is the N-Queens problem analogous to other real-world scheduling and placement problems?

Answer:
The N-Queens problem is analogous to:

    Examination Timetabling: Assigning exams to rooms and times while avoiding conflicts for students taking multiple exams.

    Urban Planning: Placing facilities (like schools or hospitals) in a city such that they don’t interfere with each other’s services or zones.

    CPU Task Scheduling: Allocating tasks to processor cores without overlaps in execution or resource contention.
    
Here’s a line-by-line explanation of the code:
is_safe Function

def is_safe(board, row, col, n):

    Purpose: Checks if it's safe to place a queen at position (row, col) on the board.

    Parameters:

        board: Current state of the chessboard.

        row: Row index to check.

        col: Column index to check.

        n: Size of the board.

    for i in range(col):
        if board[row][i] == 1:
            return False

    Loops through all columns to the left of col in the current row.

    If a queen is already placed (1), returns False.

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    Checks the upper-left diagonal of the current position.

    If a queen exists in this diagonal, returns False.

    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    Checks the lower-left diagonal of the current position.

    If a queen exists in this diagonal, returns False.

    return True

    Returns True if no conflicts are found, meaning it's safe to place the queen.

solve_n_queens_util Function

def solve_n_queens_util(board, col, n):

    Purpose: Recursively places queens on the board using backtracking.

    Parameters:

        board: Current state of the chessboard.

        col: Current column to place a queen.

        n: Size of the board.

    if col == n:
        return True

    Base case: If all queens are placed (col == n), return True.

    for row in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1  # Place queen

    Iterates through all rows in the current column. If it's safe, places a queen (1).

            if solve_n_queens_util(board, col + 1, n):
                return True

    Recursively tries to place queens in the next column. If successful, returns True.

            board[row][col] = 0  # Backtrack

    If placing a queen doesn't lead to a solution, remove it (0) and try the next row.

    return False

    Returns False if no safe position is found in the current column.

solve_n_queens Function

def solve_n_queens(n):

    Purpose: Initializes the board and calls the utility function to solve the problem.

    Parameter:

        n: Size of the chessboard.

    board = [[0] * n for _ in range(n)]  # Initialize the board

    Creates an n x n board filled with 0.

    if solve_n_queens_util(board, 0, n):

    Calls the utility function starting from the first column (col = 0).

        for row in board:
            print(" ".join("Q" if cell == 1 else "." for cell in row))

    If a solution is found, prints the board with queens (Q) and empty spaces (.).

    else:
        print("No solution exists.")

    If no solution exists, prints a message.

Example Usage

n = 4  # Change the board size here
solve_n_queens(n)

    Calls the solve_n_queens function with n = 4 to solve the problem for a 4x4 board.

Key Points:

    Backtracking: The algorithm tries all possible placements of queens and backtracks when a conflict arises.

    Safety Check: The is_safe function ensures no two queens threaten each other.

    Recursive Approach: The solve_n_queens_util function divides the problem into smaller subproblems (placing queens column by column).
    Theory of the N-Queens Problem
What is the N-Queens Problem?

The n-queens problem is a classical combinatorial problem in computer science and mathematics. The objective is to place nn queens on an n×nn×n chessboard such that:

    No two queens threaten each other.

        A queen can attack another queen if they are in the same row, column, or diagonal.

For example:

    For n=1n=1, there is 1 solution.

    For n=2n=2 or n=3n=3, there are no solutions.

    For n=4n=4, there are 2 unique solutions.

Constraint Satisfaction Problem (CSP)

The n-queens problem is a type of Constraint Satisfaction Problem (CSP). In CSPs:

    Variables: Positions of the queens on the board.

    Domain: Possible positions in each column.

    Constraints: No two queens can share the same row, column, or diagonal.

The solution is achieved by assigning positions to queens while satisfying these constraints.
Approach to Solving the N-Queens Problem

    Backtracking Algorithm:

        Definition: Backtracking is a general algorithm for solving CSPs by exploring all possible configurations and "backing up" when a conflict arises.

        How it Works:

            Start with an empty board.

            Place a queen in the first column.

            Move to the next column and place another queen while ensuring it doesn’t conflict with existing queens.

            If a conflict arises, backtrack to the previous column and try the next row.

            Repeat until all queens are placed or all possibilities are exhausted.

    Branch and Bound:

        A form of backtracking that uses bounds to prune branches of the search tree that cannot possibly contain a valid solution.

        In the n-queens problem, "bounds" are defined by constraints such as rows and diagonals being safe.

Algorithm Explanation

    Initialization:

        The chessboard is initialized with all cells set to 0, where 0 indicates an empty cell.

    Recursive Function:

        For each column, the algorithm tries placing a queen in every row.

        If placing a queen in a position satisfies the constraints (checked using is_safe), the function recursively places queens in subsequent columns.

        If no valid position is found in a column, the algorithm backtracks by removing the last placed queen and trying the next possible position.

Complexity Analysis

    Time Complexity:

        The worst-case time complexity is O(n!)O(n!), as there are nn choices for the first queen, n−1n−1 for the second, and so on.

        Using backtracking and pruning reduces the actual runtime significantly for larger nn.

    Space Complexity:

        Space complexity is O(n2)O(n2) for the chessboard and O(n)O(n) for the recursive call stack.

Applications

    Artificial Intelligence:

        CSPs like the n-queens problem are common in AI for constraint-based reasoning.

    Operations Research:

        Used in scheduling and resource allocation problems.

    Algorithm Design:

        Serves as a classic example for understanding backtracking and branch-and-bound methods.

Variations and Extensions

    Counting Solutions:

        Instead of finding one solution, determine the total number of valid configurations.

    Large Board Optimization:

        Advanced algorithms like genetic algorithms, simulated annealing, and heuristic-based methods can solve larger boards efficiently.

    K-Queens Problem:

        A generalization where k≤nk≤n queens are placed on an n×nn×n board.

The n-queens problem is a foundational problem that illustrates the power of systematic search methods like backtracking and constraint-based reasoning.'''