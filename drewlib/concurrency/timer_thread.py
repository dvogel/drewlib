# -*- coding: utf-8 -*-

import threading
import time
import datetime

__all__ = ['TimerThread']

class TimerThread(threading.Thread):
    """
    Sets the `event` every `interval` seconds.
    Definitely overkill.
    """

    def __init__(self, interval, event=None, *args, **kwargs):
        super(TimerThread, self).__init__(*args, **kwargs)
        # interval = seconds between events
        self.interval = interval
        self.event = event or threading.Event()
        self.daemon = True
        self.last_beat = datetime.datetime.now()

    def run(self):
        while True:
            now = datetime.datetime.now()
            since = now - self.last_beat
            if since.total_seconds() >= self.interval:
                self.event.set()
                self.last_beat = now
            else:
                time.sleep(self.interval)
