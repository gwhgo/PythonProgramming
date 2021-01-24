import os, time
import sys

def counter(count,Id):
    if Id == 3:
        sys.exit(0)
    for i in range(count):
        time.sleep(1)
        print('[%s] => %s' % (os.getpid(),i))
    

for i in range(5):
    pid = os.fork()
    if pid != 0:
        print("Process %d spawned" % pid)
    else:
        counter(5,i)
        os._exit(0)
