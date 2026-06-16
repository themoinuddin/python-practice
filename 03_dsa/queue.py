# queue.py
# Author: Moin Uddin

from collections import deque

queue = deque()

queue.append(1)
queue.append(2)
queue.append(3)
print("Queue:", queue)

queue.popleft()
print("After dequeue:", queue)

print("Front:", queue[0])
print("Empty?", len(queue) == 0)