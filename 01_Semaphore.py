# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 10:52:37 2022

@author: Elena
"""

from multiprocessing import Process, BoundedSemaphore
from multiprocessing import current_process
from multiprocessing import Value, Array

N = 8

def task(common, tid, semaphore):
    a = 0
    for i in range(100):
         print(f'{tid}−{i}: Non−critical Section')
         a += 1
         print(f'{tid}−{i}: End of non−critical Section')
         try:
             semaphore.acquire()
             print(f'{tid}−{i}: Critical section')
             v = common.value + 1
             print(f'{tid}−{i}: Inside critical section')
             common.value = v
             print(f'{tid}−{i}: End of critical section')
         finally:
             semaphore.release()
         
def main():
     lp = []
     common = Value('i', 0)
     semaphore = BoundedSemaphore(1)
     for tid in range(N):
         lp.append(Process(target=task, args=(common, tid, semaphore))) #lista con los 8 procesos
     print (f"Valor inicial del contador {common.value}")
     for p in lp:
         p.start()
     for p in lp:
         p.join()
     print (f"Valor final del contador {common.value}")
     print ("fin")
     
if __name__ == "__main__":
    main()