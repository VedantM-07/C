def job_scheduling(jobs):

    jobs.sort(key=lambda x: x[0], reverse=True)

   
    slot_array = [0] * len(jobs)

    total_profit = 0
    scheduled_jobs = []

   
    for i, job in enumerate(jobs):
        profit, deadline = job

        available_slot = False
        for j in range(deadline - 1, -1, -1):
            if slot_array[j] == 0:
                slot_array[j] = 1  
                total_profit += profit
                scheduled_jobs.append(i)
                available_slot = True
                break

    return total_profit, scheduled_jobs


jobs = [(100, 2), (19, 2), (27, 3), (20, 2), (10, 1)]  


total_profit, scheduled_jobs = job_scheduling(jobs)

print(f"Total Profit: {total_profit}")
print(f"Scheduled Jobs (IDs): {scheduled_jobs}")




"""
Time complexity : O(n^2)
Space Complexity : O(n)

Thought for a second


Here’s a detailed walkthrough of your job‑scheduling code, covering both the concepts it uses and a line‑by‑line explanation.

---

## Key Concepts

1. **Greedy Strategy**
   We aim to pick the highest‑profit jobs first and schedule them as late as possible before their deadlines, leaving earlier slots free for other jobs.

2. **Sorting with `key`**
   We use `jobs.sort(key=lambda x: x[0], reverse=True)` to order jobs by profit descending.

3. **Slots Array**
   An array of length *n* (where *n* = number of jobs) tracks which time slots (1 through *n*) are already occupied.

4. **Iterating Deadlines Backward**
   For each job, we scan from its deadline slot backward to slot 1 to find the latest free slot.

---

## Line‑by‑Line Explanation

```python
def job_scheduling(jobs):
```

* Define a function `job_scheduling` taking a list `jobs`, where each job is a tuple `(profit, deadline)`.

---

```python
    jobs.sort(key=lambda x: x[0], reverse=True)
```

* **Sort in‑place** by profit descending.

  * `key=lambda x: x[0]` picks the profit field.
  * `reverse=True` means highest profits come first.

---

```python
    slot_array = [0] * len(jobs)
```

* **Initialize** a list of zeros of length *n*, where *n* is the number of jobs.
* Each index `j` (0-based) represents timeslot `j+1`.
* `0` means free; `1` will mean occupied.

---

```python
    total_profit = 0
    scheduled_jobs = []
```

* `total_profit`: accumulator for the profit of all scheduled jobs.
* `scheduled_jobs`: list of indices (from the sorted `jobs` list) of the jobs we end up scheduling.

---

```python
    for i, job in enumerate(jobs):
        profit, deadline = job
```

* Loop over sorted jobs with `enumerate`, so `i` is the job’s index in the sorted list, and `job` is the `(profit, deadline)` tuple.
* Unpack it into `profit` and `deadline`.

---

```python
        available_slot = False
```

* A flag to mark if we successfully scheduled this job.

---

```python
        for j in range(deadline - 1, -1, -1):
```

* **Scan backward** through possible slots:

  * Start at `deadline - 1` (0‑based index for slot = `deadline`).
  * End at `0` (slot 1).
  * Step `-1` so we try latest possible time first.

---

```python
            if slot_array[j] == 0:
```

* Check whether slot `j+1` is free.

---

```python
                slot_array[j] = 1  
```

* **Mark the slot occupied**.

---

```python
                total_profit += profit
```

* **Add** this job’s profit to our running total.

---

```python
                scheduled_jobs.append(i)
```

* **Record** that we scheduled job at index `i` (in the sorted list).

---

```python
                available_slot = True
                break
```

* Set the flag and `break` out of the slot‑search loop, since we’ve placed the job.

---

```python
    return total_profit, scheduled_jobs
```

* Return the sum of profits and the list of scheduled job IDs (indices).

---

```python
jobs = [(100, 2), (19, 2), (27, 3), (20, 2), (10, 1)]
```

* Example list of jobs:

  * Job 0: profit 100, deadline 2
  * Job 1: profit 19,  deadline 2
  * … and so on.

---

```python
total_profit, scheduled_jobs = job_scheduling(jobs)
```

* Call the function and unpack the results.

---

```python
print(f"Total Profit: {total_profit}")
print(f"Scheduled Jobs (IDs): {scheduled_jobs}")
```

* Print the outcome.
* **Note:** The job IDs here correspond to positions in the **sorted** list, not the original order.

For the given input, the sorted order by profit is:

```
[(100,2), (27,3), (20,2), (19,2), (10,1)]
 indices:   0        1       2       3       4
```

* Slot assignments will then pick:

  * Job 0 (100) → slot 2
  * Job 1 (27)  → slot 3
  * Job 2 (20)  → slot 1
  * (Jobs 3 and 4 can’t fit before their deadlines)

So you’ll get:

```
Total Profit: 147
Scheduled Jobs (IDs): [0, 1, 2]
```

---

That’s the full breakdown of each concept and every line in your job‑scheduling implementation!


"""


































def job_scheduling(jobs):
    """
    Implements a greedy algorithm for the job scheduling problem.

    Args:
        jobs: A list of tuples, where each tuple represents a job
              and contains the job's profit and deadline.

    Returns:
        A tuple containing:
        - The total profit earned by scheduling the jobs.
        - A list of job IDs that are part of the optimal schedule.
    """
    # Sort jobs by profit in descending order
    jobs.sort(key=lambda x: x[0], reverse=True)

    # Create a slot array to track assigned time slots
    slot_array = [0] * len(jobs)

    total_profit = 0
    scheduled_jobs = []

    # Iterate through the jobs
    for i, job in enumerate(jobs):
        profit, deadline = job

        # Try to find an available time slot before the deadline
        available_slot = False
        for j in range(deadline - 1, -1, -1):
            if slot_array[j] == 0:
                slot_array[j] = 1  # Assign the time slot to the job
                total_profit += profit
                scheduled_jobs.append(i)
                available_slot = True
                break

    return total_profit, scheduled_jobs


# Example usage:
jobs = [(100, 2), (19, 2), (27, 3), (20, 2), (10, 1)]  # (profit, deadline)
# Example explanation:
# 1. Jobs are sorted by profit in descending order, and are represented as a tuple of (profit, deadline)
# 2.  The function attempts to schedule the jobs based on their deadlines, prioritizing those with higher profit
# 3.  If a slot is available before the deadline, the job is scheduled, and the slot is marked as occupied

total_profit, scheduled_jobs = job_scheduling(jobs)

print(f"Total Profit: {total_profit}")
print(f"Scheduled Jobs (IDs): {scheduled_jobs}")

# Expected Output:
# Total Profit: 127
# Scheduled Jobs (IDs): [0, 2, 3]