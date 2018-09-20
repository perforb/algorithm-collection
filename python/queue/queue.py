# -*- coding: utf-8 -*-
# https://en.wikipedia.org/wiki/Round-robin_scheduling
# https://en.wikipedia.org/wiki/Circular_buffer


class Task:

    def __init__(self, name, total_time):
        self._name = name
        self._total_time = total_time

    @property
    def name(self):
        return self._name

    @property
    def total_time(self):
        return self._total_time

    @total_time.setter
    def total_time(self, remaining_time):
        self._total_time = remaining_time


class Queue:

    def __init__(self, length):
        self._head = 0
        self._tail = 0
        self._length = length
        self._queue = [None] * length

    def is_empty(self):
        return self._head == self._tail

    def is_full(self):
        return self._head == (self._tail + 1) % self._length

    def enqueue(self, task):
        if self.is_full():
            raise RuntimeError("Queue is full.")

        self._queue[self._tail] = task

        if self._tail + 1 == self._length:
            self._tail = 0
        else:
            self._tail += 1

    def dequeue(self):
        if self.is_empty():
            raise RuntimeError("Queue is empty.")

        task = self._queue[self._head]

        if self._head + 1 == self._length:
            self._head = 0
        else:
            self._head += 1

        return task


class RoundRobinScheduling:

    def __init__(self, queue, quantum=100):
        self._queue = queue
        self._quantum = quantum

    def simulate(self):
        queue = self._queue
        quantum = self._quantum
        elapse = 0

        while not queue.is_empty():
            task = queue.dequeue()
            if quantum < task.total_time:
                task.total_time = task.total_time - quantum
                elapse += quantum
                queue.enqueue(task)
            else:
                elapse += task.total_time
                print(f"Done {task.name}. elapse: {elapse}")

        print(f"Done all tasks. elapse: {elapse}")


if __name__ == "__main__":
    pass
