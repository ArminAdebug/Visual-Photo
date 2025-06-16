import sys
import time

class ProcessBar:
    def __init__(self, max, length_time=False, time_remain=False):
        self.max = max
        self.show_time = length_time
        self.start_time = time.time()
        self.show_time_remain = time_remain
        self.time_remain = 0
        self.processed_count = 0
        
    def next(self, current):
        self.processed_count += 1
            
        percent = ((self.processed_count / self.max) * 100) if current else 0
        
        if percent > 0:
            self.time_remain = (time.time() - self.show_time / percent) * (100 - percent)
        else:
            self.time_remain = 0
            
        bar_length = 50
        filled_length = int(bar_length * self.processed_count // self.max)
        bar = '█' * filled_length + '-' * (bar_length - filled_length)
        
        sys.stdout.write(f"\rprocess: |{bar}| {percent:.1f}% |{f" {time.time() - self.start_time:.2f} |" if self.show_time else ""}{f" {self.time_remain:.2f} |" if self.show_time_remain else ""}")
        sys.stdout.flush() 