"""
This module is for the scheduler class
"""
from random import randint
from time import sleep

from .scheduler import Scheduler

class SchedulerFCFS(Scheduler):
    """
    Inheriting from the abstract Scheduler class.
    This class emulates the behavior of an FCFS
    type scheduler.
    """
    def __init__(self):
        super().__init__()

    def run(self):
        process, _ = self._p_queue.get()
        while process != 'STOP':
            process.start()
            process.join()

    def _process_callback(self, cur_state, halt, finished_state, args=None):
        while cur_state.value <= finished_state.value:
            if not halt.value:
                cur_state.value += 1
                sleep(randint(1, 100) / 1_000)
