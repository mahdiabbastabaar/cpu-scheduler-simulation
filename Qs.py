import simpy

class Waiting_Queue:

    def __init__(self, name) -> None:
        self.name = name
        self.tasks = []

    def enqueue(self, task):
        self.tasks.append(task)
        task.current_queue = self

    def sort_tasks(self):
        self.tasks.sort(key= lambda x: x.priority.value + x.service_time * 0.001 )

    def dequeue(self, K):
        if self.tasks:
            count = min(self.length(), K)
            d_list = []
            for _ in range(count):
                d_list.append(self.tasks.pop())
            return d_list
        else:
            return None

    def remove(self, task):
        self.tasks.remove(task)

    def length(self):
        return len(self.tasks)
