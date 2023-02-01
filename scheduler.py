import simpy
import random
import statistics as stats
import enum

class CPU(object):
    def __init__(self) -> None:
        pass

class Scheduler(object):

    all_tasks = []
    TASK_PROBABILITIES = [0.7, 0.2, 0.1]
    class TaskProirities(enum.Enum):
        LOW = 1
        MEDIUM = 2
        HIGH = 3


    def __init__(self, env, X, Y, process_count, simulation_time):
        self.env = env
        self.X = X
        self.Y = Y
        self.process_count = process_count
        self.simulation_time = simulation_time

    def job_creator(self, env, X, Y, process_count):
        for i in range(process_count):
            priority = random.choices(([p.value for p in self.TaskPriorities]),
                                       weights=self.TASK_PROBABILITIES, k=1)[0]
            pending_time = int(random.expovariate(X))
            yield env.timeout(pending_time)
            arrival_time = env.now
            service_time = int(random.expovariate(1/Y))
            task = Task(priority, arrival_time, service_time)
            self.all_tasks.append(task)
            print("Task created: ", task.priority, task.arrival_time, task.service_time)

        

    def job_loader(self, env, X, Y):
        while True:
            yield env.timeout(1)
            print("Job loader is working")


    def dispatcher(self, env, X, Y):
        while True:
            yield env.timeout(1)
            print("Dispatcher is working")            


class Task(object):
    def __init__(self, priority, arrival_time, service_time):
        self.priority = priority
        self.arrival_time = arrival_time
        self.service_time = service_time

