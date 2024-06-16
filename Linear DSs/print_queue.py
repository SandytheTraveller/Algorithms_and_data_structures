import random
from queue import Queue

class Printer:
    def __init__(self, max_queue_len):
        self.printQueue = Queue()
        self.max_queue_len = max_queue_len

    def add_task(self, task):
        if self.printQueue.size() < self.max_queue_len:
            self.printQueue.enque(task)
            print('Task', task, 'enqueued')
        else:
            print('The queue is full, task', task, 'refused')

    def complete_task(self):
        if not self.printQueue.isEmpty():
            print('Task', self.printQueue.deque(), 'printed')


def simulation(task_number, max_queue_len):
    myPrinter = Printer(max_queue_len)
    tasks_list = list(range(task_number, 0, -1))

    # periodically, with a 50% probability, either the printer receives a new task,
    # or a task is completed
    while len(tasks_list) > 0:
        if random.random() >= 0.5:
            myPrinter.add_task(tasks_list.pop())
        else:
            myPrinter.complete_task()