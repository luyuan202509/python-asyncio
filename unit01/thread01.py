import os 
import threading

print(f'Python process running with process id: {os.getpid()}')
totle_threads = threading.active_count()
thread_name = threading.current_thread().name


print(f'Total threads: {totle_threads}')
print(f'Current thread name: {thread_name}')

'''
Python process running with process id: 70272
Total threads: 1
Current thread name: MainThread
'''