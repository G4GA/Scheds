"""
This module has the scheduler parent class
"""

from multiprocessing import Value
from multiprocessing import Process
from multiprocessing import cpu_count
from queue import Queue

class Scheduler:
    def __init__(self, arg_dict=None):
        self._settings = {
            'p_count': cpu_count(),
            'p_list': [],
            'p_queue': Queue(),
            'cur_p': {}
        }

        if isinstance(arg_dict, dict):
            if arg_dict.get('p_count'):
                self.p_count = arg_dict['p_count']

    @property
    def p_count(self):
        """
        Returns number of processes to be run
        """
        return self._settings['p_count']

    @p_count.setter
    def p_count(self, p_count:int):
        """
        Sets p_count value

        Args:
            p_count (int): Number of processes to be
            instanciated
        """
        if isinstance(p_count, int) and p_count > 0:
            self._settings['p_count'] = p_count
        else:
            self._settings['p_count'] = cpu_count

    @property
    def p_list(self) -> list:
        """
        Returns a list of dict that contain
        process information
        """
        return self._settings['p_list']

    @property
    def _p_queue(self) -> Queue:
        """
        Returns the process queue
        """
        return self._settings['p_queue']

    def run(self):
        pass

    def _process_callback(self, cur_state, halt, args=None):
        pass

    def _build_process(self, args=None):
        for i in range(self.p_count, args=None):
            cur_state = Value('I', 0)
            halt = Value('b', False)

            process_dict = {
                'index': i,
                'cur_state': cur_state,
                'halt': halt,
            }
            process = Process(target=self._process_callback, args=(cur_state, halt, args))
            self.p_list.append(process_dict)
            self._p_queue.put(process)
