import threading
import time

"""
thread class instances with state and run() for thread's action;
uese higher-level Java-like theading module object join method (
not mutexes or shared global vars) to know when threads are done 
in main parent thread; see library manual for more details on threading;
"""


class Mythread(threading.Thread):               # subclass Thread object
    def __init__(self, myId, count, mutex):     
        self.myId = myId                        
        self.count = count                      # per-thread state information
        self.mutex = mutex                      # shared objects, not globals
        threading.Thread.__init__(self)

    def run(self):                              # run provides thread logic
        time.sleep(1)                           # still sync stout access
        for i in range(self.count):
            with self.mutex:
                print('[%s] => %s' % (self.myId,i))


stdoutmutex = threading.Lock()                  # smae as thread.allocate_lock()
threads = []

for i in range(10):
        thread = Mythread(i, 100, stdoutmutex)
        thread.start()
        threads.append(thread)

# try commenting below 2 lines code, see what happen?
# would the last code in this script run?
for thread in threads:
    thread.join()
print('Main thread exiting')

