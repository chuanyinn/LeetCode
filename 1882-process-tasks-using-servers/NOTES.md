Priority Queues: Use two priority queues:
- One to keep track of free servers (free_servers), prioritized by server weight and index.
- Another to keep track of busy servers (busy_servers), prioritized by the time they become free.
Task Queue: Keep a queue of tasks that need to be processed (task_queue).

Simulation: Process tasks and servers in a chronological order:
- At each second, add the current task to the task queue.
- Move servers from the busy queue to the free queue if their busy time is up.
- Assign tasks from the task queue to free servers as long as there are free servers and tasks in the queue.​
