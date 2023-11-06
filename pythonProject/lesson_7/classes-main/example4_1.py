# staticmethod

import time


class Counter:

    def __init__(self):
        self.start = self.get_current_time()

    def delta(self):
        return self.get_current_time() - self.start

    @staticmethod
    def get_current_time():
        return time.time()


counter = Counter()
print(counter.get_current_time())
print(Counter.get_current_time())
