import multiprocessing  as mp 
import os 

def hello_from_precess():
    print(f"Hello from child process {os.getgid()}!")

if __name__ == '__main__':
    print(f"Hello from parent process {os.getgid()}!")
    p = mp.Process(target=hello_from_precess)
    p.start()
    p.join()

