"""
This module stores the round robin scheduler
simulator class
"""

from multiprocessing import Value
from queue import Queue
from time import sleep

class SchedulerRR:
    def __init__(self):
        self.__settings = {
            'p_list': [],
            'p_queue': None,
        }