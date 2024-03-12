"""
This module stores the round robin scheduler
simulator class
"""
from time import sleep

from threading import Thread

from random import randint

from .scheduler import Scheduler

class SchedulerRR(Scheduler):
    """
    Inheriting from the Scheduler class.
    This class emulates a Round Robin type
    scheduler.
    """
    def __init__(self, arg_dict=None):
        super().__init__(arg_dict)
        self._append_new_settings()
        if isinstance(arg_dict, dict):
            if arg_dict.get('time_out'):
                self._time_out = arg_dict['time_out']

    @property
    def _SECOND(self):
        return 1_000_000_000

    def _append_new_settings(self):
        self._settings['time_out'] = 100

    def run(self):
        self._start_process()
        scheduler = Thread(target=self._schedule_process)

        scheduler.start()

    def _schedule_process(self):
        while not self.p_queue.empty():
            process_dict = self.p_queue.get()
            cur_state = process_dict['cur_state']
            finished_state = process_dict['finished_state']
            if cur_state.value < finished_state.value:
                process_dict['timed_out'].value = False
                sleep(self._time_out / self._SECOND)
                process_dict['timed_out'].value = True

                self.p_queue.put(process_dict)

    def _start_process(self):
        if self.p_list:
            for process, _ in self.p_list:
                process.start()

    @property
    def _time_out(self) -> int:
        return self._settings['time_out']

    @_time_out.setter
    def _time_out(self, time_out:int):
        if isinstance(time_out, int) and time_out > 0:
            self._settings['time_out'] = time_out
        else:
            self._settings['time_out'] = 100

    def _process_callback(self, process_dict, args):
        cur_state = process_dict['cur_state']
        finished_state = process_dict['finished_state']
        halt = process_dict['halt']
        timed_out = process_dict['timed_out']

        while cur_state.value <  finished_state.value:
            if not halt.value and not timed_out.value:
                cur_state.value += 1
                sleep(randint(1, self._time_out) / self._SECOND)



