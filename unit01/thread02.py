import threading


def hello_from_thread():
    print(f'hello from thread: {threading.current_thread().name}')

hello_thread = threading.Thread(target=hello_from_thread)
hello_thread.start()

totle_threads   = threading.active_count()
thread_name     = threading.current_thread().name

print(f'Python is currently running : {totle_threads}')
print(f'Current thread name: {thread_name}')

hello_thread.join()