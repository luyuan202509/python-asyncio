"""生成斐波那契数列并计算时间 """

import time
import threading 

def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


def fibs_with_threads():
    fortieth_thread = threading.Thread(target=fibonacci_recursive, args=(40,))
    forty_first_thread = threading.Thread(target=fibonacci_recursive, args=(41,))

    fortieth_thread.start()
    forty_first_thread.start()

    fortieth_thread.join()
    forty_first_thread.join()
    

if __name__ == '__main__':
    start_threads = time.time()
    fibs_with_threads()
    print(f'Time taken: {time.time() - start_threads}')
   