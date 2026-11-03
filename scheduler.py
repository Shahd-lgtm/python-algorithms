
import heapq

def schedule_tasks(tasks):
    heap = []

    for task in tasks:
        priority, name = task
        heapq.heappush(heap, (priority, name))

    print("Task Scheduling:")

    while heap:
        priority, name = heapq.heappop(heap)
        print(f"Task: {name}, Priority: {priority}")


# Example
tasks = [
    (2, "Study"),
    (1, "Assignment"),
    (3, "Revision"),
    (1, "Project")
]

schedule_tasks(tasks)
