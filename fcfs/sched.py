"""
This module is for the scheduler class
"""

from multiprocessing import Process
from multiprocessing import Value
from multiprocessing import cpu_count
from queue import Queue
from random import randint
from time import sleep

class SchedulerFCFS:
    """
    This class will simulate a FCFS scheduler
    using the multiprocessing module
    """
    def __init__(self, arg_dict=None):
        self.__settings = {
            'p_count': cpu_count(),
            'p_queue': Queue(),
            'cur_p': {}
        }
        if arg_dict is not None and isinstance(arg_dict, dict):
            if arg_dict.get('p_count'):
                self.p_count = arg_dict['p_count']

    @property
    def cur_p(self):
        return self.__settings['cur_p']

    @cur_p.setter
    def cur_p(self, cur_p:dict):
        if isinstance(cur_p, dict):
            self.__settings['cur_p'] = cur_p

    def set_process_queue(self):
        for _ in range(self.p_count):
            p_value = Value('I', 0)
            p_finished = randint(1_500, 3_000)
            p_dict = {
                'cur_state': p_value,
                'p_fi_val': p_finished,
                'process': Process(target=self._dummy_process, args=(p_value, p_finished))
            }
            self.p_queue.put(p_dict)
        self.p_queue.put('STOP')

    def run_queue(self):
        self.cur_p = self._p_queue.get()
        while self.cur_p != 'STOP':
            self.cur_p['process'].start()
            self.cur_p['process'].join()
            self.cur_p = self.p_queue.get()

    @staticmethod
    def _dummy_process(cur_state, final_state:int):
        while cur_state.value < final_state:
            cur_state.value += 1
            sleep(randint(0, 100) / 300)


    @property
    def p_count(self) -> int:
        return self.__settings['p_count']

    @p_count.setter
    def p_count(self, process_count: int):
        if isinstance(process_count, int) and process_count > 0:
            self.__settings['p_count'] = process_count
        else:
            self.__settings['p_count'] = cpu_count()

    @property
    def p_queue(self) -> Queue:
        return self.__settings['p_queue']
